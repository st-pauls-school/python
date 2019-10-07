import turtle

def curves(height, step):
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.screensize(height*2.1,height*2.1)

    wn.onkey(wn.bye, "q")
    wn.listen()
    t.speed(0)

    for x in [-1, 1]:
        for y in [-1, 1]:
            for i in range(0, height+1, step):
                t.penup()
                t.setpos((0, y*(height-i)))
                t.pendown()
                t.goto((x*i,0))
    
    t.hideturtle()
    wn.mainloop()


curves(800, 20)