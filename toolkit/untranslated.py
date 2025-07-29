def find_untranslated(source_dict, target_dict):
    """
    Returns a list of keys where the target value is missing or identical to the source.
    """
    untranslated = []
    for key, src_val in source_dict.items():
        tgt_val = target_dict.get(key, '')
        if not tgt_val or str(tgt_val).strip().lower() == str(src_val).strip().lower():
            untranslated.append(key)
    return untranslated