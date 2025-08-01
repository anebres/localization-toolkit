import re

def validate_placeholders(source_dict, target_dict):
    issues = []
    pattern = r"{{[^}]+}}|\{[^}]+\}|%[sdf]|\$\w+"
    for key, src_val in source_dict.items():
        src_placeholders = set(re.findall(pattern, str(src_val)))
        tgt_placeholders = set(re.findall(pattern, str(target_dict.get(key, ''))))
        if src_placeholders != tgt_placeholders:
            issues.append((key, src_placeholders, tgt_placeholders))
    return issues