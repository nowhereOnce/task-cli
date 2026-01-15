import readline

def get_prefilled_input(prompt, prefill=''):
    """Función auxiliar para manejar la entrada de texto con pre-llenado."""
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    except KeyboardInterrupt:
        # Lanzamos la excepción hacia arriba para que la lógica decida qué hacer
        raise 
    finally:
        readline.set_startup_hook()