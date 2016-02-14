---
layout: post
author: camazotz
title: "Navaneet's Enhanced Tetris Refactor!"
---

Refactored Tetris Turtles:

<iframe src="https://trinket.io/embed/python/94d50b7b6b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Enhanced Tetris Turtles:

<iframe src="https://trinket.io/embed/python/ef059387d7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

**Refactored Tetris**

In the refactoring process, I wanted to keep the page setup process outside of the main function as much as possible. So I created a module called pageSetup where I included all of the colors, pieces, functions for creating pieces, and constants. There were a lot of redundancies in creating each turtle so I built a function and had each turtle created by calling the function like so:

```
# Default code to setup turtles
def turtleSetup():
  someTurtle = turtle.Turtle()
  someTurtle.speed(9)
  someTurtle.hideturtle()
  return someTurtle
  
jay = turtleSetup()
sam = turtleSetup()
fin = turtleSetup()
but = turtleSetup()
key = turtleSetup()
speak = turtleSetup()
```

Each of the turtles also had their own specific set of lengthy instructions so I created a module for each and simply called that module's function from the main function.

**Enhanced Tetris**

I noticed that when the pieces reached the bottom of the grid, they disappeared because a new grid was drawn each time in the while loop and the previous pieces weren't saved. So I created a list and when each piece reached the bottom of the grid, I appended it as a tuple consisting of the piece, its height, and x and y values to the list because this information is needed when redrawing the piece. So on every iteration of the while loop, I also looped through the list of previous pieces and drew them as well.

As the number of pieces grew however, the tetris display began to lag, since a lot more drawing needed to be done on each iteration of the loop. To resolve this, I made the display tracer speed a variable (declared in my pageSetup module) and added a 1000 to it (1 second) after every three new pieces. That way the tracer keeps up with the time to render the increasing number of pieces.

I had also forgotten all of the rules of Tetris so I played it for a little while [here](http://tetris.com/play-tetris-flash/) and noticed that whenever I pressed the 'up' arrow key, the piece changed orientation. I implemented a similar function but rather than change the piece's orientation, I changed the the piece itself to another random piece from the list of pieces. I called this function 'moveUp' to be consistent with the already-present 'moveDown', 'moveLeft', and 'moveRight' functions.

To make this an actual tetris game however, the pieces will have to stack on top of one another at the bottom (right now they all just sort of blend into one other). So each piece will have to know the position of the other pieces and stop at a collision. I think drawing the grid and all pieces on each iteration is also not an efficient approach as the number of pieces increases. Only the new piece should be redrawn on each iteration. The up arrow function will also have to be changed to reorient the piece and not simply replace it with another piece.
