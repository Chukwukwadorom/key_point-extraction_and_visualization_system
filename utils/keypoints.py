import mediapipe as mp


skeleton_connections = [
        (mp.solutions.pose.PoseLandmark.NOSE.value, mp.solutions.pose.PoseLandmark.LEFT_EYE_INNER.value),
        (mp.solutions.pose.PoseLandmark.NOSE.value, mp.solutions.pose.PoseLandmark.LEFT_EYE.value),
        (mp.solutions.pose.PoseLandmark.NOSE.value, mp.solutions.pose.PoseLandmark.LEFT_EYE_OUTER.value),
        (mp.solutions.pose.PoseLandmark.NOSE.value, mp.solutions.pose.PoseLandmark.RIGHT_EYE_INNER.value),
        (mp.solutions.pose.PoseLandmark.NOSE.value, mp.solutions.pose.PoseLandmark.RIGHT_EYE.value),
        (mp.solutions.pose.PoseLandmark.NOSE.value, mp.solutions.pose.PoseLandmark.RIGHT_EYE_OUTER.value),
        (mp.solutions.pose.PoseLandmark.LEFT_EYE_INNER.value, mp.solutions.pose.PoseLandmark.LEFT_EYE.value),
        (mp.solutions.pose.PoseLandmark.LEFT_EYE.value, mp.solutions.pose.PoseLandmark.LEFT_EYE_OUTER.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_EYE_INNER.value, mp.solutions.pose.PoseLandmark.RIGHT_EYE.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_EYE.value, mp.solutions.pose.PoseLandmark.RIGHT_EYE_OUTER.value),
        (mp.solutions.pose.PoseLandmark.MOUTH_LEFT.value, mp.solutions.pose.PoseLandmark.MOUTH_RIGHT.value),
        (mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value, mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value),
        (mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value, mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value),
        (mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value, mp.solutions.pose.PoseLandmark.LEFT_WRIST.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value, mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value, mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value),
        (mp.solutions.pose.PoseLandmark.LEFT_SHOULDER.value, mp.solutions.pose.PoseLandmark.LEFT_HIP.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER.value, mp.solutions.pose.PoseLandmark.RIGHT_HIP.value),
        (mp.solutions.pose.PoseLandmark.LEFT_HIP.value, mp.solutions.pose.PoseLandmark.RIGHT_HIP.value),
        (mp.solutions.pose.PoseLandmark.LEFT_HIP.value, mp.solutions.pose.PoseLandmark.LEFT_KNEE.value),
        (mp.solutions.pose.PoseLandmark.LEFT_KNEE.value, mp.solutions.pose.PoseLandmark.LEFT_ANKLE.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_HIP.value, mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value),
        (mp.solutions.pose.PoseLandmark.RIGHT_KNEE.value, mp.solutions.pose.PoseLandmark.RIGHT_ANKLE.value),
    ]

def preprocess_keypoints(input_keypoints, height=480, width=640):
    """
    Preprocess the keypoints to extract and normalize them for canvas drawing.
    Returns:
        list: A list of normalized (x, y) tuples.
    """
    processed_keypoints = []

    if isinstance(input_keypoints, list):
        # Case 1: Process landmark dicts (Format 1)
        if isinstance(input_keypoints[0], dict):
            for landmark in input_keypoints:
                x = landmark.get('x', 0)
                y = landmark.get('y', 0)
                # Normalize to image dimensions (assuming x, y are between 0 and 1)
                normalized_x = int(x * width)
                normalized_y = int(y * height)
                processed_keypoints.append((normalized_x, normalized_y))
        
        # Case 2: Process tuples (Format 2)
        elif isinstance(input_keypoints[0], tuple):
            # This is already in the form (x, y) so no need to change
            processed_keypoints = input_keypoints
        else:
            raise ValueError("Invalid keypoint format.")
    else:
        raise ValueError("Expected a list of keypoints.")

    return processed_keypoints
