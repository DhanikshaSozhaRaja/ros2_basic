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

        

**Conclusion:**
    This task really provided me the practical exposure to ROS2 humble fundas, specifically nodes, topics, package, workspace, and graphs.
    It also improved my understanding with GitHub control and documentation.
