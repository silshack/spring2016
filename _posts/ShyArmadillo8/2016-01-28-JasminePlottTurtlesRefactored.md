---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Turtles Refactored"
---

All in all, this was a pretty fun exercise, since it allowed me to expand on my Logical Turtles exercise and do what actually would have been easiest to do all along had I known how to do it.  In choosing which parts of my code I wanted to create as a functions, I chose to use a function for creating my circles.  The code looked like this:

```
def go_draw_circle(coordinate_x, coordinate_y):
    #Draw those peppermints!
    for x in range(int(peppermints)):  
      tina.penup()
      tina.goto(coordinate_x,coordinate_y)
      tina.pendown()
      tina.color(random.choice(colors))
      tina.circle(50)
      tina.left(90)
      tina.forward(50)
      tina.right(90)
      tina.forward(50)
      tina.right(180)
      tina.forward(50)
      tina.right (90)
      tina.forward(50)
      tina.right(180)
      tina.forward(50)
      tina.right (90)
      tina.forward(50)
      tina.right(180)
      tina.forward(50)
      tina.right(135)
      tina.forward(50)
      tina.right(180)
      tina.forward(50)
      tina.right(90)
      tina.forward(50)
      tina.right(180)
      tina.forward(50)
      tina.right(90)
      tina.forward(50)
      tina.right(180)
      tina.forward(50)
      tina.right(90)
      tina.forward(50)
      #We need to call new coordinates, otherwise Tina doesn't move away from her original spot
      coordinate_x = random.randint(-200,200)
      coordinate_y = random.randint(-200,200)
```

Initially, I didn't have the last two lines of code in my function, but I discovered that if I didn't tell the computer to randomize the coordinates, then the peppermints would just draw where they had been before rather than locating to a new location, which was what I wanted to do.  This was a fun way for me to play around with the different look of my peppermints.

The other function that I used was for calculating the calories consumed based on the number of peppermints eaten.  The code for that function looked something like this:

```
def calculate_calories(eat, peppermints):
    if int(eat) is int(peppermints):
       calories = int(eat)*2
       print("Since there are 2 calories for each peppermint and you had" + " " + str(eat) + ", you have consumed" + " " + str(calories) + " calories. You should eat more peppermints.") 
       return(int(calories))
    else:
      print("I know you're lying! Now we have to start from the beginning..")
```

Learning how to use a function to enable my program to repeat a loop for as many times as the user specified was so refreshing! It was so much quicker and more concise than having to copy and paste the code, as I had done in the previous assignment.  Functions are powerful features, since they expand the extent of the program and take some pressure off the programmer too.

One thing that I was really excited to learn about was how to randomize background colors and peppermint colors by importing random. This was exactly what I was looking for in my program, since I wanted to experiment and see how much I could do with color each time. 

Here's an example of my code for the background:

```
myscreen = turtle.Screen()
myscreen.bgcolor(random.choice(colors))
```

Here's my completed code for this exercise:
<iframe src="https://trinket.io/embed/python/fa2d627578" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Overall, this was a fun exercise that allowed me to be more concise in my code and make the process of coding more efficient.
