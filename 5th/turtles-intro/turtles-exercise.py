#the turtle library
import turtle             

def triangle(n=80):
    wn = turtle.Screen()
    wn.title("Playground")

    a = turtle.Turtle()    

    a.pensize(5)
 
    for i in range(3):
        a.forward(n)             
        a.left(120)

    wn.mainloop()

def square(n=80):
    wn = turtle.Screen()
    wn.title("Playground")

    a = turtle.Turtle()    

    a.pensize(5)
 
    for i in range(4):
        a.forward(n)             
        a.left(90)

    wn.mainloop()

def polygon(n, p):
    wn = turtle.Screen()
    wn.title("Polygons")

    a = turtle.Turtle()    

    a.pensize(1)
 
    for i in range(n):
        a.forward(p)             
        a.left(360/n)

    wn.mainloop()

def star(n=100):
    wn = turtle.Screen()
    wn.title("5-pointed star")

    a = turtle.Turtle()    

    a.pensize(1)
 
    for i in range(5):
        a.forward(n)             
        a.right(720/5)

    wn.mainloop()

def clockface(n=100):
	wn = turtle.Screen()
	wn.title("Clockface")
	wn.bgcolor("green")
	
	a = turtle.Turtle()    

	a.pensize(1)
	a.color("blue")
	a.shape("turtle")
	for i in range(12):
		a.penup()    	
		a.forward(n)
		a.pendown()
		a.forward(20)
		a.penup()    	
		a.forward(20)
		a.stamp()
		a.penup()
		a.backward(n+40)      
		a.right(30)

	wn.mainloop()

def squares(n=10, l=100):
	wn = turtle.Screen()
	wn.title("Clockface")
	wn.bgcolor("green")
	
	a = turtle.Turtle()    

	a.pensize(1)
	a.color("blue")
	a.shape("turtle")
	for i in range(n):
		side = l*(n-i)/n
		a.penup()
		a.forward(l/(2*n))
		a.right(90)
		a.forward(l/(2*n))
		a.left(90)
		a.pendown()
		for i in range(4):
			a.forward(side)
			a.right(90)

	wn.mainloop()


# triangle(140)

# square(100)

# polygon(8, 200)

# star(120)

# clockface()

# squares()

