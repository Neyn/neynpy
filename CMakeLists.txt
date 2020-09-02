cmake_minimum_required(VERSION 3.5)
option(NEYN_BUILD_LIB "Build Neyn C++ Library" OFF)
add_subdirectory(src/neynxx)

project(Neynpy VERSION ${NEYN_VERSION} LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB SOURCES
    "src/neynxx/cneyn/src/cneyn/*.c"
    "src/neynxx/src/neyn/*.cpp")

add_subdirectory(src/pybind11)
pybind11_add_module(impl ${SOURCES} src/bind/main.cpp)
target_link_libraries(impl PUBLIC pthread)
target_include_directories(impl PUBLIC
    "${CNEYN_INCLUDE_DIR}"
    "${NEYN_INCLUDE_DIR}")
