from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url.text)
        print(req)