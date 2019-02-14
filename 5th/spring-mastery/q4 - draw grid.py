from test import test 

#Q4 
def draw_grid(x,y):
  edge = '*---'*y + '*\n'
  middle = ('|   '*y + '|\n') * 2
  grid = ((edge + middle)*x + edge )
  return grid

test(draw_grid(2,2) == '*---*---*\n|   |   |\n|   |   |\n*---*---*\n|   |   |\n|   |   |\n*---*---*\n')

