def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    res = 0
    for value in data.values():
        if isinstance(value, str):
            res += len(value)
    print(res)
find_length_of_values({"one": "one", "two": "two", 3: 3, 4.0: "four"})