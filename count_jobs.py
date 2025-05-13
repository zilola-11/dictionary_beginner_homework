def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job
    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
   
    res = 0
    for item in data:
        print(list(item.values()))
        if 'Student' in item.values():
            res += 1
    print(res)
count_jobs(data = [
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Student'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]
, job = "Student")
lst = [1,2,3]

print()