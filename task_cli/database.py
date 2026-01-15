import json 
from pathlib import Path

# Hidden folder to read/save the JSON file from
# (~/.task-cli)
DB_DIR = Path.home() / ".task-cli"

# Make sure the folder exists
DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "tasks.json" # Final path

def load_tasks():
    """ 
    Returns the data inside of the tasks JSON file
     - If the file doesn't exist or its empty returns a default dict 
    """
    if not DB_PATH.exists():
        return {"tasks": []}
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError: # JSON file exist but its empty
        return {"tasks": []}
    
def save_tasks(data):
    """ 
    Saves the data obtained frome the load_task func 
    """
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)