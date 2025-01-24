from utils.pose_detection import PoseDetection
import cv2



### testing api with just landmarks
if __name__ == "__main__": 
    pose_model = PoseDetection()
    img = pose_model.get_pose("static/raw_images/pose2.jpeg")
    # print(pose_model.result.pose_landmarks)
    # print(pose_model.result.pose_landmarks)
    if pose_model.result.pose_landmarks:
        keypoints = []
        for landmark in pose_model.result.pose_landmarks.landmark:
            keypoints.append((landmark.x, landmark.y))
    
    imgg = pose_model.draw_keypoints_on_canvas(keypoints)
    cv2.imshow("Pose Detection", imgg)
    # print(keypoints)

    
            
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    import sys
    sys.exit("Pose detection completed")
            
    
    #curl -X POST -F "image=@pose3.jpeg" http://127.0.0.1:5000/process-image --output downloaded_image.jpg
