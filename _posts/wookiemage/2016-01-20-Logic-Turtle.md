---
author: wookiemage
layout: post
title: "Colin's Turtle Logic"
---
I had some trouble finding any inspiration for this one. I just couldn't think of what to do.
So I started off overly ambitious. I decided I was going to draw the Apple Logo with the turtle. I didn't get too far. I couldn't make it fill in the spaces I wanted filled and leave the rest black. And positioning of the circles was difficult too. So I gave up on that one.
Instead, I decided on this program:
<iframe src="https://trinket.io/embed/python/f4b996cffb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I started off by figuring out how to make a dotted line, then I figured out how to set up a loop to draw that line instead of typing it all out manually. Then I put that loop in a loop so that it would draw that line 13 times to create a complete set of lines.
Check out my loop in a loop:
```
 ycord = -200
  for y in range(1,14) :
    tina.stamp()
    for x in range(1,60) :
      tina.pendown()
      tina.forward(1)
      tina.penup()
      tina.forward(10)
    tina.setx(-190)
    ycord = ycord + 30
    tina.sety(ycord)
```
The tricky part here was getting the coordinates right and then using trial and error to figure out how far I wanted tina to move for each line.

After that, the other options were pretty easy. Making lines was easier than dots because it only needed one loop. And making quadrille was similar to the dotted lines, except it moved in the X-Axis after finishing in the Y-Axis.
