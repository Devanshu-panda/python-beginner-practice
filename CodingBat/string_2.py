#Problem_1: double_char
def double_char(str):
  result = ""
  for i in range(len(str)):
    result += 2*str[i]
  return result

#Problem_2: count_hi
def count_hi(str):
  n = len(str)
  count = 0
  for i in range(len(str)):
    if "hi" == str[i:i+2]:
      count += 1
  return count

#Problem_3: cat_dog
def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)):
    if "cat" == str[i:i+3]:
      count_cat += 1
    if "dog" == str[i:i+3]:
      count_dog += 1
  return(count_dog == count_cat)

#Problem_4: count_code
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    sub_str = str[i:i+4]
    if "c" == sub_str[0] and "o" == sub_str[1] and "e" == sub_str[3]:
      count +=1
  return count

#Problem_5: end_other
def end_other(a, b):
  a_lower = a.lower()
  b_lower = b.lower()
  return(a_lower == b_lower[-len(a):] or b_lower == a_lower[-len(b):])

#Problem_6: 
