# Human Body Pose Tracking using Mediapipe and OpenCV
This project demonstrates real-time human body pose detection and visualization using Mediapipe and OpenCV. The detected pose landmarks are connected with predefined colors for better visualization.

## Features
- Detects human pose landmarks in real-time using a webcam or a video file.
- Visualizes connections between pose landmarks with vibrant colors.
- Displays pose visualization on both the original and a blank frame.

## Prerequisites
### Libraries
Ensure you have the following Python libraries installed:

- OpenCV: For video processing and visualization
    > Install using `pip install opencv-python`
- Mediapipe: For human pose detection
    > Install using `pip install mediapipe`
- NumPy: For array and matrix operations
    > Install using `pip install numpy`

### Hardware
- A functional webcam for real-time detection (or use a video file).
- Moderate CPU/GPU for smooth real-time processing.

## How to Use
1. Clone the Repository
    - Clone the repository or download the source code:
      ```bash
      git clone https://github.com/your_username/human-body-pose-tracking.git
2. Navigate to the Project Directory
   ```bash
   cd human-body-pose-tracking
3. Run the Script
    - Use Python to run the pose tracking script:
      ```bash
      python pose_tracking.py
    - Default Camera: The script uses the default webcam (cv2.VideoCapture(0)).
To use a different camera or a video file, replace 0 in the cv2.VideoCapture line with:
        - 1, 2, ... for additional cameras.
        - A video file path (e.g., `r"path/to/video.mp4"`).
     
## Keyboard Controls
- Press `x`: Exit the application.

## Output
1. Human Body Pose Tracking Window: Displays the original frame with detected pose landmarks and connections.
2. Extracted Video Window: Displays pose landmarks and connections on a blank background.

## Acknowledgments
1. Mediapipe: For the human pose detection module.
2. OpenCV: For video processing and visualization.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
