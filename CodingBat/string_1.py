#Problem_1: hello_name
def hello_name(name):
  return "Hello " + name + "!"

#Problem_2: make_abba
def make_abba(a, b):
  return a + 2*b + a

#Problem_3: make_tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "<" + "/" + tag + ">"

#Problem_4: make_out_word
def make_out_word(out, word):
  n = len(out)
  return out[0:n/2] + word + out[n/2:]

#Problem_5: extra_end
def extra_end(str):
  n = len(str)
  end = str[n-2:]
  return 3*end

#Problem_6: first_two
def first_two(str):
  return str[0:2]

#Problem_7: first_half
def first_half(str):
  n = len(str)
  return str[0:n/2]

#Problem_8: without_end
def without_end(str):
    return str[1:len(str)-1]

#Problem_9: combo_string
def combo_string(a, b):
 if len(a) > len(b):
   return b + a + b
 else:
    return a + b + a

#Problem_10: non_start
def non_start(a, b):
  return a[1:len(a)] + b[1:len(b)] 

#Problem_11: left2
def left2(str):
  return str[2:] + str[0:2]
