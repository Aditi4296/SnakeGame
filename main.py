import turtle
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_index = 0
for i in range(0,3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(x=x_index ,y=0)
    x_index -= 20









screen.exitonclick()