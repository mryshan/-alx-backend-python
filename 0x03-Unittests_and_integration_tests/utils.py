# utils.py

def access_nested_map(nested_map, path):
    """
    Access a value in a nested dictionary using a tuple path of keys.

    Args:
        nested_map (dict): The dictionary to traverse.
        path (tuple): A tuple of keys to follow.

    Returns:
        The value found at the end of the path.

    Raises:
        KeyError: If any key in the path is not found.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map
