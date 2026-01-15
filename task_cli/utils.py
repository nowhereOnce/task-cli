import readline
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("Task-CLI", font="ansi_shadow")
    print()
    print(banner)
    print("Welcome to your personal task manager!\n")


def get_prefilled_input(prompt, prefill=''):
    """Aux function to handle the text input with pre-fill"""
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    except KeyboardInterrupt:
        raise # caller function decides the logic after this exception
    finally:
        readline.set_startup_hook()