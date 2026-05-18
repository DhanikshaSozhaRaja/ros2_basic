**ROS2 Summer Task_01:
Publisher Subscriber Project**

**Description:**
  This project helped me learn various stuffs, starting from basic ubuntu terminal commands to creating and running nodes.
  It demonstrates ROS2 communication using the Publisher-Subscriber model. 
  
  Initially, a ROS2 Workspace was created, containing one C++ package and a Python package.
  Both packages contain publisher(sender) and Subscriber(Reciever) nodes, which are used to send and receive messages using ROS2 topics(Communication channels).
  
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
