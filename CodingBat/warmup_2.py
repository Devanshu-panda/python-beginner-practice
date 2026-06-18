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


