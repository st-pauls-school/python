from test import test 

def is_right_angled(a,b,c):
  return a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 

test(is_right_angled(13,12,5) == True)
test(is_right_angled(13,5,12) == True)
test(is_right_angled(13,11,6) == False)