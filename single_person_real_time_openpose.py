import cv2  # Importing OpenCV for image and video processing
import mediapipe as mp  # Importing Mediapipe for human pose detection
import numpy as np  # Importing NumPy for array and matrix operations

# Initialize Mediapipe Pose module
mp_pose = mp.solutions.pose  # Access Mediapipe's pose detection module
pose = mp_pose.Pose()  # Create a pose detection object

# Define predefined colors for pose connections
CONNECTION_COLORS = [
    (0, 0, 255),  # Red
    (0, 165, 255),  # Orange
    (0, 255, 255),  # Yellow
    (0, 255, 0),  # Green
    (255, 0, 0),  # Blue
    (75, 0, 130),  # Indigo
    (238, 130, 238)  # Violet
]

# Open a video file (replace with 0 to use the default camera, 1 for additional camera, or path video file (r"Your_PATH"))
cap = cv2.VideoCapture(0)

# Continuously read frames from the video
while True:
    ret, img = cap.read()  # Read the next frame from the video stream
    if not ret:  # If no frame is returned, end the loop (video has ended)
        break

    # Resize the frame to a fixed size (600x400 pixels) for consistent processing
    img_resized = cv2.resize(img, (600, 400))

    # Create a blank image for "Extracted Video" window
    h, w, c = img_resized.shape  # Get dimensions of the resized frame
    opImg = np.zeros([h, w, c], dtype=np.uint8)  # Initialize a blank black image

    # Process the resized frame to detect human pose landmarks
    result = pose.process(img_resized)

    if result.pose_landmarks:  # Check if pose landmarks are detected
        # Draw each connection with different colors on both frames
        for i, connection in enumerate(mp_pose.POSE_CONNECTIONS):
            start_idx, end_idx = connection  # Get the indices of start and end landmarks
            start_landmark = result.pose_landmarks.landmark[start_idx]
            end_landmark = result.pose_landmarks.landmark[end_idx]

            # Convert normalized coordinates to pixel coordinates
            start_point = (int(start_landmark.x * w), int(start_landmark.y * h))
            end_point = (int(end_landmark.x * w), int(end_landmark.y * h))

            # Select a color from the CONNECTION_COLORS list based on the connection index
            color = CONNECTION_COLORS[i % len(CONNECTION_COLORS)]

            # Draw the connection line
            cv2.line(img_resized, start_point, end_point, color, 2)  # On original frame
            cv2.line(opImg, start_point, end_point, color, 2)  # On blank frame

            # Draw the connected joints with the same color
            cv2.circle(img_resized, start_point, 5, color, -1)  # Start joint
            cv2.circle(img_resized, end_point, 5, color, -1)  # End joint

            cv2.circle(opImg, start_point, 5, color, -1)  # Start joint on blank frame
            cv2.circle(opImg, end_point, 5, color, -1)  # End joint on blank frame

    # Display the original frame with pose landmarks in a window named "Human Body Pose Tracking"
    cv2.imshow("Human Body Pose Tracking", img_resized)

    # Display the blank frame with pose landmarks in a window named "Extracted Video"
    cv2.imshow("Extracted Video", opImg)

    # Check if the 'x' key is pressed; if yes, exit the loop
    if cv2.waitKey(30) & 0xFF == ord('x'):
        break

# Release the video capture resource to free up memory
cap.release()
# Close all OpenCV windows that were opened
cv2.destroyAllWindows()
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------