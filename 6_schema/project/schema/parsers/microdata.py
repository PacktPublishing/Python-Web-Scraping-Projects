from typing import Dict, Union


def format_microdata(doc: Dict[str, Union[str, int, float, Dict, list]], incl_type=True) -> Dict:
    """
    Reformat microdata extracted data by flattening property and type fields
    """
    # handle list objects by unpacking them to type:list format
    if {'itemListElement', 'type'}.issubset(set(doc.keys())):
        return {doc['type']: doc['itemListElement']}
    # skip processing unknown dict formats
    if not {'type', 'properties'}.issubset(set(doc.keys())):
        return doc  # only process
    # process type:properties objects
    results = {}
    for key, value in doc['properties'].items():
        if isinstance(value, list):
            value = [format_microdata(v) if isinstance(v, dict) else v for v in value]
        if isinstance(value, dict):
            value = format_microdata(value)
        results[key] = value
    if incl_type:  # whether to include type
        results['type'] = doc['type']
    return format_microdata(results)

