import cv2
import mediapipe as mp
import numpy as np
from config import STATIC_IMAGE_MODE, MODEL_COMPLEXITY, ENABLE_SEGMENTATION, MIN_DETECTION_CONFIDENCE



mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils


class PoseDetection:
    def __init__(self, static_image_mode=STATIC_IMAGE_MODE, model_complexity=MODEL_COMPLEXITY, 
                 enable_segmentation=ENABLE_SEGMENTATION, min_detection_confidence=MIN_DETECTION_CONFIDENCE):
        # self.static_image_mode = static_image_mode
        # self.model_complexity = model_complexity
        # self.enable_segmentation = enable_segmentation
        # self.min_detection_confidence = min_detection_confidence

        self.pose = mp_pose.Pose(static_image_mode=static_image_mode,
                            model_complexity=model_complexity,
                            enable_segmentation=enable_segmentation,
                            min_detection_confidence= min_detection_confidence)

    def get_pose(self, img_path, draw=True):
        
        img = cv2.imread(img_path)  
        if img is None:
            raise ValueError(f"Image at {img_path} could not be loaded.")

        # Get the height and width of the image
        height, width, _ = img.shape

        # Creating a black canvas with the same size as the image
        black_canvas = np.zeros((height, width, 3), dtype=np.uint8)


        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.pose.process(frame_rgb)
        if self.result.pose_landmarks:
            if draw:
                mp_draw.draw_landmarks(black_canvas, self.result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                

                ##mediapipe doesnt landmark the neck so i calculated it
                nose = self.result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
                left_shoulder = self.result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = self.result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            
                # Calculate the midpoint between the left and right shoulders
                midpoint_x = (left_shoulder.x + right_shoulder.x) / 2
                midpoint_y = (left_shoulder.y + right_shoulder.y) / 2
            
                # Convert normalized coordinates to image coordinates
                nose_coords = (int(nose.x * width), int(nose.y * height))
                midpoint_coords = (int(midpoint_x * width), int(midpoint_y * height))
            
                # Drawing a line from the nose to the midpoint of the shoulders
                cv2.line(black_canvas, nose_coords, midpoint_coords, (0, 255, 0), 2)  # Green line with thickness 2

        return black_canvas
    
    def save_image(self, img, filename = "static/processed_images/processed_image.jpg"):
        cv2.imwrite(filename, img)  
        return filename

    def get_positions(self, img, draw = False):
        positions = []
        if self.result.pose_landmarks:
            for id, landmark in enumerate(self.result.pose_landmarks.landmark):
                h,w, c = img.shape
                cy = int(landmark.y * h)
                cx = int(landmark.x * w)
                positions.append([id, cy, cx])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
        return positions




if __name__ == "__main__":
    pose_model = PoseDetection()
    print("Starting pose detection")
    img = pose_model.get_pose("static/raw_images/pose2.jpeg")
    print("Pose detection completed")
    cv2.imshow("Pose Detection", img)
            
        
cv2.waitKey(0)
cv2.destroyAllWindows()
import sys
sys.exit("Pose detection completed")
        

