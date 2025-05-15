def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    key_list = []
    for key in data:
        if type(key) == int:
            key_list.append(key)
    print(key_list)
find_int_keys({1: "one", 2: "two", "three": 3, 4.0: "four"})
print(find_int_keys({1: "one", 2: "two", "three": 3, 4.0: "four"}))
