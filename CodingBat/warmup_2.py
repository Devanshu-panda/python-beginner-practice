#Problem_1: string_times
def string_times(str, n):
    word = str
    if n>0:
        for x in range(n-1):
            word += str
        return word
    elif n==0:
        return ""

#Problem_2: front_times
def front_times(str, n):
  front = str[0:3]
  if n == 0:
    return ""
  elif n > 0:
    for x in range(n-1):
      front += str[0:3]
    return front

#Problem_3: string_bits
def string_bits(str):
    word = ""
    n = len(str) - 1
    if len(str) == 1:
        return str
    for x in range(n):
        z = 2*x
        if z <= n:
            word += str[z]
    return word

#Problem_4: string_splosion
def string_splosion(str):
  n = len(str)
  word = ""
  for i in range(n+1):
    word += str[:i]
  return word

#Problem_5: last2
def last2(str):
  n = len(str)
  sub_str = str[n-2:]
  count = 0
  if n <= 1:
    return 0
  else:
    for i in range(n):
        if i+2 <= n:
            if sub_str in str[i : i+2]:
                count += 1
    return count - 1

#Problem_6: array_count9
def array_count9(nums):
  n = len(nums)
  count = 0
  for i in range(n):
    if nums[i] == 9:
      count += 1
  return count

#Problem_7: array_front9
def array_front9(nums):
  if len(nums) <= 4:
    if 9 in nums:
      return True
    else:
      return False
  else:
    if 9 in nums[:4]:
      return True
    else:
      return False

#Problem_8: array123
def array123(nums):
    n = len(nums)
    all_sub_array = []
    for i in range(n):
        if i + 3 <= n:
            all_sub_array += [nums[i:i + 3]]
    if [1, 2, 3] in all_sub_array:
        return True
    else:
        return False

#Problem_9: string_match
def string_match(a, b):
    len_a = len(a)
    len_b = len(b)
    set_a = []
    set_b = []
    count = 0
    for i in range(len_a-1):
        set_a += [a[i:i+2]]
    for i in range(len_b-1):
        set_b += [b[i:i+2]]
    if len_a >= len_b:
        for i in range(len(set_b)):
            if set_b[i] == set_a[i]:
                count += 1
    else:
        for i in range(len(set_a)):
            if set_b[i] == set_a[i]:
                count += 1
    return count


