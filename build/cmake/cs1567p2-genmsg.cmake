# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "cs1567p2: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ics1567p2:/home/PITT/bcy3/cs1567_ws/src/msg;-Igeometry_msgs:/opt/ros/hydro/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/hydro/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/hydro/share/sensor_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(cs1567p2_generate_messages ALL)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(cs1567p2
  "/home/PITT/bcy3/cs1567_ws/src/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs1567p2
)
_generate_msg_cpp(cs1567p2
  "/home/PITT/bcy3/cs1567_ws/src/msg/LocationList.msg"
  "${MSG_I_FLAGS}"
  "/home/PITT/bcy3/cs1567_ws/src/msg/Location.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs1567p2
)

### Generating Services

### Generating Module File
_generate_module_cpp(cs1567p2
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs1567p2
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(cs1567p2_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(cs1567p2_generate_messages cs1567p2_generate_messages_cpp)

# target for backward compatibility
add_custom_target(cs1567p2_gencpp)
add_dependencies(cs1567p2_gencpp cs1567p2_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs1567p2_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(cs1567p2
  "/home/PITT/bcy3/cs1567_ws/src/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs1567p2
)
_generate_msg_lisp(cs1567p2
  "/home/PITT/bcy3/cs1567_ws/src/msg/LocationList.msg"
  "${MSG_I_FLAGS}"
  "/home/PITT/bcy3/cs1567_ws/src/msg/Location.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs1567p2
)

### Generating Services

### Generating Module File
_generate_module_lisp(cs1567p2
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs1567p2
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(cs1567p2_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(cs1567p2_generate_messages cs1567p2_generate_messages_lisp)

# target for backward compatibility
add_custom_target(cs1567p2_genlisp)
add_dependencies(cs1567p2_genlisp cs1567p2_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs1567p2_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(cs1567p2
  "/home/PITT/bcy3/cs1567_ws/src/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs1567p2
)
_generate_msg_py(cs1567p2
  "/home/PITT/bcy3/cs1567_ws/src/msg/LocationList.msg"
  "${MSG_I_FLAGS}"
  "/home/PITT/bcy3/cs1567_ws/src/msg/Location.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs1567p2
)

### Generating Services

### Generating Module File
_generate_module_py(cs1567p2
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs1567p2
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(cs1567p2_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(cs1567p2_generate_messages cs1567p2_generate_messages_py)

# target for backward compatibility
add_custom_target(cs1567p2_genpy)
add_dependencies(cs1567p2_genpy cs1567p2_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cs1567p2_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs1567p2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cs1567p2
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(cs1567p2_generate_messages_cpp geometry_msgs_generate_messages_cpp)
add_dependencies(cs1567p2_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(cs1567p2_generate_messages_cpp sensor_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs1567p2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cs1567p2
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(cs1567p2_generate_messages_lisp geometry_msgs_generate_messages_lisp)
add_dependencies(cs1567p2_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(cs1567p2_generate_messages_lisp sensor_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs1567p2)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs1567p2\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cs1567p2
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(cs1567p2_generate_messages_py geometry_msgs_generate_messages_py)
add_dependencies(cs1567p2_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(cs1567p2_generate_messages_py sensor_msgs_generate_messages_py)
