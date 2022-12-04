from ..regs.patterns import pattern_number


def __get_key(var):
    key = pattern_number.findall(var)
    key = [int(numeric_string) for numeric_string in key]
    return key


def sort_numeric(cls, items, preformat=None):
    """Sorted lists based on the number contained in the items"""
    if preformat is None:
        pre_f = cls.__get_key
    else:
        pre_f = lambda x: cls.__getKey(preformat(x))
    return sorted(items, key=pre_f)
