import sys
import clipboard
import json

commands = {
    "save": 1,
    "load": 2,
    "list": 3,
    "--help": 4
}

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
        print(f"The different commands are: {commands}")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command. For more info write '--help'.")