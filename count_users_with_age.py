def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    res = 0
    for item in data:
        print(list(item.values()))
        if item.get('age') == age:
            res += 1
    print(age)
    print(res)
count_users_with_age(data = [
  {
    'name': 'John', 
    'age': 35
  },
  {
    'name':'Mary', 
    'age': 20
  }
  ], age = 35)
