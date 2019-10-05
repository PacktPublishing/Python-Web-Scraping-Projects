from typing import Dict


def format_rdfa(data, include_id=False) -> Dict[str, Dict[str, str]]:
    """Format OpenGraph formatted data by flattening the structure"""
    if not isinstance(data, dict):
        return data
    results = {}
    for name, value in data.items():
        # processing the name removing url part, e.g. http://foo.bar#title -> title
        name = name.split('#', 1)[-1]
        # all fields by default are lists even when containing single item
        # e.g. "title": [{"@value": "scary book"}]
        if isinstance(value, list):
            results[name] = [
                # if it's a nested dictionary try to reformat it
                format_rdfa(v.get('@value') or v, include_id=include_id)
                for v in value
            ]
            if len(results[name]) == 1:  # flatten single level lists
                results[name] = results[name][0]
            if not results[name]:  # get rid of empty values
                results.pop(name)
        elif value:  # skip empty values
            results[name] = value

    # cleanup meta keys
    if include_id:
        if '@id' in results:
            results['_rdfa_id'] = results.pop('@id')
    else:
        if '@id' in results:
            results.pop('@id')
        if 'role' in results:
            results.pop('role')
    return results

