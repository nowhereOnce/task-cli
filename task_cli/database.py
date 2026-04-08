import json 
from pathlib import Path
from filelock import FileLock
from contextlib import contextmanager

# Hidden folder to read/save the JSON file from
# (~/.task-cli)
DB_DIR = Path.home() / ".task-cli"

# Make sure the folder exists
DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "tasks.json" # Final path

lock = FileLock(str(DB_PATH) + ".lock")

@contextmanager
def db_session(mode= "r"):
    with lock:
        try:
            with open(DB_PATH, mode) as f:
                yield f
        except FileNotFoundError:
            if mode == "r":
                yield None
            else:
                raise

def load_tasks():
    with db_session(mode="r") as f:
        if f is None: return {"tasks": []}
        
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"tasks": []}
    
def save_tasks(data):
    """ 
    Saves the data obtained from the load_task func 
    """
    with db_session(mode="w") as f:
        json.dump(data, f, indent=4)