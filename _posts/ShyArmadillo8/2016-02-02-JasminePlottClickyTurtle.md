---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Clicky Turtles"
---

This was an exciting turtle exercise that allowed me to work on functions and better understand how the user can click on screen.  What I
decided to do for my final Trinket was to play a "game" of sorts where the user just clicks on the screen until a blue star appears. There
is no specific layout as to how many times or where the user has to click for the star to turn blue, but when the blue star finally appears,
then the user has won the game, the user has won and is congratulated.  Here is the code that I used for my setup function as a preface to the game:

```
def setup(screen):
  colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
  screen.bgcolor(random.choice(colors))
  
  sally = turtle.Turtle()
  sally.hideturtle()
  
  sally.color("black")
  sally.penup()
  sally.goto(0,-100)
  sally.write("Let's play a game!", "Cambria", "center", "22pt bold")
  time.sleep(2)
  sally.clear()
  sally.write("You don't want to? Too bad!!!", "Cambria", "right", "18pt bold")
  time.sleep(2)
  sally.clear()
```

After the user has been forced into the game, they are instructed to click the screen.  This action causes stars of different colors to
be drawn all throughout the screen.  Here is the code that I used to define my star and its parameters:

```
def draw_star(size, color):
    angle = 120
    tina.fillcolor(color) 
    tina.begin_fill()
    for side in range(5):
        tina.forward(size)
        tina.right(angle)
        tina.forward(size)
        tina.right(72 - angle)
    tina.end_fill()
    return
```

The biggest hurtle that I kept running into was how to get the congratulate function to work when the blue star actually appeared.
I realized that 1.) I needed to define size and color before running the draw_star function and 2.) I needed to add color to the above
function where I began to draw my star with the "tina.fillcolor()". Using the random.choice(colors) allowed my stars to have randomly
generated colors that will ultimately lead to blue.  Here is what the clicky looked like with the draw_star function called inside:

```
def clicky(x, y):
  tina.penup()
  tina.goto(x, y)
  tina.pendown()
  color= random.choice(colors)
  size = 25
  draw_star(size, color)
  if color == "blue":
    congratulate(tina)
  else:
    print("Keep clicking!")
```
 
 I was lucky that I was able to include logic into my clicky function in some form by including the "if" allow the congratulate
 function to play when the blue star finally appeared and the encouraging "Keep clicking!" to let the user know that they were on the
 right track.  All it took was more clicking.
 
 Here is my final version of my Clicky Turtle Trinket:
 <iframe src="https://trinket.io/embed/python/b1fce1bf20" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 
 Overall, this was an exciting way to play around with functions and clicking on the screen!
