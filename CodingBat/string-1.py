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


