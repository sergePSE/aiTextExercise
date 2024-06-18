from pathlib import Path
import json
import os.path

# files are saved in local directory, original names in index file json
# should not normally load everything im memory, can be database or maybe apache arrow, or simple grep
# for simplicity for now json
DIR = "store"
STORE_FN = f"{DIR}/.index.json"


# init function to prepare structure
def create_if_not_exists():
    Path(DIR).mkdir(parents=True, exist_ok=True)
    if not os.path.isfile(STORE_FN):
        with open(STORE_FN, mode='w+') as f:
            f.write("{}")


def record_file(name):
    with open(STORE_FN, mode='r+') as f:
        j = json.load(f)

        # if exists, overwrite
        if name in j:
            return j[name]

        max_index = 0
        if len(j.keys()) > 0:
            max_index = max(map(int, list(j.values())))
        j[name] = max_index + 1
        # need to go back in order not to append
        f.seek(0)
        json.dump(j, f)
        # rename file so none would overwrite by simple incrementation
        # can be smarter with e.g. hash
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
