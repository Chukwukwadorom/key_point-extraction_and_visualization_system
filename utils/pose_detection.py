import cv2
import mediapipe as mp
import numpy as np
from utils.image_utils import load_image
from utils.keypoints import skeleton_connections
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
     
        img = load_image(img_path)
    
        # Get the height and width of the image. convert to format used by cv2
        height, width, _ = img.shape
        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Creating a black canvas with the same size as the image
        black_canvas = np.zeros((height, width, 3), dtype=np.uint8)


        
        self.result = self.pose.process(frame_rgb)
        if self.result.pose_landmarks:
            if draw:
                mp_draw.draw_landmarks(black_canvas, self.result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                

                ##mediapipe doesnt landmark the neck so i calculated it using the mid point of the 2 sholders
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
                cv2.line(black_canvas, nose_coords, midpoint_coords, (255, 255, 255), 2)  # Green line with thickness 2

        return black_canvas 
    
    def draw_keypoints_on_canvas(self, keypoints, canvas_size=(400, 500)):
        """
        Draw keypoints on a black canvas without needing an image.

        :param keypoints: List of [x, y] coordinates for each keypoint.
        :param canvas_size: Tuple specifying the size (height, width) of the canvas.
        :return: np.ndarray representing the canvas with drawn keypoints and connections.
        """
        # Creating a black canvas
        canvas = np.zeros((*canvas_size, 3), dtype=np.uint8)


        # Normalize keypoints
        max_x, max_y = canvas_size[1], canvas_size[0]  # Width, Height
        normalized_keypoints = []
        for x, y in keypoints:
            normalized_x = int(x * max_x)  
            normalized_y = int(y * max_y)  
            normalized_keypoints.append((normalized_x, normalized_y))

        # Draw landmarks on the canvas
        for (x, y) in normalized_keypoints:
            cv2.circle(canvas, (x, y), 5, (0, 255, 0), -1)  # Draw keypoints as circles

        # Drawing skeleton by connecting the keypoints
        for connection in skeleton_connections:
            id1, id2 = connection
            if id1 < len(normalized_keypoints) and id2 < len(normalized_keypoints):
                x1, y1 = normalized_keypoints[id1]
                x2, y2 = normalized_keypoints[id2]
                cv2.line(canvas, (x1, y1), (x2, y2), (255, 255, 255), 2)  # White line with thickness 2

        ## solving the neck problem:
        # Now connect the nose to the midpoint of shoulders
        nose = normalized_keypoints[0]  
        left_shoulder = normalized_keypoints[11]  
        right_shoulder = normalized_keypoints[12]  

        # Calculate midpoint between left and right shoulder
        midpoint_x = (left_shoulder[0] + right_shoulder[0]) // 2
        midpoint_y = (left_shoulder[1] + right_shoulder[1]) // 2
        midpoint_coords = (midpoint_x, midpoint_y)

        # Draw the line from the nose to the midpoint of the shoulders
        cv2.line(canvas, nose, midpoint_coords, (255, 255, 255), 2) 
        
        
        return canvas


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

