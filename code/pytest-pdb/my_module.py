import requests


def get_ip():
    """Get my current external IP."""
    return requests.get("https://icanhazip.com")
