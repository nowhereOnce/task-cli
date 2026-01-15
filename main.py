#!/usr/bin/env python3
from task_cli.cli import setup_parser
from task_cli.logic import add_task, list_tasks, delete_task, update_task, mark_in_progress, mark_done, mark_todo
from task_cli.utils import show_banner


def main():
    parser = setup_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)

    elif args.command == "list":
        list_tasks(args.status)

    elif args.command == "delete":
        delete_task(args.id)

    elif args.command == "update":
        update_task(args.id, args.description)

    elif args.command == "mark-in-progress":
        mark_in_progress(args.id)
    
    elif args.command == "mark-done":
        mark_done(args.id)

    elif args.command == "mark-todo":
        mark_todo(args.id)

    elif not args.command:
        show_banner()
        parser.print_help()

if __name__ == "__main__":
    main()