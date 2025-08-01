# File Loaders: JSON / YAML
import json
import yaml

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Save Results to File
def save_to_file(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(data)

# Normalize Strings
def normalize_string(s):
    return str(s).strip().lower()

# Compare Strings Safely
def strings_match(s1, s2):
    return normalize_string(s1) == normalize_string(s2)