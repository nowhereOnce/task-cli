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
    parser_add = subparsers.add_parser("delete", help="Deletes a task given its id.")
    parser_add.add_argument("id", type=int, help="Integer ID of the task to delete.")

    return parser