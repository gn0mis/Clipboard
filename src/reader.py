import os
import yaml

class Reader:
    
    def __init__(self, filepath) -> None:
        self.out = {}
        if os.path.exists(filepath):
            with open(filepath, "r") as stream:
                try:
                    for line in stream:
                        words =line.split()
                        arg = words[0][:-1]
                        self.out[arg] = line.split(" ", 1)[1]
                except yaml.YAMLError as e:
                    print(f"Reading of file failed: {e}")


file = os.path.dirname(os.path.dirname(__file__)) + "/history/test.json"
r = Reader(file)
print(r.out)