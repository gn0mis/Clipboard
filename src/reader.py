'''This module created the Reader class'''

import os
import yaml
import json

class Reader:
    '''Reader class reads the commands.yaml file as well as the
    clipboard history stored in the json files in /history'''

    def __init__(self, filepath=str) -> None:
        self.out = {}
        if os.path.exists(filepath):
            if filepath.endswith(".json"):
                with open(filepath, "r", encoding="utf-8") as stream:
                    self.out = json.load(stream)
            else:
                with open(filepath, "r", encoding="utf-8") as stream:
                    try:
                        for line in stream:
                            words =line.split()
                            arg = words[0][:-1]
                            self.out[arg] = line.split(" ", 1)[1][:-1]
                    except yaml.YAMLError as e:
                        print(f"Reading of file failed: {e}")

