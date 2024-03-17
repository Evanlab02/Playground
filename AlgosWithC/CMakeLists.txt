cmake_minimum_required(VERSION 3.27)
project(AlgosWithC C)

set(CMAKE_C_STANDARD 23)

add_executable(AlgosWithC src/main.c
        src/cli/argparser.c
        src/cli/argparser.h
        src/commands/help.c
        src/commands/help.h
        src/commands/array_command.c
        src/commands/array_command.h
)
