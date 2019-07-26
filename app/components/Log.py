import json


class Log:
    file_path = None
    data = None

    def __init__(self, file_path):
        self.file_path = file_path
        self.load_data()


    def load_data(self):
        with open(self.file_path) as log_file:
            self.data = json.load(log_file)
