def get_flat_keys(d, parent_key=''):
    keys = {}
    for k, v in d.items():
        full_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            keys.update(get_flat_keys(v, full_key))
        else:
            keys[full_key] = v
    return keys