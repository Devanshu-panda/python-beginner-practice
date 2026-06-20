#Problem_1: first_last6
def first_last6(nums):
  n = len(nums)
  if nums[0] ==6 or nums[n-1] == 6:
    return True 
  else:
    return False

#Problem_2: same_first_last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False

#Problem_3: make_pi
def make_pi():
  return [3, 1, 4]

#Problem_4: common_end
def common_end(a, b):
  return(a[0] == b[0] or a[len(a)-1] == b[len(b)-1])

#Problem_5: sum3
def sum3(nums):
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  return sum

#Problem_6: rotate_left3
def rotate_left3(nums):
    nums.reverse()
    num_1 = nums[0:2]
    num_1.reverse()
    return num_1 + nums[2:]

#Problem_7: reverse3
def reverse3(nums):
  nums.reverse()
  return nums

#Problem_8: max_end3
def max_end3(nums):
  x = max(nums[0], nums[2])
  nums = [x, x, x]
  return nums

#Problem_9: sum2
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  return nums[0] + nums[1]

#Problem_10: middle_way
def middle_way(a, b):
  return [a[1], b[1]]

#Problem_11: make_ends
def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]

#Problem_12: has23
def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False


