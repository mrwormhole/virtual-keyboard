cmake_minimum_required(VERSION 3.27.0)
project(virtual-keyboard C)

set(CMAKE_C_STANDARD 17)

# Find and include GTK3
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

# Add the GTK3 include directories to the project
include_directories(${GTK3_INCLUDE_DIRS})

# Create the executable from the source file and link against GTK3
add_executable(virtual-keyboard keyboard.c)

# Link against GTK3 libraries
target_link_libraries(virtual-keyboard PRIVATE ${GTK3_LIBRARIES})
