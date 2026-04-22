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
```




🛠️ Installation & Setup
1. Prerequisites
OS: Ubuntu 22.04 (ROS 2 Humble)
Python packages:
```bash
pip install ultralytics opencv-python
```
2. Workspace Setup

Clone the repository into your ROS 2 workspace:
```bash
cd ~/ros2_ws/src
git clone https://github.com/MahmmudQatmh/FastGate-Tello-YOLO.git
```
3. Install Tello Driver

This project depends on the TIERS Tello ROS 2 Driver:
```bash
sudo apt install libh264-decoder-dev
```
```bash
cd ~/ros2_ws
colcon build --packages-select tello_msg tello_driver my_tello_vision
```
source install/setup.bash


🚀 Running the Mission

⚠️ Open a new terminal for each step

Step 1: Connect to Drone Wi-Fi
Power on the DJI Tello
Connect your PC to the drone’s Wi-Fi network

Step 2: Launch the Driver
```bash
ros2 launch tello_driver tello_driver_launch.py
```
Step 3: Start the Mission Recorder (Optional)
```bash
ros2 run my_tello_vision record_tello
```
Step 4: Execute Autonomous Flight
```bash
ros2 run my_tello_vision tello_vision_control


```
## 🧠 Navigation Logic

### Finite State Machine (FSM)

The drone operates on a 6-state logic system to ensure robust flight:

    1. **SEARCH**: 360° scan for the gate. Includes "Blind Maneuvering" for difficult angles.

    2. **ALIGN**: PID control centers the drone on the target while managing camera/tilt offsets.

    3. **PENETRATE**: An aggressive forward burst to clear the gate area quickly.

    4. **BRAKE**: Immediate backward thrust to stabilize before the next search.

    5. **LAND**: Precision approach triggered upon detecting the Stop Sign.

    6. **RECOVERY**: Failsafe state to maintain last known trajectory if target is lost.

### PID Tuning & Correction

    1. **Camera Offset**: Compensates for the Tello's non-centered lens.

    2. **Tilt Compensation**: Dynamically adjusts the target "center" based on forward velocity (fvel​).

    3. **Aggressive Search**: Hard-coded 60-80° rotations after specific gates to minimize search time.


## 📊 Model Performance

Real-time detection performance of the YOLOv8 model:

| Class      | Accuracy (%) | Inference Time (ms) |
|:-----------|:------------:|:-------------------:|
| Gate       | 99.4         | 7                   |
| Stop Sign  | 99.0         | 7                   |







https://github.com/user-attachments/assets/1d728bf9-6e44-4a3b-89b3-14ebaf8c18ff



