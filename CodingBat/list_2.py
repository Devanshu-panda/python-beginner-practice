#Problem_1: count_evens
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count

#Problem_2: big_diff
def big_diff(nums):
  largest = nums[0]
  smallest = nums[0]
  for i in range(len(nums)):
    if largest < nums[i]:
      largest = nums[i]
    elif smallest > nums[i]:
      smallest = nums[i]
  return largest-smallest
