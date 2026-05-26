cmake_minimum_required(VERSION 3.8)
project(turtle_patrol)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/ExecuteCircle.action"
)


install(PROGRAMS
  turtle_patrol/circle_patrol_server.py
  turtle_patrol/circle_patrol_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()

