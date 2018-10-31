def argmin_random_tie(seq, key= lambda x: x):
    """Return a minimum element that ties at random"""
    return min(shuffled(seq), key=key)


def count(seq):
    """Count the number of items in sequence that are interpreted as true"""
    return sum(bool(x) for x in seq)

def first(iterable, default=None):
    """Return the first element of an iterable or the next element of a generator or default."""
    try:
        return iterable[0]
    except IndexError:
        return default
    except TypeError:
        return next(iterable, default)

def is_in(elt, seq):
    return any(x is elt for x in seq)

