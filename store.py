from pathlib import Path
import json
import os.path

DIR = "store"
STORE_FN = f"{DIR}/.index.json"


def create_if_not_exists():
    Path(DIR).mkdir(parents=True, exist_ok=True)
    if not os.path.isfile(STORE_FN):
        with open(STORE_FN, mode='w+') as f:
            f.write("{}")


def record_file(name):
    with open(STORE_FN, mode='r+') as f:
        j = json.load(f)

        if name in j:
            return j[name]

        max_index = 0
        if len(j.keys()) > 0:
            max_index = max(map(int, list(j.values())))
        j[name] = max_index + 1
        f.seek(0)
        json.dump(j, f)
        return max_index + 1


def list_existing():
    with open(STORE_FN) as f:
        j = json.load(f)
        return list(j.keys())


def fetch_saved(url):
    with open(STORE_FN) as f:
        j = json.load(f)
        if url not in j:
            return None
        return f"{DIR}/{j[url]}"


create_if_not_exists()