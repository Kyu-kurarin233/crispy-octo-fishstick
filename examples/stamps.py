"""
3.4CR Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "Zhibing Song"

from turtle import Turtle

def place_stamp(stamper: Turtle, x: float , y: float,ink:str):
    """
    Draws the author's initials
    bottom-left corner at (x,y)
    using specified ink 
    arg:
        stamper is instance of Turtle
        x:float
        y:float
        ink:str
    Return:
        None
    """

    old_ink = stamper.pencolor()
    old_direction = stamper.heading()
    old_x = stamper.xcor()
    old_y = stamper.ycor()
    
    stamper.penup()
    stamper.goto(x, y)
    stamper.setheading(0)
    stamper.pencolor(ink)
    stamper.speed(3)
    stamper.pendown()
    
    
    stamper.setheading(0)

    stamper.pendown()
    stamper.forward(100)

    stamper.right(135)
    stamper.forward(140)   

    stamper.left(135)
    stamper.forward(100)   
    
    stamper.penup()
    stamper.setheading(0)
    stamper.forward(150)
    stamper.pendown()
    
    stamper.forward (100)
    stamper.left(90)
    stamper.forward(50)
    stamper.left(90)
    stamper.forward(100)
    stamper.right(90)
    stamper.forward(50)
    stamper.right(90)
    stamper.forward(100)


    stamper.penup()
    stamper.goto(old_x, old_y)
    stamper.pencolor(old_ink)
    stamper.setheading(old_direction)


def main():
    t = Turtle() 

    place_stamp(t, 0, 0, "blue")
    place_stamp(t, -200, -100, "red")
    place_stamp(t, 100, 100, "green")
    
    t.pendown()
    t.forward(100)

    t.screen.mainloop()
    
    t.screen.mainloop()


if __name__ == "__main__":
    main()
