---
layout: post
author: wookiemage
title: Colin's Turtles
---

Here's the first Turtle:
<iframe src="https://trinket.io/embed/python/332d11321e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
This turtle was basically the same turtle I shared in class. It does prompt for info though.

Here's my super Turtle:
<iframe src="https://trinket.io/embed/python/7c81b5cc31" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
This turtle took it a little further. It not only asks for color options but also asks the user what kind of polygon they want to draw. There's a little math involed.
```
#The following lines do simple math to determine the interior angle of the polygon with the number of sides the user has specified.
#This spans multiple lines because I am unsure of order of operations in python. This declares far more variables than would be needed
#otherwise.
sides_2 = sides - 2
sides_3 = sides_2 * 180
sides_4 = sides_3 / sides
turn = 180 - sides_4
```
And it involved the use of a loop:
'''
#This makes tina walk and turn as many times as there are sides.
for x in range(0, sides):
  tina.left(turn)
  tina.forward(100)
  '''
  
Originally, I hoped to have the turtle draw a star with as many points as specified by the user but I ran into trouble with the math.
I'm sure there is a simple formula for it, but I decided to make my life easier and draw polygons.
Here's a fun challenge for more math minded folks, can you figure out how to make this go?
And for those of you who are more familiar with Python, can you make my math simpler / use fewer lines and variables?

Thanks!
