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

#Problem_3: centered_average
def centered_average(nums):
  n = len(nums)
  total = 0
  smallest = nums[0]
  largest = nums[0]
  for i in range(n):
    if largest < nums[i]:
      largest = nums[i]
    if smallest > nums[i]:
      smallest = nums[i]
  for i in nums:
    total += i
  return  (total - smallest - largest)/(n-2)

#Problem_6: has22
def has22(nums):
  sub_array = []
  n = len(nums)
  for i in range(n-1):
    sub_array += [nums[i:i+2]]
  if [2,2] in sub_array:
    return True
  else:
    return False


