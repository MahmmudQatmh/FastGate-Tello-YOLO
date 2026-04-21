🛸 Autonomous Aerial Robot: YOLO-Powered Gate Navigation

An elite, high-speed autonomous drone mission. The system uses a DJI Tello drone controlled via ROS 2 Humble, utilizing a custom-trained YOLO model for object detection and a refined Finite State Machine (FSM) with PID control for navigation.

Performance Goal: Complete a 4-gate course and precision landing in under 50 seconds.

Final Best Time: 45 Seconds.
🛠 Hardware: The DJI Tello

The project utilizes the DJI Tello, a small, lightweight beginner-friendly mini-drone designed for learning to fly and programming.
Specifications & Features

    Developer: Developed by Ryze Tech, powered by DJI.

    Safety: Equipped with detachable propeller guards and specific marked/unmarked propellers to ensure correct motor rotation.

    Connectivity: Connects via a phone or computer to the drone's built-in Wi-Fi.

🏗 The Bridge: TIERS Tello ROS 2 Driver

A critical component of this project is the TIERS Tello ROS 2 Humble Driver.
Why this driver is essential:

    Protocol Translation: The driver acts as a bridge between the ROS 2 ecosystem and the Tello's official SDK.

    Seamless Control: It allows us to use standard ROS 2 messages (geometry_msgs/Twist) to control the drone's flight instead of manual joystick inputs.

    Real-Time Data: It handles the high-speed telemetry and video stream required for our YOLO model to process images at 140 FPS.

📸 Phase 1: Data Collection & Model Training

To build the "brain" of the drone, we first had to teach it what a gate and a stop sign look like.

1. Image Acquisition (save_images.py)

We used a custom Python script to stream the Tello's live feed and save frames every 10th iteration. This ensured a diverse dataset of over 400 images captured from various angles and lighting conditions.

2. Manual Labeling

Images were hand-labeled using Roboflow. Each frame was meticulously annotated to distinguish between "Gate" and "Stop Sign" classes.

3. The "Report Card" (YOLO Model Results)

We trained a YOLO (You Only Look Once) model to achieve ultra-low latency and high accuracy:

    Accuracy: 99.4% for Gates; 99.0% for Stop Signs.

    Inference Speed: 7 milliseconds (140 FPS).

    Performance: Significantly faster than human reaction time (30-60 FPS).

🧠 Phase 2: Control Logic & Challenges

The drone doesn't just "see"; it must "act." We implemented a PID Controller within an FSM.

Technical Challenges Overcome:

    Camera Offset: The Tello camera is not perfectly centered. We implemented a dynamic horizontal and vertical offset to align the drone's true center with the visual center.

    Tilt Angle Correction: At higher forward velocities, the drone tilts forward, shifting the camera's view. We calculated tilt as a function of velocity (f_vel) to adjust the target center point dynamically.

    PID Tuning (Kp​, Kd​):

        Kp​: High values for fast correction without induced oscillation.

        Kd​: "The Brakes"—tuned to prevent overshooting the center of the gate.

    Search Optimization: To save time, we "locked" the search area. Since the next gate was consistently to the right, we programmed a forced 60-80° right rotation immediately after crossing a gate.

The Finite State Machine (FSM)

    State 0 (SEARCH): Rotate and scan for the target. Includes "Blind Maneuvering" logic for Gate 3.

    State 1 (ALIGN): Use PID to center the drone on the gate/sign while moving forward.

    State 2 (PENETRATE): "The Punch"—aggressive forward burst to clear the gate.

    State 3 (BRAKE & COUNT): Brief backward thrust to stabilize and increment the gate counter.

    State 4 (LAND): Final precision approach and landing on the Stop Sign.

    State 5 (RECOVERY): Memory mode to stay on course if a target is briefly lost.

💻 Core Codebase

High-Precision FSM Controller (tello_vision_control.py)

This is the "Pilot." It manages the PID updates and state transitions to navigate the gates with aggressive efficiency.
Visual Flight Recorder (record_tello.py)

To document our success, we developed a recording script that captures the drone's-eye view with the YOLO bounding boxes overlaid.

Key Features:

    QoS Matching: Uses BEST_EFFORT reliability to match the Tello driver's stream.

    OpenCV Integration: Saves the annotated frames into an MP4 file with a unique timestamp.

    Visual Proof: Captures exactly what the AI sees during its 45-second run.

🚀 How to Run

    Start the Driver: ros2 launch tello_driver tello_driver_launch.py

    Start Recording: ros2 run my_tello_vision record_tello

    Initiate Mission: ros2 run my_tello_vision tello_vision_control


Developed for the Aerial Robotics and Multi-Robot Systems Course, Spring 2026.






