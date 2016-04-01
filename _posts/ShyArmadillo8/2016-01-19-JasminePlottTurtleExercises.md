---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Turtle Exercise"
---

Overall, this was a pretty exciting exercise that allowed me to experiment with Tina (I'd grown too attached to change her name to
something else).  The raw input trinket I created was fairly straightforward and easier than I had thought that it would be.  One
problem that I encountered and figured out how to solve was that when you ask Tina to do something with a variable that was selected 
by input, you don't put quotes around the variable name.  To clarify a little, it means that your code does not look like this (notice 
the quotation marks)...

```
#This allows background color selection
choose_background = raw_input("What color would you like the background to be?")
myscreen = turtle.Screen()
myscreen.bgcolor("choose_background")
```
Instead, your code should look like this...

```
#This allows background color selection
choose_background = raw_input("What color would you like the background to be?")
myscreen = turtle.Screen()
myscreen.bgcolor(choose_background)
```
Otherwise, I found this exercise fun, and a good opportunity for me to play around with color. Below is my completed trinket, which just 
a multicolored square of squares with a colorful background.

<iframe src="https://trinket.io/embed/python/c306d6c32f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For the second Turtle trinket I created, I wanted to experiment with some different shapes, so I referred to a couple different sources
to get an idea of how to do semi-circles and stars.  Below is the code that I used to create semi-circles (which were meant to be hills).
I copied the code from this site <a href="http://stackoverflow.com/questions/29441237/how-to-draw-a-semi-circle-in-python-turtle-only">
here </a>. From my understanding the "x in range" command tells Tina to move in a 180 degree motion forwards and to the right 1 time.

If you wanted to do this more than once, then you would change the number that comes after the forward and right instructions. I added
the extra right(180) to get Tina pointed in the direction so that she could make multiple semi-circles back to back.

```
#This is where we draw the hills with some semicircles
tina.pendown()
tina_color = raw_input("What color do you want the hills to be?")
tina.color(tina_color)
tina.fill(True)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.right(180)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.right(180)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.right(180)
for x in range(180):
    tina.forward(1)
    tina.right(1)
tina.fill(False)
```
I was pleased with how the hills turned out for the most part, but I couldn't figure out how to speed up drawing the hills.  I even 
used the proper code to increase the speed, but it would not work.  Does anyone have any ideas? I guess this taught me that even though you might copy and paste code that works, it's important to understand how to work with it.

I also created some stars after finishing the hills.  I copied the code from this site <a href="http://stackoverflow.com/questions/26356543/turtle-graphics-draw-a-star">
here</a>. The trickiest part for the stars was figuring out the coordinates to tell them where to go so that they could appear in different places on the screen.  I'm still not 100% sure how to use the coordinates on trinket, but I was surprised to discover that you can use negative numbers to direct Tina to different places. Below is the code that I used to draw the stars:

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

draw_star(25, "yellow")
```
The "for side in range" code is used to indicate how many times I want Tina to move with the directions specified underneath the code 
below those words, so it makes sense that this number would be 5 if I wanted to create a 5-pointed star.The size and color of the star
are specified at the very end of the code, so that Tina knows how many pixels to move forward in a certain direction (for my instance, 
it was 25), and what color the star will be.

Here is the final completed trinket I created.  To give you a clue about what you'll see in the end, I named this one Starry Night.

<iframe src="https://trinket.io/embed/python/9475228430" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

These exercises allowed me to play around with some different ideas and explore which of these ideas worked and which did not.
