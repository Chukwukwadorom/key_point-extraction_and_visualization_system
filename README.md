# Keypoint Extractor App

This is a Flask-based application that performs keypoint extraction and visualization from images. It provides API to accept an image and keypoints and return the keypoint visualization as a downloadable file or an image URL.

## Features

- **Keypoint Extraction**: The app processes images to detect body keypoints (such as head, shoulders, elbows, knees) using a pose estimation model.
- **Visualization**: The detected keypoints are drawn onto a blank canvas and returned as an image.
- **RESTful API**: The app exposes a simple API for interacting with the keypoint extraction and visualization functionalities.

## Requirements

- Docker
- Python 3.x
- Mediapipe
- Opencv-Python

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

    The application will now be running on `http://localhost:5000`.

### Option 2: Running with Python


If you'd like to run the application directly without using Docker, follow these steps:

### 1. Set Up a Virtual Environment
It's recommended to create and activate a virtual environment to isolate dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:
    ```bash
    python app.py
    ```

    The application will be available at `http://localhost:5000`.

## API Endpoints

### POST /keypoints
- **Description**: Extracts keypoints from an image and returns the visualization.
- **Request**: Send a POST request with the image file in the form-data.
    - Example request:
      ```bash
      curl -X POST -F "image=@path_to_image.jpg" http://localhost:5000/process-image
      ```
    alternatively if you have landmarks you can pass them as json data like so:
  Example request:
      ```bash
      curl -X POST "http://127.0.0.1:5000/process-landmarks" -H "Content-Type: application/json" -d '{"landmarks":[{"x":0.5,"y":0.5},{"x":0.4,"y":0.6},{"x":0.45,"y":0.55}]} ' --output downloaded_image.jpg


*Response**: The API will return a downloadable image containing the keypoints and skeletal drawing in the directory from which you made the call.
    - Example response:
      ```bash
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
      100 15746  100 15701  100    45   326k    957 --:--:-- --:--:-- --:--:--  327k
      ```


## Dockerize the App

If you want to deploy the app with Docker, follow the steps under the "Installation and Setup" section above to build and run the Docker container.
