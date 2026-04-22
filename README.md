🛸 FastGate: Autonomous Tello Navigation

Aerial Robotics & Multi-Robot Systems | Spring 2026

An autonomous mission utilizing a DJI Tello drone and YOLOv8 to navigate a 4-gate course with a precision landing on a stop sign.

    [!IMPORTANT]
    Performance: Achieved a best time of 45 seconds (Target: <50s).
    Detection: Inference speed of 7ms (~140 FPS) with 99% accuracy.

📺 Mission Demo



https://github.com/user-attachments/assets/7d2087d7-d7cd-4d46-8dbb-fb4713091db5



## 📁 Project Structure
```text
my_tello_vision/
├── launch/             # ROS 2 Launch files
├── models/             # YOLOv8 weights (best.pt)
├── my_tello_vision/    # Core Python Logic (FSM & PID)
├── simulation/         # Gazebo .world and models
├── Media/              # Flight recordings & demos
├── package.xml         # Package metadata
└── setup.py            # Entry points and dependencies

🛠️ Installation & Setup
1. Prerequisites

    Ubuntu 22.04 with ROS 2 Humble installed.

    Python Dependencies:

Bash

pip install ultralytics opencv-python

2. Workspace Setup

Clone this repository into your ros2_ws/src folder. This repository includes the necessary driver directly for a seamless build.
Bash

cd ~/ros2_ws/src
git clone https://github.com/MahmmudQatmh/FastGate-Tello-YOLO.git .

3. Install the Tello Driver

This project relies on the TIERS Tello ROS 2 Driver. Ensure all driver dependencies are met:
Bash

sudo apt install libh264-decoder-dev
cd ~/ros2_ws
colcon build --packages-select tello_msg tello_driver my_tello_vision
source install/setup.bash

🚀 Running the Mission

Follow these steps in order (each in a new terminal):

Step 1: Connect to Drone Wi-Fi Power on the DJI Tello and connect your Alienware to the drone's Wi-Fi access point.

Step 2: Launch the Driver
Bash

ros2 launch tello_driver tello_driver_launch.py

Step 3: Start the Mission Recorder (Optional)
Bash

ros2 run my_tello_vision record_tello

Step 4: Execute Autonomous Flight
Bash

ros2 run my_tello_vision tello_vision_control

🧠 Navigation Logic
Finite State Machine (FSM)

The drone operates on a 6-state logic system to ensure robust flight:

    SEARCH: 360° scan for the gate. Includes "Blind Maneuvering" for difficult angles.

    ALIGN: PID control centers the drone on the target while managing camera/tilt offsets.

    PENETRATE: An aggressive forward burst to clear the gate area quickly.

    BRAKE: Immediate backward thrust to stabilize before the next search.

    LAND: Precision approach triggered upon detecting the Stop Sign.

    RECOVERY: Failsafe state to maintain last known trajectory if target is lost.

PID Tuning & Correction

    Camera Offset: Compensates for the Tello's non-centered lens.

    Tilt Compensation: Dynamically adjusts the target "center" based on forward velocity (fvel​).

    Aggressive Search: Hard-coded 60-80° rotations after specific gates to minimize search time.

📊 Model Performance
Class	Accuracy	Inference Speed
Gate	99.4%	7ms
Stop Sign	99.0%	7ms
