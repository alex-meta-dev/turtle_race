# Turtle race mini game
# Alexandru Meta
# 13 March 2023
import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=2000, height=1200)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
user_bet.lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_value = -300

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.shapesize(3)
    new_turtle.goto(x=-900, y=y_value)
    all_turtles.append(new_turtle)
    y_value += 100

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 940:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the bet! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost the bet! The {winning_color} turtle won the race!")
            is_race_on = False
            turtle.goto(0, 0)
            turtle.shapesize(8)
            break
        random_distance = random.randint(0, 35)
        turtle.forward(random_distance)

screen.exitonclick()
