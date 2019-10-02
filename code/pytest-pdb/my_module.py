import requests


def get_ip():
    return requests.get("https://icanhazip.com")
