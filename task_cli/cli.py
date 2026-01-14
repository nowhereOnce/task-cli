import argparse

def setup_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Adds a new task")
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

    # Mark in progress command
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Marks the given task as \"in progress\" status.")
    parser_mark_in_progress.add_argument("id", type=int, help="Integer ID of the task to mark as \"in progress\".")

    # Mark task as done
    parser_mark_done = subparsers.add_parser("mark-done", help="Marks the given task as \"done\" status.")
    parser_mark_done.add_argument("id", type=int, help="Integer ID of the task to mark as \"done\".")

    return parser