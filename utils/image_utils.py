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
