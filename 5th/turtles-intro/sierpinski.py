import turtle

def sierpinski(level=5, side=500):
	wn = turtle.Screen()
	wn.title("Triangles")

	a = turtle.Turtle()    

	a.pensize(1)
	a.penup()
	a.setpos(-side/2,-side/2)
	a.pendown()
	for i in range(3):
		a.forward(side)             
		a.left(120)

	internaltriangle(a, level, side/2)

	wn.mainloop()

def internaltriangle(t, l, s):
	if l==0:
		return
	t.forward(s)
	t.left(60)
	for i in range(3):		
		t.forward(s)
		t.left(120)
	t.right(60)
	# go to bottom left 
	t.backward(s)
	internaltriangle(t, l-1, s/2)
	if l > 1: 
		# go to bottom middle 
		t.forward(s)
		internaltriangle(t, l-1, s/2)
		t.backward(s)
		# go to left middle 
		t.left(60)
		t.forward(s)
		t.right(60)
		internaltriangle(t, l-1, s/2)
		# return to bottom left 
		t.left(60)
		t.backward(s)
		t.right(60)
		

sierpinski(5)
