cmake_minimum_required(VERSION 3.5)
option(NEYNXX_BUILD_LIB "Build Neyn C++ Library" OFF)
add_subdirectory(neynxx)

project(Neynpy VERSION ${NEYNXX_VERSION} LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

file(GLOB SOURCES
    "${NEYN_INCLUDE_DIR}/neyn/*.c"
    "${NEYNXX_INCLUDE_DIR}/neynxx/*.cpp")
configure_file("neynxx/neynxx/config.h.in" "config.h")

add_subdirectory(pybind11)
pybind11_add_module(neynpy ${SOURCES} bind/main.cpp)
target_link_libraries(neynpy PUBLIC pthread)
target_include_directories(neynpy PUBLIC
    ${NEYN_INCLUDE_DIR}
    ${NEYNXX_INCLUDE_DIR}
    ${PROJECT_BINARY_DIR})
