from flask import Flask, request, jsonify, send_file
from utils.pose_detection import PoseDetection
import json
import numpy as np
import cv2
from io import BytesIO

app = Flask(__name__)
pose_model = PoseDetection()

def convert_image_to_bytes(img):
    """Helper function to convert image to byte format to send in the response."""
    _, img_encoded = cv2.imencode('.jpg', img)
    return BytesIO(img_encoded.tobytes())

@app.route("/")
def home():
    return "Welcome to the Keypoint Extraction System!"


@app.route("/process", methods=["POST"])
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
                         as_attachment=True,  # This makes the file downloadable
                         download_name="processed_image.jpg", 
                         mimetype='image/jpeg')  

    elif "landmarks" in request.json:
        # Case 2: Landmarks provided
        landmarks = request.json["landmarks"]
        if not isinstance(landmarks, list) or len(landmarks) == 0:
            return jsonify({"error": "Invalid landmarks data"}), 400

        # Create a black canvas to draw the skeleton from landmarks
        height, width = 480, 640  
        black_canvas = np.zeros((height, width, 3), dtype=np.uint8)

        for landmark in landmarks:
            if len(landmark) != 3:
                continue
            id, y, x = landmark
            # Convert normalized coordinates back to image space
            cy, cx = int(y * height), int(x * width)
            cv2.circle(black_canvas, (cx, cy), 5, (0, 255, 0), -1)

        
        
        processed_img_bytes = convert_image_to_bytes(black_canvas)

        # Returning the image as a downloadable file
        return send_file(processed_img_bytes, 
                         as_attachment=True,  # This makes the file downloadable
                         download_name="skeleton_image.jpg",  
                         mimetype='image/jpeg')  

    return jsonify({"error": "No valid input found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
