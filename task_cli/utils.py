import readline

def get_prefilled_input(prompt, prefill=''):
    """Aux function to handle the text input with pre-fill"""
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    except KeyboardInterrupt:
        raise # caller function decides the logic after this exception
    finally:
        readline.set_startup_hook()