import turtle

def simple():
    ts = turtle.getscreen()
    
    a = turtle.getturtle()
    
    a.forward(100)
    a.right(90)
    
    a.forward(100)
    a.right(90)
    
    a.forward(100)
    a.right(90)
    
    a.forward(100)
    a.right(90)
    
    a.color("red")
    a.penup()
    a.forward(300)
    a.pendown()
    a.forward(100)
    
    ts.mainloop()
    
    
simple()