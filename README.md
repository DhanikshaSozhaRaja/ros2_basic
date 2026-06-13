## What I Learned

This project provided practical experience in using the ROS 2 ecosystem. Starting from a basic robot model, I learned how different components of a robotic system work together to create a complete simulation environment.

Throughout the development process, I gained knowledge in:

- Building robot models using URDF and Xacro
- Defining links, joints, and robot kinematics
- Integrating sensors such as Camera, LiDAR, and IMU
- Simulating robots in Gazebo Fortress (Ignition)
- Visualizing robot states, TF frames, and sensor data in RViz2
- Understanding ROS 2 topics, nodes, publishers, and subscribers
- Configuring and managing controllers using ros2_control
- Implementing differential drive motion control
- Creating launch files for automated robot deployment
- Debugging TF, sensor, controller, and simulation issues
- Working with robot state publishers and joint state broadcasters

I developed a deeper understanding of robot simulation workflows and the tools commonly used in modern robotics development. The project strengthened both my ROS 2 fundamentals and my ability to troubleshoot and integrate multiple robotic subsystems into a functional simulation.

# ROS 2 Mobile Robot Simulation

A custom mobile robot simulation developed using ROS 2 Humble and Gazebo Fortress (Ignition). This project demonstrates robot modeling, sensor integration, robot control, and visualization using modern ROS 2 tools.

## Project Overview

The robot consists of:

- Differential drive mobile base
- Two drive wheels and caster wheels
- Single DOF robotic arm
- RGB Camera
- LiDAR sensor
- IMU sensor
- ROS 2 Control integration
- RViz visualization
- Gazebo simulation environment

The goal of this project was to build a complete simulation stack from scratch, including robot modeling, controllers, sensors, and visualization.

---

## Features

### Mobile Base
- Differential drive locomotion
- Velocity control using ROS 2 topics
- Real-time simulation in Gazebo

### Robotic Arm
- Revolute joint arm mounted on the robot
- Position controlled through ROS 2 controllers

### Sensors
- Camera sensor for image streaming
- 360° LiDAR for environment perception
- IMU for orientation and motion sensing

### Visualization
- Robot model visualization in RViz
- TF tree visualization
- LaserScan display
- Camera image display

### Control Framework
- ros2_control integration
- Controller Manager
- Joint State Broadcaster
- Diff Drive Controller
- Arm Position Controller

---

## Technologies Used

- ROS 2 Humble
- Gazebo Fortress (Ignition Gazebo)
- ros2_control
- gz_ros2_control
- RViz2
- Xacro
- URDF

---

## Project Structure

```text
robot_sim/
│
├── config/
│   └── controllers.yaml
│
├── launch/
│   └── spawn_robot.launch.py
│
├── urdf/
│   ├── robot.urdf.xacro
│   ├── wheels.xacro
│   ├── arm.xacro
│   └── sensors.xacro
│
├── worlds/
│   └── custom_world.sdf
│
├── resource/
│   └── robot_sim
│
├── package.xml
└── setup.py
```

---

## Installation

Clone the repository into your ROS 2 workspace:

```bash
cd ~/robot_ws/src

git clone <repository-url>

cd ..
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## Running the Simulation

Launch Gazebo and spawn the robot:

```bash
ros2 launch robot_sim spawn_robot.launch.py
```

---

## Checking Controllers

List active controllers:

```bash
ros2 control list_controllers
```

Expected controllers:

```text
joint_state_broadcaster
diff_drive_controller
arm_controller
```

---

## Driving the Robot

Move the robot forward:

```bash
ros2 topic pub /diff_drive_controller/cmd_vel_unstamped \
geometry_msgs/msg/Twist \
"{linear:{x:0.3},angular:{z:0.0}}" -r 10
```

Rotate the robot:

```bash
ros2 topic pub /diff_drive_controller/cmd_vel_unstamped \
geometry_msgs/msg/Twist \
"{linear:{x:0.0},angular:{z:0.5}}" -r 10
```

---

## Controlling the Arm

Move the arm joint:

```bash
ros2 topic pub /arm_controller/commands \
std_msgs/msg/Float64MultiArray \
"{data:[0.8]}"
```

---

## Useful ROS 2 Commands

### View Topics

```bash
ros2 topic list
```

### View TF Tree

```bash
ros2 run tf2_tools view_frames
```

### View Joint States

```bash
ros2 topic echo /joint_states
```

### View Hardware Interfaces

```bash
ros2 control list_hardware_interfaces
```

---

## Sensor Topics

| Sensor | Topic |
|----------|---------|
| Camera | `/camera` |
| LiDAR | `/lidar` |
| Point Cloud | `/lidar/points` |
| IMU | `/imu` |
| Joint States | `/joint_states` |

---

## Results

The final simulation successfully demonstrates:

- Mobile robot navigation
- Differential drive control
- Arm actuation
- Camera image generation
- LiDAR scanning
- IMU sensing
- TF tree generation
- ROS 2 controller integration
- RViz visualization

---

## Future Improvements

- Autonomous navigation using Nav2
- SLAM integration
- Object detection using camera feed
- Multi-joint robotic arm
- MoveIt motion planning
- Autonomous obstacle avoidance

---

<img width="1920" height="1080" alt="Screenshot from 2026-06-12 17-59-44" src="https://github.com/user-attachments/assets/0e18b33b-d424-450d-8d10-b72667c85c90" />
<img width="1920" height="1080" alt="Screenshot from 2026-06-13 11-21-13" src="https://github.com/user-attachments/assets/27056d21-5e1a-4572-b650-c158c933bc75" />
<img width="1694" height="387" alt="Screenshot from 2026-06-13 20-12-27" src="https://github.com/user-attachments/assets/690f01e4-76db-4121-8f95-662c1a1e4cb6" />
<img width="1223" height="993" alt="Screenshot from 2026-06-13 20-12-10" src="https://github.com/user-attachments/assets/596876a4-85fa-45f7-84bc-4280a3a62feb" />




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

![RViz Robot]<img width="1920" height="1080" alt="Screenshot from 2026-06-04 19-02-29" src="https://github.com/user-attachments/assets/2951793c-75e2-4208-abe4-9b1cca2072f7" />

---

## Gazebo Simulation

A custom Gazebo world was created using SDF.

The world contains:

* Ground plane

* Gravity and physics

* A cube obstacle

During setup, there were issues loading default Gazebo models such as `ground_plane` and `sun`. To solve this, a custom ground plane was defined directly in the world file.

### Gazebo Screenshot

![Gazebo World]<img width="1920" height="1080" alt="Screenshot from 2026-06-04 18-57-03" src="https://github.com/user-attachments/assets/34098297-6f78-4f94-9c35-922d8f064ca2" />

---

## TF Tree Screenshot

![TF Tree]<img width="1920" height="1080" alt="Screenshot from 2026-06-04 18-37-57" src="https://github.com/user-attachments/assets/f5914e4f-70d5-41a8-a073-382c24d78612" />


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

=======

**ROS2 Summer Task_01:

Publisher Subscriber Project**



**Description:**

  This project helped me learn various stuffs, starting from basic ubuntu terminal commands to creating and running nodes.

  It demonstrates ROS2 communication using the Publisher-Subscriber model. 

  

  Initially, a ROS2 Workspace was created, containing one C++ package and a Python package.

  Both packages contain publisher(sender) and Subscriber(Receiver) nodes, which are used to send and receive messages using ROS2 topics(Communication channels).

  

  I've also learnt about the basic command-line tolls for inspecting sctive nodes, topics, and communication graphs(rqt).


**1. Workspace Creation:**

  Workspace is nothing but a folder to store our project.

  commands used:

  

    1. mkdir                      -> to create directory

    2. cd                         -> to change directory

    3. colcon build               -> to build the workspace

    4. source install/setup.bash  -> to source the workspace

    

**2. Package Creation:**

    It is the funda organizational unit used to bundle and distribute code. we used here for the C++ and Python nodes.

    commands used:

    

      1. ros2 pkg create --build-type ament_cmake cpp_pubsub -- dependencies rclcpp std_msgs   -> for C++

      2. ros2 pkg create --build-type ament_python py_pubsub -- dependencies rclpy std_msgs    -> for Python

      

**3. (i)  C++ / Python Publisher:**

               It continuously publishes(sends) string messages to the topic.

               

   **(ii) C++ / Python Subscriber:**

               It listens to the same topic and displays received messages in the terminal.

               

**4. Build Process:**

    Building the project (compiling and organizing).

    commands used:

    

      1. colcon build

      2. source install/setup.bash

      

**5. Running the nodes:**

    commands used:

    
      1. ros2 run cpp_pubsub publisher

      2. ros2 run cpp_pubsub subscriber

      3. ros2 run py_pubsub publisher

      4. ros2 run py_pubsub subscriber

      

**6. Other CLI commands used:**


    1. ros2 node list            -> to list the nodes active 

    2. ros2 topic list           -> to list the topics active

    3. ros2 topic echo /topic    -> to print real-time messages published (in C++)

    4. ros2 topic echo /topic_py -> to print real-time messages published (in Python)

    5. ros2 topic info /topic    -> to get specific details about the given topic

    6. rqt_graph                 -> to visualize ROS graph

    7. turtlesim commands:

        (i)    source /opt/ros/humble/setup.bash    -> sourcing

        (ii)   ros2 run turtlesim turtlesim_node    -> opens the turtle window

        (iii)  ros2 run turtlesim turtle_teleop_key -> control turtle with arrows and other keyboard keys

        (iv)   ros2 topic echo /turtle1/pose        -> prints live coordinates of the turtle to the terminal



**7. Screenshots:**


C++ rqt graph: 

<img width="1920" height="1080" alt="cpp_cli" src="https://github.com/user-attachments/assets/90d28019-2ef6-46b7-88ad-3958fa9dfc46" />

<img width="762" height="72" alt="ros_cpp" src="https://github.com/user-attachments/assets/0b33ad32-cbda-4332-ba67-82c12a2d6f4b" />



Python rqt graph:

<img width="1920" height="1080" alt="py_cli" src="https://github.com/user-attachments/assets/fc8b1596-9b99-4750-905d-da58be1029c4" />

<img width="768" height="72" alt="rosgraph_py" src="https://github.com/user-attachments/assets/081e2f58-5792-42af-8859-6cb003624c1a" />



turtlesim:

<img width="1920" height="1080" alt="turtle" src="https://github.com/user-attachments/assets/92698da3-1783-436d-9128-4ce01c6cce66" />

<img width="1138" height="181" alt="rosgraph_turtle" src="https://github.com/user-attachments/assets/eb816335-52f8-4c10-844e-2ab822b0b3b0" />



Extras(Service and Client):

<img width="1920" height="1080" alt="sercli" src="https://github.com/user-attachments/assets/c665a6a8-b12f-4bac-b92b-7c90ac41a274" />



**8. Extras:**



    1. Service and Client:

      A service is basically like a server. It is used when one node wants another node to do a specific task and send back a response.

      A client node sends the request to the service.



      work flow:

        1. Client  -> sends req

        2. Service -> processes the req and sends response

        3. Client  -> receives result



    2. Parameters:

      These are the values stored inside a node to control its behaviour.

      Eg.: Speed of the robot, name of the topic or the robot itself, and resolution of the camera.



    3. Actions:

      There are used for long-running tasks. They send feedback while running. 

      Eg: Path planning, moving robot arm, and navigation.



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Task-02:



### 1. Custom Actions:



Actions are used for long-running tasks where continuous feedback is needed.



In this project:




- A custom action `ExecuteCircle.action` was created

- Goal, Feedback, and Result were defined

- Action Server and Client were implemented from scratch


---

## Conclusion

This project provided an introduction to robot modelling and simulation in ROS 2. Starting from a simple robot description, I was able to visualize the robot in RViz2, verify its TF structure, and create a simulation environment in Gazebo.


=======

### 2. Circular Turtle Patrol:

The turtle moves autonomously in a circular path using velocity commands.

Formula used:

```

w = v / r

```
where:

```

v -> linear velocity

w -> angular velocity

r -> radius

```

---

### 3. Feedback Handling:



The Action Server continuously sends:



```

- distance travelled

- current mission status

```



to the Action Client while the turtle is moving.



---



### 4. Boundary Collision Detection:



The turtle position is continuously monitored.



If the turtle approaches walls:



```

- mission gets aborted

- turtle stops immediately

- abort message is returned to client

```



---



### 5. CLI Commands Used:


```

1. ros2 action list

   -> lists active actions



2. ros2 interface show turtle_patrol/action/ExecuteCircle

   -> shows custom action structure



3. ros2 topic echo /turtle1/pose

   -> prints live turtle coordinates



4. rqt_graph

   -> visualizes ROS2 communication graph
```

Part 2: Deep Dive into the Communication Layer



A. ROS 1 vs ROS 2 Architectural Shift



1. ROS 1 Master and SPOF

ROS 1 uses a centralized component called the ROS Master ("roscore").

It manages node registration, topic information, and node discovery.



Steps:

1. Nodes register with "roscore"

2. Nodes get connection details from the Master

3. Nodes communicate directly


Problem

The ROS Master is a Single Point of Failure (SPOF):

```
- If "roscore" crashes, new nodes cannot communicate.

- Discovery stops and the system becomes unstable.

```

---



2. Decentralized Architecture in ROS 2



ROS 2 removes the ROS Master and uses DDS (Data Distribution Service).



In ROS 2:

```

- Nodes automatically discover each other

- Communication is peer-to-peer

- No centralized broker is needed
```


Advantages


```
- Better reliability

- No single point of failure

- Improved scalability

- Suitable for real-time and multi-robot systems

```

---



3. ROS 1 vs ROS 2 Communication



ROS 1

Uses:

```

- TCPROS → reliable but slower

- UDPROS → faster but less reliable


```
Nodes first contact the ROS Master before communicating.


ROS 2

Uses:
```

- DDS Wire Protocol (RTPS)

```

Features:


```
- Automatic discovery

- Direct peer-to-peer communication

- QoS support

- Better real-time performance

```

---



B. DDS (Data Distribution Service)

DDS is the middleware used by ROS 2 for communication between nodes.

---

1. Discoverability Mechanism

ROS 2 nodes on the same Wi-Fi network discover each other automatically using:


```
- Simple Discovery Protocol (SDP)

- Multicast UDP

```

Process

```

1. A node joins the network

2. It sends multicast discovery messages

3. Other nodes detect it

4. Direct communication starts

```

No central server is required.

---



2. DDS Vendors

```

DDS Vendor| Middleware Package

eProsima Fast DDS| "rmw_fastrtps_cpp"

Eclipse Cyclone DDS| "rmw_cyclonedds_cpp"

RTI Connext DDS| "rmw_connextdds"



Environment Variable

Used to switch DDS vendors:

RMW_IMPLEMENTATION

Example:

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

```

------------------------------------------





**Conclusion:**

    This task really provided me the practical exposure to ROS2 humble fundas, specifically nodes, topics, package, workspace, and graphs.

    It also improved my understanding with GitHub control and documentation.


