import clipboard
import json
import os
import re
from sys import argv
from datetime import date, datetime

import reader
import writer

PARENT = os.path.dirname(os.path.dirname(__file__))
DATE_CHECK = "^[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}$"

com_file = os.path.join(PARENT, "commands.yaml")
commands = reader.Reader(com_file).out
command_list = list(commands.keys())
    
if len(argv) <= 3:
    command = argv[1]
    filename = str(date.today()) + ".json"
    data = reader.Reader(PARENT + "/history/" + filename).out
    
    if command == "save" and len(argv) == 3:
        key = argv[2]
        value = clipboard.paste()
        data[key] = value
        writer.Writer(filename, data)
        print("Data saved")

    elif command == "load" and len(argv) == 3:
        key = argv[2]

        if re.match(DATE_CHECK, key):
            r = reader.Reader(PARENT + "/history/" + key + ".json").out
            for key in r:
                print(f"{key}: {r[key]}")

        elif data.get(key):
            print(data.get(key))
        else:
            print("Given key hasn't been logged today.")

    elif command == "list" and len(argv) == 2:
        print(command)
    elif command == "--help" and len(argv) == 2:
        print("The different commands are: ")
        for command in command_list:
            print("  " + command + ": " + commands[command])
    else:
        print("Unknown command. Type '--help' for more information.")
else:
    print("If using 'save' command, pass save command and one string "
    "being used as a key. Otherwise, pass exactly one command  For more info write '--help'.")