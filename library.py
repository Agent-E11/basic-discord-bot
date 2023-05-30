def command_echo(params: list[str]):
    if params == []:
        return None
    else:
        return f'{" ".join(params)}'
