from typing import Dict, List, Union


def format_jsonld(data, namespaces=False) -> Union[str, Dict[str, Union[Dict, List]]]:
    """
    Format json-ld formatted data by flattening the structure and removing metadata
    """
    results = {}
    if 'itemListElement' in data:
        return {data['@type']: [format_jsonld(v) for v in data['itemListElement']]}
    if 'item' in data:
        return format_jsonld(data['item'])
    for name, value in data.items():
        # if name == '@id':
        #     name = '_jsonld_id'
        if name.startswith('@'):
            continue
        name = name.split('#', 1)[-1]
        if isinstance(value, list):
            value = [
                format_jsonld(v, namespaces=namespaces) if isinstance(v, dict) else v
                for v in value
            ]
        if isinstance(value, dict):
            value = format_jsonld(value)
        results[name] = value
    if list(results) == ['name']:  # sometimes ItemListElements only have name fields
        return results['name']
    return results

