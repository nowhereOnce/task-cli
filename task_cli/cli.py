import argparse

def setup_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # List command
    parser_list = subparsers.add_parser("list", help="Lists the current tasks")

    # Delete command 
    parser_delete = subparsers.add_parser("delete", help="Deletes a task given its id.")
    parser_delete.add_argument("id", type=int, help="Integer ID of the task to delete.")

    # Update command
    parser_update = subparsers.add_parser("update", help="Updates a task given its id and a description")
    parser_update.add_argument("id", type=int, help="Integer ID of the task to update.")
    parser_update.add_argument("description", type=str, nargs="?", help="Task description to update")

    return parser