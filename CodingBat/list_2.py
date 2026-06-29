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

#Problem_4: sum13
def sum13(nums):
    n = len(nums)
    sum = 0
    for i in range(n):
        if i <= 0 and nums[0] != 13:
            sum += nums[0]
        if i > 0:
            if nums[i - 1] != 13 and nums[i] != 13:
                sum += nums[i]            
    return sum

#Problem_5: sum67
def sum67(nums):
    ignore = False
    sum = 0
    for i in nums:
        if i == 6:
            ignore = True
        if ignore == False:
            sum += i
        if i == 7:
            ignore = False
    return sum

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


