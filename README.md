# Robot Simulation using ROS 2, RViz2 and Gazebo

## Project Overview

In this task, I created a simple robot using URDF/Xacro in ROS 2. The robot consists of a rectangular chassis and two wheels connected using joints. The robot was visualized in RViz2, its TF tree was verified, and a custom Gazebo world was created for simulation.

The main goal of this exercise was to understand how robot models are created, how TF frames are connected, and how simulations are set up in Gazebo.

---

## Robot Design

The robot was created using Xacro.

### Components

* Rectangular chassis (`base_link`)
* Left wheel (`left_wheel`)
* Right wheel (`right_wheel`)
* Continuous joints connecting the wheels to the chassis

Using Xacro properties made it easier to modify dimensions without changing multiple places in the file.

---

## TF Tree

The robot's TF tree consists of:

```text
base_link
├── left_wheel
└── right_wheel
```

The TF tree was generated using:

```bash
ros2 run tf2_tools view_frames
```

This helped verify that all links and joints were connected correctly.

---

## RViz2 Visualization

The robot was visualized in RViz2 using:

* robot_state_publisher
* joint_state_publisher_gui
* RobotModel display
* TF display

Initially the robot was not visible because of Xacro processing and frame configuration issues. After fixing the launch file and setting the correct fixed frame, the robot was displayed successfully.

### RViz Screenshot

![RViz Robot](images/rviz_robot.png)

---

## Gazebo Simulation

A custom Gazebo world was created using SDF.

The world contains:

* Ground plane
* Gravity and physics
* A cube obstacle

During setup, there were issues loading default Gazebo models such as `ground_plane` and `sun`. To solve this, a custom ground plane was defined directly in the world file.

### Gazebo Screenshot

![Gazebo World](images/gazebo_world.png)

---

## TF Tree Screenshot

![TF Tree](images/tf_tree.png)

---

## Challenges Faced

Some issues encountered during development were:

* Syntax errors in `setup.py`
* Xacro variables not expanding correctly
* Robot not appearing in RViz
* Fixed frame errors (`map` frame not found)
* Gazebo model URI errors
* Launch file installation issues

These problems were resolved by checking ROS topics, TF frames, launch files, and package installation paths.

---

## What I Learned

Through this task I learned:

* Basic URDF and Xacro modelling
* Difference between links and joints
* Importance of TF trees in robotics
* Using RViz2 for visualization
* Creating custom Gazebo worlds
* Organizing a ROS 2 simulation package

---

## Commands Used

Build workspace:

```bash
colcon build
source install/setup.bash
```

Launch RViz:

```bash
ros2 launch robot_simulation display.launch.py
```

Generate TF tree:

```bash
ros2 run tf2_tools view_frames
```

Launch Gazebo world:

```bash
ign gazebo worlds/custom_world.sdf
```

---

## Conclusion

This project provided an introduction to robot modelling and simulation in ROS 2. Starting from a simple robot description, I was able to visualize the robot in RViz2, verify its TF structure, and create a simulation environment in Gazebo.

