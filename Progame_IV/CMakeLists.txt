# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)

# == DO NOT EDIT THE FOLLOWING LINES for the Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.3.1)
set(toolchainVersion 15_2_Rel1)
set(picotoolVersion 2.3.1)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if (EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
set(PICO_BOARD pico CACHE STRING "Board type")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

project(Progame_IV C CXX ASM)

# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1

add_executable(Progame_IV Progame_IV.c )

pico_set_program_name(Progame_IV "Progame_IV")
pico_set_program_version(Progame_IV "0.1")

# Modify the below lines to enable/disable output over UART/USB
pico_enable_stdio_uart(Progame_IV 0)
pico_enable_stdio_usb(Progame_IV 0)

pico_enable_stdio_rtt(Progame_IV 1) # Enable RTT

# Add the standard library to the build
target_link_libraries(Progame_IV
        pico_stdlib)

# Add the standard include files to the build
target_include_directories(Progame_IV PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
)

# Add any user requested libraries
target_link_libraries(Progame_IV 
        hardware_i2c
        )

pico_add_extra_outputs(Progame_IV)

