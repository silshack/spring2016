---
layout: post
author:yiyangshi
title: Yiyang's Turtle Exercise
---

Here's the User Input turtle program I'm embedding:
<iframe src="https://trinket.io/embed/python/5e83e014c2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```
# Here is the code:
import turtle
tina = turtle.Turtle()
myscreen=turtle.Screen()
myscreen_color=raw_input("What color should the background be?")
myscreen.bgcolor(myscreen_color)
tina_color=raw_input("What color should Tina be?")
tina.color(tina_color)
tina.forward(100)
```
Reflections:
This program is a simple example of a program that allows for user inputs. It is very helpful interms of game design.
One can think of games that requires a lot of user inputs and can lead to complete different result.

Here's the Coolest Turtle program I'm embedding:
<iframe src="https://trinket.io/embed/python/99ab53d1b7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```
# Here is the code:
import turtle

tina = turtle.Turtle()

myscreen=turtle.Screen()
myscreen.bgcolor('black')
tina.color('yellow','yellow')

tina.penup()
tina.back(100)
tina.pendown()

tina.fill(True)
tina.forward(200)
tina.right(144)
tina.forward(200)
tina.right(144)
tina.forward(200)
tina.right(144)
tina.forward(200)
tina.right(144)
tina.forward(200)
tina.right(144)
tina.fill(False)

tina.color('white','white')
tina.penup()
tina.goto(-60,-10)
tina.pendown()

tina.fill(True)
tina.forward(120)
tina.right(144)
tina.forward(120)
tina.right(144)
tina.forward(120)
tina.right(144)
tina.forward(120)
tina.right(144)
tina.forward(120)
tina.right(144)
tina.fill(False)

tina.color('yellow','yellow')
tina.penup()
tina.goto(-30,-20)
tina.pendown()

tina.fill(True)
tina.forward(60)
tina.right(144)
tina.forward(60)
tina.right(144)
tina.forward(60)
tina.right(144)
tina.forward(60)
tina.right(144)
tina.forward(60)
tina.right(144)
tina.fill(False)

tina.color('white','white')
tina.penup()
tina.goto(-10,-25)
tina.pendown()

tina.fill(True)
tina.forward(20)
tina.right(144)
tina.forward(20)
tina.right(144)
tina.forward(20)
tina.right(144)
tina.forward(20)
tina.right(144)
tina.forward(20)
tina.right(144)
tina.fill(False)

tina.hideturtle()
```
Reflections:
What the program does: 
This program draws stars inside stars. It gives a good visual effect.
The program's problem: 
1.The codes are highly repetitive. I wonder if there is a way to repeat the necessary code automatically.
2.The lengths and the angles of the stars are manually calculated. I wonder if this can be automated by some code.
Room for improvement:
1. Find out if there are some code sentences that are similar to a for loop that can reduce some repetitive codes.
2. Find out how to do calculations in Python and embed them into code to avoid manual calculation.

