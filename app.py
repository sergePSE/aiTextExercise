from flask import Flask, request, abort, send_file
from downloader import save_file
from store import list_existing, fetch_saved
import os
from urllib.parse import urlparse

app = Flask(__name__)


@app.route("/images")
def get_image_list():
    return ','.join(list_existing())


@app.route("/image")
def get_image():
    url = request.headers['url']
    if not url:
        abort(400)
    path = fetch_saved(url)
    if not path:
        abort(404)
    filename = os.path.basename(urlparse(url).path)
    return send_file(path, download_name=filename)


@app.route("/upload", methods=['POST'])
def upload_images():
    body = request.get_data(as_text=True)
    if not body:
        return "empty body, nothing uploaded"
    urls = [x.strip() for x in body.split(',')]
    for url in urls:
        save_file(url)
    return str(len(urls))
