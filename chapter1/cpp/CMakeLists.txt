cmake_minimum_required(VERSION 3.5)

project(main)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
link_directories(${OpenCV_LIB_DIR})
set(OpenCV_DIR "/home/chengyingjie666/code/OpencvSrc/opencv/build")


file(GLOB_RECURSE CPP_SOURCES "*.cpp")
add_executable(main ${CPP_SOURCES})

target_link_libraries(main ${OpenCV_LIBS})