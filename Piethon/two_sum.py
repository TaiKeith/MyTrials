def two_sum(nums, target):
  """
  Returns the indices of the two numbers in the array that add up to the target.

  Args:
    nums: An array of integers.
    target: The target sum.

  Returns:
    A list of two integers, where the first integer is the index of the first number
    in the array that adds up to the target, and the second integer is the index of
    the second number in the array that adds up to the target.
  """

  # Create a hash table to store the elements of the array.
  hash_table = {}
  for i in range(len(nums)):
    hash_table[nums[i]] = i

  # Iterate through the array, and for each element, check if the target minus the element
  # is in the hash table.
  for i in range(len(nums)):
    if target - nums[i] in hash_table:
      return [i, hash_table[target - nums[i]]]

  # If the target minus the element is not in the hash table, return None.
  return None

print(two_sum([2, 7, 11, 15], 9))
