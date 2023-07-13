#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """
    Agrs:
        obj(list) for the first instance
        obj(str)
        obj(int)
        obj(bool)
    """
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(key): class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        return obj
    else:
        return {attr: class_to_json(getattr(obj, attr)) for attr in dir(obj) if not attr.startswith('__')}
