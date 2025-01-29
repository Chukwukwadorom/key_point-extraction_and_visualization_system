from flask import Flask, request, jsonify, send_file
from utils.keypoints import preprocess_keypoints
from utils.pose_detection import PoseDetection
import json
import numpy as np
import cv2
from io import BytesIO

app = Flask(__name__)
pose_model = PoseDetection()

def convert_image_to_bytes(img):
    """Helper function to convert image to byte format to send in the response."""
    _, img_encoded = cv2.imencode('.jpeg', img)
    return BytesIO(img_encoded.tobytes())

@app.route("/")
def home():
    return "Welcome to the Keypoint Extraction System!"


@app.route("/process-image", methods=["POST"])
def process_image():
    if "image" in request.files:
        # Case 1: Image uploaded
        file = request.files["image"]
        if file.filename == '':
            return jsonify({"error": "No image uploaded"}), 400

        filepath = f"static/raw_images/{file.filename}"
        file.save(filepath)
        processed_img = pose_model.get_pose(filepath)
        processed_img_bytes = convert_image_to_bytes(processed_img)

        # Returning the image as a downloadable file
        return send_file(processed_img_bytes, 
                         as_attachment=True,  
                         download_name="processed_image.jpg", 
                         mimetype='image/jpeg')  

    return jsonify({"error": "No valid input found"}), 400


@app.route("/process-landmarks", methods=["POST"])
def process_landmarks():
    if "landmarks" in request.json:
        # Case 2: Landmarks provided
        landmarks = request.json["landmarks"]
        if not isinstance(landmarks, list) or len(landmarks) == 0:
            return jsonify({"error": "Invalid landmarks data"}), 400
        
        # Preprocess landmarks to extract and normalize (x, y)
        processed_keypoints = preprocess_keypoints(landmarks)
        
        # Use PoseDetection's draw_keypoints_on_canvas function to draw keypoints
        processed_img = pose_model.draw_keypoints_on_canvas(processed_keypoints)
        processed_img_bytes = convert_image_to_bytes(processed_img)

        # Returning the image as a downloadable file
        return send_file(processed_img_bytes, 
                         as_attachment=True, 
                         download_name="skeleton_image.jpg",  
                         mimetype='image/jpeg')  

    return jsonify({"error": "No landmarks data provided"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


