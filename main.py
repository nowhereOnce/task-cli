#!/usr/bin/env python3
from task_cli.cli import setup_parser
from task_cli.logic import add_task, list_tasks, delete_task


def main():
    parser = setup_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)

    elif args.command == "list":
        list_tasks()

    elif args.command == "delete":
        delete_task(args.id)

if __name__ == "__main__":
    main()