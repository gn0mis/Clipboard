import json
import os

class Writer:

    def __init__(self, filename=str, data=dict) -> None:
        path = os.path.dirname(os.path.dirname(__file__)) + "/history"
        filepath = os.path.join(path, filename)

        with open(filepath, "w") as f:
            json.dump(data, f)
