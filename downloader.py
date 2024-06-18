import requests
from store import DIR, record_file
from io import BytesIO


def save_file(url):
    response = requests.get(url)
    bs = BytesIO(response.content)
    save_file_name = record_file(url)
    with open(f"{DIR}/{save_file_name}", "wb") as f:
        f.write(bs.getbuffer())