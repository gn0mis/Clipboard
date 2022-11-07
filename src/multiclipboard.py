import sys
import clipboard
import json
import os

import reader

PARENT = os.path.dirname(os.path.dirname(__file__))

com_file = os.path.join(PARENT, "commands.yaml")
commands = reader.Reader(com_file).commands
command_list = list(commands.keys())
    
if len(sys.argv) == 2:
    command = sys.argv[1]
            
    if command == command_list[0]:
        print(command)
    elif command == command_list[1]:
        print(command)
    elif command == command_list[2]:
        print(command)
    elif command == command_list[3]:
        print("The different commands are: ")
        for command in command_list:
            print("  " + command + ": " + commands[command])
    else:
        print("Unknown command. Type '--help' for more information.")
else:
    print("Please pass exactly one command. For more info write '--help'.")