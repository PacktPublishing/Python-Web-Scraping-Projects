from collections import defaultdict
from typing import Dict


def format_og(data, namespaces=False) -> Dict[str, Dict[str, str]]:
    """Format OpenGraph formatted data by flattening the structure"""
    results = defaultdict(dict)
    for name, value in data['properties']:
        namespace, name = name.rsplit(':', 1)
        if namespaces:
            results[namespace][name] = value
        else:
            results[name] = value
    return dict(results)

