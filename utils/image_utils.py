import cv2

def load_image(img_path:str):
    """Utility to load an image and validate it."""
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Image at {img_path} could not be loaded.")
    return img

def save_image(img, filename="static/processed_images/processed_image.jpg"):
    """Save the processed image."""
    cv2.imwrite(filename, img)
    return filename

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
