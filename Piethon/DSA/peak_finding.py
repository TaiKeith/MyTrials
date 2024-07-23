def peak_finding(array):
  """
  Finds the peak element in a 1D array.

  Args:
    array: The array to search.

  Returns:
    The index of the peak element.
  """

  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2

    if mid == 0 or array[mid - 1] <= array[mid]:
      if mid == len(array) - 1 or array[mid + 1] <= array[mid]:
        return mid
      else:
        high = mid - 1
    else:
      low = mid + 1

  return -1


if __name__ == "__main__":
  array = [6, 7, 10, 12, 9]
  peak_index = peak_finding(array)
  print("The peak element is at index:", peak_index)
