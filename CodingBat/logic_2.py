#Problem_1: make_bricks
def make_bricks(small, big, goal):
  rem_1 = goal % 5
  q = goal // 5
  if rem_1 == 0:
    if goal/5 <= big:
      return True
    elif goal/5 >= big:
      return(goal - big*5 <= small)
  else:
    if q >= big:
      return(goal - big*5 <= small)
    elif q<= big:
      return(goal - q*5 <= small)

#Problem_2: lone_sum
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: 
   sum += a
  if b != a and b != c:
    sum += b
  if c != a and c != b:
    sum += c
  return sum

#Problem_3: lucky_sum
def lucky_sum(a, b, c):
  sum = 0
  if a != 13:
    sum += a
    if b != 13:
      sum += b
      if c != 13:
        sum += c
      else:
        sum = sum
    else:
      sum = sum
  else:
    sum = sum
  return sum

#Problem_4: no_teen_sum
def no_teen_sum(a, b, c):
 return fix_teen(a) + fix_teen(b) + fix_teen(c)
 
def fix_teen(n):
  if n >= 13 and n < 15 or n > 16 and n <= 19: 
    n = 0
  return n

#Problem_5: round_sum
def round_sum(a, b, c):
  return round10(a) + round10(b) +round10(c)   

def round10(num):
  rem = num % 10
  if rem >= 5:
    return num + (10-rem)
  else:
    return num - rem
    
#Problem_6: close_far
def close_far(a, b, c):
  diff_1 = abs(a-b)
  diff_2 = abs(b-c)
  diff_3 = abs(a-c)
  if diff_1 <= 1:
    if diff_3 >= 2 and diff_2 >= 2:
      return True
    else:
        return False
  if diff_3 <=1:
    if diff_2 >= 2 and diff_1 >= 2:
      return True
    else:
      return False

#Problem_7: make_chocolate
def make_chocolate(small, big, goal):
  rem = goal % 5
  q = goal // 5
  if rem == 0:
    if goal/5 <= big:
      return 0
    elif goal/5 > big:
      if goal - 5*big <= small:
        return goal - 5*big
      elif goal - 5*big > small:
          return -1
  elif rem != 0:
    if q > big:
      if goal - 5*big <= small:
        return goal - 5*big
      elif goal - 5*big > small:
        return -1
    elif q <= big:
      if goal - 5*q <= small:
        return goal - 5*q
        
      elif goal - 5*q > small:
        return -1

