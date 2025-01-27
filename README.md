# Keypoint Extractor App

This is a Flask-based application that performs keypoint extraction and visualization from images. It provides an API to accept an image or keypoints and return the keypoint visualization as a downloadable file or an image URL.

## Features

- **Keypoint Extraction**: Processes images to detect body keypoints (such as head, shoulders, elbows, and knees) using a pose estimation model.
- **Visualization**: Draws the detected keypoints onto a blank canvas and returns the result as an image.
- **RESTful API**: Exposes endpoints for interacting with the keypoint extraction and visualization functionalities.

## Requirements

- Docker
- Python 3.x
- Mediapipe
- OpenCV-Python

## Installation and Setup

### Option 1: Dockerize the Application (Recommended)

1. Clone the repository:
    ```bash
    git clone https://github.com/Chukwukwadorom/key_point-extraction_and_visualization_system.git
    cd key_point-extraction_and_visualization_system
    ```

2. Build the Docker image:
    ```bash
    docker build -t keypoint-extractor-app .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 5000:5000 keypoint-extractor-app
    ```

    The application will now be running at `http://localhost:5000`.

### Option 2: Run Locally with Python

1. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

    The application will be available at `http://localhost:5000`.

## API Endpoints

### POST `/keypoints`

- **Description**: Extracts keypoints from an image or processes existing landmarks and returns the visualization.
- **Request**: 
    - To process an image:
      ```bash
      curl -X POST -F "image=@path_to_image.jpg" http://localhost:5000/process-image
      ```
    - To process landmarks directly:
      ```bash
      curl -X POST "http://localhost:5000/process-landmarks" \
      -H "Content-Type: application/json" \
      -d '{"landmarks":[{"x":0.5,"y":0.5},{"x":0.4,"y":0.6},{"x":0.45,"y":0.55}]}' \
      --output downloaded_image.jpg
      ```

- **Response**: Returns a downloadable image containing the keypoints and skeletal drawing. Example:
    ```
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
      100 15746  100 15701  100    45   326k    957 --:--:-- --:--:-- --:--:--  327k
    ```

## Docker Deployment

To deploy the app with Docker, follow the steps in the **"Option 1: Dockerize the Application"** section above.
