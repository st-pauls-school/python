from test import test 

def right_justify(s, w):
  if len(s) >= w:
    return s
  return "{0}{1}".format(' '*(w-len(s)), s)


test(right_justify("Hello, World.", 20) == "       Hello, World.")
