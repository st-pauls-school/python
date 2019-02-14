from test import test 

# Q2
def sum_to(n, is_even):
  start = 0 if is_even else 1
  s = 0
  for i in range(start, n+1, 2):
    s += i
  return s


test(sum_to(10, True) == 30)
test(sum_to(11, False) == 36)