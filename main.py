# Given a users data, return sum of all age values


# Example
# users = [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
# >>> sum_age_values(users)
# 69

# Example
# users = [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
# >>> get_max_age_user_name(users)
# 'Mary'

# Example
# users = [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
# >>> get_min_age_user_name(users)
# 'John'

# Example
# users = [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
# >>> count_users_with_age(users, 27)
# 1


# Example
# users = [{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
# >>> get_user_country(users, 'John')
# 'USA'


# Example
# users = [{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
# >>> get_user_names(users, 'USA')
# ['John']

def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    pass

# Example
# users = [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
# >>> get_user_names_with_age(users, 27)
# ['John']

def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    pass

# Example
# users = [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
# >>> get_user_names_with_age_range(users, 20, 30)
# ['John']

def get_user_names_with_age_range_and_country(data:list, min_age:int, max_age:int, country:str) -> list:
    """
    Return a list of users with a given age range and country

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
        country (str): The country to search for
    Returns:
        list: A list of users with the given age range and country
    """
    pass

# Example
# users = [{'name': 'John', 'age': 27, 'country': 'USA'}, {'name': 'Mary', 'age': 42, 'country': 'UK'}]
# >>> get_user_names_with_age_range_and_country(users, 20, 30, 'USA')

# ['John']

def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    pass

# Example
# users = [{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}]
# >>> count_jobs(users, 'Developer')
# 2

def get_country_with_most_users(data:list) -> str:
    """
    Return the country with the most users

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The country with the most users
    """
    pass

# Example
# users = [{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
# >>> get_country_with_most_users(users)
# 'USA'

# Example
# users = [{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
# >>> get_country_with_least_users(users)
# 'UK'

# Example
# users = [{'name': 'John', 'country': 'USA', 'age': 27}, {'name': 'Mary', 'country': 'UK', 'age': 42}]

# >>> get_country_with_most_users_with_age(users, 27)
# 'USA'

 



