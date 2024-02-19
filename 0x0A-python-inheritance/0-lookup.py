#!/usr/bin/python3
def lookup(obj):
    all_attrs_methods = dir(obj)
    filtered_attrs_methods = [
        attr for attr in all_attrs_methods
        if not attr.startswith('_') and not callable(getattr(obj, attr))
    ]
    return filtered_attrs_methods
