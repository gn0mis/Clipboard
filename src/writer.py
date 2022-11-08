'''Creates writer class'''

import json
import os

class Writer:
    '''Writes the clipboard history in json files'''

    def __init__(self, filename=str, data=dict) -> None:
        path = os.path.dirname(os.path.dirname(__file__)) + "/history"
        filepath = os.path.join(path, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
