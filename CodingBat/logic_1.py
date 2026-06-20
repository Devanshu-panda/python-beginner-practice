#Problem_1: cigar_party
def cigar_party(cigars, is_weekend):
  if cigars <= 60 and cigars >= 40 and not(is_weekend):
    return True
  elif 40 <= cigars and is_weekend:
    return True
  else:
    return False

#Problem_2: date_fashion
def date_fashion(you, date):
  z = min(you, date)
  y = max(you, date)
  if z <= 2:
    return 0
  elif y >= 8 and z >= 2:
    return 2
  else:
    return 1

#Problem_3: squirrel_play
def squirrel_play(temp, is_summer):
  if 60<= temp <= 90 and not(is_summer):
    return True
  elif 60<= temp <= 100 and is_summer:
    return True
  else:
    return False

#Problem_4: caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed > 65 and speed <= 85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed > 60 and speed <= 80:
      return 1
    else:
      return 2

#Problem_5: sorta_sum
def sorta_sum(a, b):
  total = a + b
  if total <= 19 and total >= 10:
    return 20
  else:
    return total

#Problem_6: alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    if day >=1 and day <= 5:
      return "10:00"
    else:
      return "off"
  else:
    if day >=1 and day <= 5:
      return "7:00"
    else:
      return "10:00"

#Problem_7: love6
def love6(a, b):
  sum = a + b
  diff = abs(a - b)
  return(sum == 6 or diff == 6 or a == 6 or b == 6)

#Problem_8: in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    return( n <= 1 or n >= 10)
  else:
    return( n >= 1 and n <= 10)

#Problem_9: near_ten
def near_ten(num):
  remainder = num % 10
  return( remainder <= 2 or abs(remainder - 10) <= 2)
