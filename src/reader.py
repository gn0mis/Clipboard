import os
import yaml

class Reader:
    
    def __init__(self, filepath) -> None:
        self.commands = {}
        if os.path.exists(filepath):
            with open(filepath, "r") as stream:
                try:
                    for line in stream:
                        words =line.split()
                        com = words[0][:-1]
                        self.commands[com] = line.split(" ", 1)[1][:-1]
                except yaml.YAMLError as e:
                    print(f"Reading of file failed: {e}")
