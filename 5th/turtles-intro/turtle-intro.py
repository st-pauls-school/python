#the turtle library
import turtle             

def simple():
    # create the window for the turtle to exist in - careful, it is case-sensitive!
    wn = turtle.Screen()
    
    # create a turtle and assign it to a variable
    # this one   
    a = turtle.Turtle()    

    # move the turtle around, left and right (i.e. anti-clockwise and clockwise) using degrees,
    # forward (and backwards) are approximately pixels
    
    # at the beginning the turtle points to the right, in middle of the screen
    a.forward(50)
    # turn 90 degrees left, so it now points up 
    a.left(90)
    # go forward (i.e. up) 
    a.forward(30)
    # turn left again, so now pointing to the left 
    a.left(90)
    # go back, i.e. to the right 
    a.backward(100)
    
    # stamp the shape
    a.stamp()
    
    # lift the turtle off the canvas
    a.penup()
    
    # move out of the way
    a.forward(200) 
    
    # this is an infinite loop - hit control-c to exist the window 
    wn.mainloop()


def triangle():
    wn = turtle.Screen()
    a = turtle.Turtle()    

    a.forward(80)             
    a.left(120)
    a.forward(80)
    a.left(120)
    a.forward(80)
    a.left(120)

    wn.mainloop()

def triangle2():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.title("Playground")

    a = turtle.Turtle()    

    a.color("hotpink")
    a.pensize(5)
 
    a.forward(80)             
    a.left(120)
    a.forward(80)
    a.left(120)
    a.forward(80)
    a.left(120)

    wn.mainloop()

def triangleLoop():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.title("Playground")

    a = turtle.Turtle()    

    a.color("hotpink")
    a.pensize(5)
 
    for i in range(3):
        a.forward(80)             
        a.left(120)

    wn.mainloop()