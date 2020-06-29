#the turtle library
import turtle             

# run (F5) this file

# type one of the function names from the shell 

# note that if you close the turtle window, you will need to re-run this

# to make new functions, copy the simple() function and replace the text in between the comments to do
# the different new movements 

def simple():
    # create the screen for the turtle to exist in 
    ts = turtle.getscreen()
    
    # create a turtle, assign to a variable  
    a = turtle.getturtle()    

    # code below here moves the turtle around

    # move the turtle around, left and right use degrees, forward
    # (and backwards) are approximately pixels 

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
    
    # code above here moves the turtle around
    
    # loop around - hit control-c to exit the function back to the shell 
    ts.mainloop()


def triangle():
    ts = turtle.getscreen()
    a = turtle.Turtle()    

    a.forward(80)             
    a.left(120)
    a.forward(80)
    a.left(120)
    a.forward(80)
    a.left(120)

    ts.mainloop()
    

def triangle2():
    ts = turtle.getscreen()

    a = turtle.getturtle()    


    ts.bgcolor("lightblue")
    ts.title("Playground")

    a.color("hotpink")
    a.pensize(5)
 
    a.forward(80)             
    a.left(120)
    a.forward(80)
    a.left(120)
    a.forward(80)
    a.left(120)

    ts.mainloop()




