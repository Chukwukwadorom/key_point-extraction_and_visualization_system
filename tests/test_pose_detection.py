from utils.pose_detection import PoseDetection
from utils.image_utils import load_image
import pytest

def test_pose_detection():
    pose_model = PoseDetection()
    img = pose_model.get_pose("static/raw_images/pose1.jpeg")
    assert img is not None
    assert img.shape[-1] == 3  # Ensuring it's a color image

def test_get_positions():
    pose_model = PoseDetection()
    img = load_image("static/raw_images/pose1.jpeg")
    pose_model.get_pose("static/raw_images/pose1.jpeg")
    positions = pose_model.get_positions(img)
    assert isinstance(positions, list)
    assert len(positions) > 0
