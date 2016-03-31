---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Poetry Slam Tina"
---

This was a pretty fun exercise! I liked the idea of working towards a program that had a fun end purpose to it.  The hardest part for
me was figuring out how to move the different input sections from one line to another.  I divided the program into 3 components.  
Below is the first portion:

```
import turtle

tina = turtle.Turtle()
tina.penup()
tina.goto(-180, 180)
tina.right(90)

still_going = True

slam_poetry = []
```

This first part of the code is where I summoned TIna, set my loop to True, and created an empty list. I had Tina turn to the right ninety degrees so that she was pointing downwards and would be able to write each line.

```
while still_going:
  lyrics = input("Enter a word or line of your poem.  Type done when you are finished. \n")
  if lyrics == "done" or lyrics == "Done":
    break
  slam_poetry.append(lyrics)
```

This above (and second) part of the code is where I created a loop to take the user input, which would ultimately be the lyrics, and then append each of the lyrics to the list.

```
x = 0
for lyrics in slam_poetry:
  tina.write(slam_poetry[x])
  tina.forward(25)
  x = x + 1
```
  
This final above portion of the code was the most complicated for me to figure out.  I set x as a variable equal to 0, and then for each of the lyrics in the slam poetry list I'd created, I asked Tina to write an item in slam poetry, move forward so she wouldn't overlap with the next line, and then add one to x so that we could move on to the next item in the list until we'd completed the list.  For some reason, I kept finding that the program would give me an error if I specified the font, alignment, or font size of tina.write(), and so I eventually just left these pieces off.  I'll have to play around with these in the future to see what I can correct.

Here is my completed Trinket:
<iframe src="https://trinket.io/embed/python/1d7bade207" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
