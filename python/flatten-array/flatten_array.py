def flatten_not(iterable):
    for i, x in filter(None, enumerate(iterable)):
        if x is None:
            iterable = iterable[:i] + iterable[i+1:]
            break
        if isinstance(x, list):
            iterable = iterable[:i] + iterable[i] + iterable[i+1:]
            break
        if isinstance(x, tuple):
            iterable = iterable[:i] + list(iterable[i]) + iterable[i+1:]
    if any(isinstance(i, (tuple, list, type(None))) for i in iterable):
        return flatten_not(iterable)
    return iterable

def flatten(iterable):
    res = []
    for i in iterable:
        if isinstance(i, (tuple, list)):
            res += flatten(i)
        elif i is not None:
            res.append(i)
    return res