import requests
import json


class HiUtils:
    url = None
    data = None
    headers = None
    path = "http://localhost:5000/"

    def __init__(self):
        # self.set_url(self.path, "check")
        self.headers = {'Content-type': 'application/json'}

    def set_url(self, path, extension):
        self.url = path + extension

    def parse_data(self, data, extension):

        self.set_url(self.path, extension)

        response = requests.put(self.url, data=json.dumps(data), headers=self.headers)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(response.text)
            quit()

        return response.text


