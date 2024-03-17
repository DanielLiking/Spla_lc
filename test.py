# Import the necessary packages
import cv2
import pyorbslam

# Load video and create 3D path drawer
cap = cv2.VideoCapture("video/path/here", 0)
drawer = pyorbslam.TrajectoryDrawer()

# Timestamp information
timestamp = 0
fps = 1/24

# Create SLAM
slam = pyorbslam.MonoSLAM("./settings/OrbSlam3_TUM_freiburg3.yaml") # Examples found in ``settings`` folder

# Main loop
while True:

    # Read
    ret, frame = cap.read()
    if not ret:
        break

    # Process frame and update timestamp
    state = slam.process(frame, timestamp)
    timestamp += fps

    # If all things work, then we get a camera pose (YAY!)
    if state == pyorbslam.State.OK:
        pose = slam.get_pose_to_target()
        drawer.plot_trajectory(pose)

    # Show the image
    cv2.imshow('frame', frame)
    cv2.waitKey(1)