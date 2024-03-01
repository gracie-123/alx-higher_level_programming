def find_peak(list_of_integers):
  """
  Finds a peak in a list of unsorted integers using binary search.

  Args:
      list_of_integers: A list of unsorted integers.

  Returns:
      A peak element in the list.
  """

  n = len(list_of_integers

  if n == 1:
      return list_of_integers[0]

  mid = n // 2
  if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
      return list_of_integers[mid]
  elif list_of_integers[mid] < list_of_integers[mid - 1]:
      return find_peak(list_of_integers[:mid])
  else:
      return find_peak(list_of_integers[mid + 1:])
