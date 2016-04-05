---
layout: post
author: yiyangshi
title: "Yiyang's Logical Turtle Exercise"
---

Here is the logical turtle I created.
<iframe src="https://trinket.io/embed/python/5292f2db95" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

In the first turtle exercise, I created a turtle that draws stars within stars. In this program, I reproduced the sames stars by using the "for loop" and the "if" logical statements. In the original program, I wrote around 70 command lines to draw four stars. After using the loops and the logical statements, the number of lines used to draw the four stars is reduced to around 25. It shows that loops and logical statements can significantly improve a program by reducing the number of command lines.
I think there is still space for improvement for the coloring part. I want the pencil color to swith between yellow and white, and below is my current codes. Although it is just a feeling, but I don't think it is a good way to accomplish the color changing process by saying if the color is yellow then white, and if it is white then yellow. I wonder if there is a better way to achieve this. 

```
for number_of_star in range (1, 5):
  if previous_color=='yellow':
    current_color='white'
  if previous_color=='white':
    current_color='yellow'
  tina.color(current_color, current_color)
  #tina draw a star here
  previous_color=current_color
```
