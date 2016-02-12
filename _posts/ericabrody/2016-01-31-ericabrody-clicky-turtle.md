---
layout: post
author: ericabrody
title: "Erica's Clicky Turtle"
---

Here is my clicky turtle program - it creates fireworks wherever the user clicks on the screen:
<iframe src="https://trinket.io/embed/python/3737b50c6c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflections:
For this assignment, I started with the idea of creating fireworks wherever the user clicked on the screen, which required managing
multiple turtles (i.e. 12) on the screen at the same time so that I could create the multiple lines needed for the fireworks 
explosions at (almost) the same time. I defined a couple of functions in the module, animations.py, and discovered that error messages mentioned a particular line of code and then I had to figure out if they were referring to the main program or the module.

To make the fireworks disappear, initially, I redrew the lines using the background color, but the user could still see a faint version
of the firecracker after I did this, which I guess is called "zig zag artifact." I then found turtlename.clear() which erased the lines 
and was actually simpler to program. I created functions to randomize the color and length of each firecracker spoke -- this was 
good practice for writing syntax related to calling up functions. Initially, I kept trying turtlename.color(color), which didn't work and had to remember that the function needs () after it so turtlename.color(color()) - syntax took a while to come up with and looked weird at first.
