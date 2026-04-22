# 🛸 FastGate: Autonomous Tello Navigation
**Aerial Robotics & Multi-Robot Systems | Spring 2026**

An autonomous mission utilizing a **DJI Tello** drone and **YOLOv8** to navigate a 4-gate course with a precision landing.

---

## 🎥 Demo
https://github.com/user-attachments/assets/7d2087d7-d7cd-4d46-8dbb-fb4713091db5

---

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
OS: Ubuntu 22.04 (ROS 2 Humble)
Python packages:
```bash
pip install ultralytics opencv-python

2. Workspace Setup

Clone the repository into your ROS 2 workspace:
```bash
cd ~/ros2_ws/src
git clone https://github.com/MahmmudQatmh/FastGate-Tello-YOLO.git

3. Install Tello Driver

This project depends on the TIERS Tello ROS 2 Driver:
```bash
sudo apt install libh264-decoder-dev
```bash
cd ~/ros2_ws
colcon build --packages-select tello_msg tello_driver my_tello_vision

source install/setup.bash


🚀 Running the Mission

⚠️ Open a new terminal for each step

Step 1: Connect to Drone Wi-Fi
Power on the DJI Tello
Connect your PC to the drone’s Wi-Fi network

Step 2: Launch the Driver
```bash
ros2 launch tello_driver tello_driver_launch.py

Step 3: Start the Mission Recorder (Optional)
```bash
ros2 run my_tello_vision record_tello

Step 4: Execute Autonomous Flight
```bash
ros2 run my_tello_vision tello_vision_control

🧠 Navigation Logic
Finite State Machine (FSM)

The drone operates using a 6-state control architecture:

SEARCH
360° scan for the gate, including blind maneuvers for difficult angles
ALIGN
PID controller centers the drone relative to the detected gate
PENETRATE
Aggressive forward motion to pass through the gate
BRAKE
Immediate backward correction to stabilize
LAND
Precision landing triggered by stop sign detection
RECOVERY
Failsafe mode when the target is lost
PID Tuning & Corrections
Camera Offset Compensation
Adjusts for non-centered Tello camera
Tilt Compensation
Dynamically shifts target center based on forward velocity
Aggressive Search Strategy
Predefined 60–80° rotations to reduce search time


📊 Model Performance
Class	Accuracy	Inference Speed
Gate	99.4%	7 ms
Stop Sign	99.0%	7 ms
