'''
Code to decorate an string and show flashy effects on terminals.
'''

opening = '\x1b['
closing = '\x1b[0m'


def decorate(source: str, *,
             bold: bool = False,
             dim: bool = False,
             it: bool = False,
             uline: bool = False,
             blink: bool = False,
             strike: bool = False,
             duline: bool = False) -> str:
    """Decorates a string using ANSI Escape sequences

    Args:
        source (str): Original string
        bold (bool, optional): Bold text. Defaults to False.
        dim (bool, optional): Dim text. Defaults to False.
        it (bool, optional): Italics text. Defaults to False.
        uline (bool, optional): Underlined text. Defaults to False.
        blink (bool, optional): Blinking text. Defaults to False.
        strike (bool, optional): Strike-through text. Defaults to False.
        duline (bool, optional): Double-underlined text. Defaults to False.

    Returns:
        str: Decorated string
    """

    args = []
    if bold:
        args.append('1')
    if dim:
        args.append('2')
    if it:
        args.append('3')
    if uline:
        args.append('4')
    if blink:
        args.append('5')
    if strike:
        args.append('9')
    if duline and not uline:
        args.append('21')

    if len(args) == 0:
        return source
    else:
        prefix = ';'.join(args) + 'm'
        return opening + prefix + source + closing
