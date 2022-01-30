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
