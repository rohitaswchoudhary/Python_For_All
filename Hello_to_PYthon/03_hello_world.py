import turtle
import random

win = turtle.Screen()
win.title("Hello World")
win.bgcolor("#c9bdbf")

turta = turtle.Turtle()  # I gave the name turta for my turtle



def turta_color():
    colors = random.choice(('#eb3434', '#eb8934', '#ebe534','#a8eb34','#5eeb34', '#34eb6e', '#05ffd1', '#059bff', '#0d05ff', '#7a05ff', '#bc05ff', '#f305ff', '#ff05b8', '#ff0522'))
    turta.color(colors) 


turta.pensize(4)  # set the width of turta as 4
turta.speed(100)



# Print the letter H

def print_H():
    turta_color()
    turta.penup()
    turta.goto(-320, 0)
    turta.pendown()
    turta.left(90)
    turta.forward(70)
    turta.penup()
    turta.goto(-320, 35)
    turta.down()
    turta.right(90)
    turta.forward(50)
    turta.penup()
    turta.goto(-270, 70)
    turta.pendown()
    turta.right(90)
    turta.forward(70)

# printing letter E

def print_E():
    turta_color()
    turta.penup()
    turta.goto(-260, 0)
    turta.pendown()
    turta.right(180)
    turta.forward(70)
    turta.right(90)
    turta.forward(35)
    turta.penup()
    turta.goto(-260, 35)
    turta.pendown()
    turta.forward(35)
    turta.penup()
    turta.goto(-260, 0)
    turta.pendown()
    turta.forward(35)

# printing letter L
def print_L(x,y):
    turta_color()
    turta.penup()
    turta.goto(x, y)
    turta.pendown()
    turta.right(90)
    turta.forward(70)
    turta.left(90)
    turta.forward(35)


# printing letter O
def print_O(x,y):
    turta_color()
    turta.penup()
    turta.goto(x, y)
    turta.pendown()

    for i in range(25):
        turta.right(15)
        turta.forward(10)

# printing  letter w
def print_W():
    turta_color()
    turta.penup()
    turta.goto(-10, 70)
    turta.pendown()
    turta.right(55)
    turta.forward(70)
    turta.left(150)
    turta.forward(70)
    turta.right(155)
    turta.forward(70)
    turta.left(150)
    turta.forward(70)


# printing letter R
def print_R():
    turta_color()
    turta.penup()
    turta.goto(160, 70)
    turta.pendown()
    turta.right(150)
    turta.forward(70)
    turta.goto(160, 70)
    turta.right(200)
    for i in range(20):
        turta.right(15)
        turta.forward(6)
    turta.left(180)
    turta.forward(60)


# printing letter D
def print_D():
    turta_color()
    turta.penup()
    turta.goto(290, 70)
    turta.pendown()
    turta.right(90)
    turta.forward(70)
    turta.penup()
    turta.goto(270, 70)
    turta.pendown()
    turta.left(120)

    for i in range(15):
        turta.right(15)
        turta.forward(10)

def print_L2():
    turta_color()
    turta.penup()
    turta.goto(220, 70)
    turta.pendown()
    turta.right(40)
    turta.forward(70)
    turta.left(90)
    turta.forward(35)
        

print_H()
print_E()
print_L(-210, 70)
print_L(-165,70)
print_O(-90, 70)

print_W()
print_O(70, 55)
print_R()
print_L2()
print_D()

turta.penup()

turta.goto(-90,-60)
turta.pendown()

turta_color()

turta.write("Python is cool!!!", font=("Calibri", 26, "bold"))


turtle.done()