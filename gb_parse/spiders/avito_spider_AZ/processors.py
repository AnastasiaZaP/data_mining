def to_type(type_cls):
    def procedure(item):
        try:
            data = type_cls(item)
        except ValueError:
            data = None
        return data

    return procedure

def concatenate_items(items):
    result = " ".join(items)
    return result