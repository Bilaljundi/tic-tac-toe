import turtle

#Screen
w=turtle.Screen()
w.setup(600,600)
w.title('tick tak tok @by bilal')
w.bgcolor('white')
w.tracer()
#colone and row draw
cr=turtle.Turtle()
cr.color('black')
cr.goto(0,0)
cr.speed(100)
cr.hideturtle()
cr.forward(200),cr.left(180),cr.forward(400)
cr.right(180),cr.forward(100),cr.left(90),cr.forward(200),cr.left(180),cr.forward(100),cr.right(90)
cr.forward(100),cr.right(180),cr.forward(400),cr.left(180),cr.forward(150),cr.right(90),cr.forward(100)
cr.right(180),cr.forward(300),cr.right(180),cr.forward(100),cr.left(90),cr.forward(150),cr.left(90),cr.forward(100) 
#draw X 
def x1():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(-180,120),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x2():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(-50,120),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x3():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(80,120),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x4():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(-180,30),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x5():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(-50,20),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x6():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(80,20),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x7():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(-180,-80),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x8():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(-50,-80),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)

def x9():
 x=turtle.Turtle()
 x.speed(0),x.color('black'),x.penup(),x.goto(80,-80),x.pendown(),x.pensize(2),x.hideturtle(), x.left(35),x.forward(80),x.left(180),x.forward(40),x.left(100),x.forward(40),x.left(180),x.forward(80)
 # draw O
def o1():
 o=turtle.Turtle()
 o.penup(),o.goto(-150,120),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)
 
def o2():
  o=turtle.Turtle()
  o.penup(),o.goto(-20,120),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)

def o3(): 
  o=turtle.Turtle()
  o.penup(),o.goto(120,120),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)


def o4():
 o=turtle.Turtle()
 o.penup(),o.goto(-150,20),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)


def o5():
 o=turtle.Turtle()
 o.penup(),o.goto(-20,20),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)

def o6():
 o=turtle.Turtle()
 o.penup(),o.goto(120,20),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)

def o7():
 o=turtle.Turtle()
 o.penup(),o.goto(-150,-80),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)

def o8():
 o=turtle.Turtle()
 o.penup(),o.goto(-20,-80),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)

def o9():
 o=turtle.Turtle()
 o.penup(),o.goto(120,-80),o.hideturtle(),o.pendown(),o.pensize(2),o.circle(25)




w.listen()
w.onkeypress(x1,'1') 
w.onkeypress(x2,'2')
w.onkeypress(x3,'3')
w.onkeypress(x4,'4')
w.onkeypress(x5,'5')
w.onkeypress(x6,'6')
w.onkeypress(x7,'7')
w.onkeypress(x8,'8')
w.onkeypress(x9,'9')


w.listen()
w.onkeypress(o1,'')
w.onkeypress(o2,'')
w.onkeypress(o3,'')
w.onkeypress(o4,'')
w.onkeypress(o5,'')
w.onkeypress(o6,'')
w.onkeypress(o7,'')
w.onkeypress(o8,'')
w.onkeypress(o9,'')



w.mainloop()