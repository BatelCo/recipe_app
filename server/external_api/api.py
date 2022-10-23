import requests

class Api:

    def __init__(self, url):
        self.url = url
        self.raw_data = None

    def get_data(self):
        response = requests.get(self.url, self.headers)
        self.raw_data = response.json()
        return self

    def proccess_data(self):
        pass
