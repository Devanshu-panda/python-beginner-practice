#Problem_1: Sleep_in
def sleep_in(weekday, vacation):
  if not(weekday) or vacation:
    return True
  else:
    return False

#Problem_2: monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not(a_smile) and not(b_smile):
    return True
  else:
    return False

#Problem_3: sum_double
def sum_double(a, b):
  if int(a) != int(b):
    return int(a) + int(b)
  else:
    return 2*(int(a) + int(b))

#Problem_4: diff21
def diff21(n):
  if n > 21:
    return 2*(abs(21-n))
  else:
    return abs(21-n)

#Problem_5: parrot_trouble
def parrot_trouble(talking, hour):
  if talking is True and hour > 20:
    return True
  elif talking is True and hour < 7:
    return True
  else:
    return False

#Problem_6: makes10
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a+b == 10:
    return True
  else:
    return False

#Problem_7: near_hundred
def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  else:
    return False

#Problem_8: pos_neg
def pos_neg(a, b, negative):
  if a>0 and b<0 and negative is False:
    return True
  elif a<0 and b>0 and negative is False:
    return True
  elif a<0 and b<0 and negative is True:
    return True
  else:
    return False

#Problem_9: not_string
def not_string(str):
  word  = str.split()
  if word[0] == "not":
      return str
  else:
      return "not " + str

#Problem_10: missing_char
def missing_char(str, n):
   return str[:n] + str[n+1:]

#Problem_11: front_back
def front_back(str):
  n = len(str)
  if n == 1:
    return str
  elif n >= 2:
    return str[n-1] + str[1:n-1] + str[0]
  else:
    return str

#Problem_12: front3
def front3(str):
  if len(str) < 3:
    return str+str+str
  else :
    return str[0:3]+str[0:3]+str[0:3]
    
