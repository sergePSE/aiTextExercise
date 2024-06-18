To install

```
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
pip install requests
```
Then run
```
flask --app app run
```
Use the [postman collection](./postman_collection.json) for some sample requests
- Upload links - comma separated in body POST request to upload pictures from internet
- Get files - just get list of saved files
- Read file - put header 'url' with url to get the file