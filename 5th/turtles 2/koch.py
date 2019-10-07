import turtle 

wn = turtle.Screen()
t = turtle.Turtle()
wn.onkey(wn.bye, "q")
wn.listen()
t.speed(0)


def koch(l, mag, angle=0):
	if mag == 0:
		t.setheading(angle)
		t.forward(l)
		return
	koch(l/3, mag-1, angle)	
	koch(l/3, mag-1, (angle+60)%360)
	koch(l/3, mag-1, (angle-60)%360)
	koch(l/3, mag-1, angle)	

side=800
mag=5
t.penup()
t.backward(side/2)
t.left(90)
t.forward(side/4)
t.right(90)
t.pendown()
koch(side, mag,0)
koch(side, mag,240)
koch(side, mag,120)

wn.mainloop()