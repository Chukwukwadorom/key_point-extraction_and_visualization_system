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

def preprocess_keypoints(landmarks):
    """
    Convert a list of landmark dictionaries into pairs of (x, y) tuples.
    """
    pairs = [(landmark["x"], landmark["y"]) for landmark in landmarks]
    return pairs

