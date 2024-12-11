import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Comic Sans", 30, "normal")
score = 0
game_over = False

#turtle_list
turtle_list = []


#ScoreTurtle
sc_turtle = turtle.Turtle()

#Countdown Turtle
countdown_turtle = turtle.Turtle()

def setup_sc_turtle():
    sc_turtle.hideturtle()
    sc_turtle.color("blue")
    sc_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    sc_turtle.setposition(0, y)
    sc_turtle.write(arg="score = 0", move=False, align="center", font=("Comic Sans", 20, "normal"))

grid_size = 8

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        sc_turtle.clear()
        sc_turtle.write(arg="score = {}".format(score), move=False, align="center", font=("Comic Sans", 20, "normal"))

        #print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5,1.5)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


'''make_turtle(-20,20)
make_turtle(-10,20)
make_turtle(0,20)
make_turtle(10,20)
make_turtle(20,20)

make_turtle(-20,10)
make_turtle(-10,10)
make_turtle(0,10)
make_turtle(10,10)
make_turtle(20,10)

make_turtle(-20,0)
make_turtle(-10,0)
make_turtle(0,0)
make_turtle(10,0)
make_turtle(20,0)

make_turtle(-20,-10)
make_turtle(-10,-10)
make_turtle(0,-10)
make_turtle(10,-10)
make_turtle(20,-10)'''

x_cordinates = [-20,-10,0,10,20]
y_cordinates = [-20,-10,0,10,20]



def setup_turtels():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)


def hide_turtels():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtels_randomly():
    if not game_over:
        hide_turtels()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtels_randomly, 500)



def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("blue")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=("Comic Sans", 20, "normal"))
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtels()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=("Comic Sans", 20, "normal"))






turtle.tracer(0)

setup_sc_turtle()
setup_turtels()
hide_turtels()
show_turtels_randomly()
countdown(10)

turtle.tracer(1)






screen.mainloop()