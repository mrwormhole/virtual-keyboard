cmake_minimum_required(VERSION 3.27.0)
project(virtual-keyboard C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_FLAGS_WARNINGS "-Wall -Wextra -Wpedantic -Werror")
set(SOURCE_FILES keyboard.c)
set(COMPILE_OPTIONS -Wall -Wextra -Wpedantic -Werror)

# Add compiler options
add_compile_options(${COMPILE_OPTIONS})

# Find and include GTK3
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

# Add the GTK3 include directories to the project
include_directories(${GTK3_INCLUDE_DIRS})

# Create the executable from the source file and link against GTK3
add_executable(virtual-keyboard ${SOURCE_FILES})

# Set compiler flags for the specific target
# target_compile_options(virtual-keyboard PRIVATE ${COMPILE_OPTIONS})

# Link against GTK3 libraries
target_link_libraries(virtual-keyboard PRIVATE ${GTK3_LIBRARIES})
