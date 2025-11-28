items = []

def push(val):
    if len(items) == 0:
        items.append((val, val))
    else:
        min_val = min(val, items[-1][1])
        items.append((val, min_val))


def pop():
    if len(items) == 0:
        return None
    return items.pop()[0]


def get_min():
    if len(items) == 0:
        return None
    return items[-1][1]