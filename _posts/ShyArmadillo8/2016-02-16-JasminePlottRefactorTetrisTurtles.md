---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Refactored Tetris Turtles"
---

Here is my completed refactored tetris turtles Trinket:
<iframe src="https://trinket.io/embed/python/19ce584663" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I liked this assignment, since it made me practice using strategies that I would not necessarily want to do like importing functions from
another module and using dictionaries.  For some reason, I had it in my mind that these strategies were more difficult to put into practice
than they actually were, but it actually worked out quite nicely.

When I first saw the code for this assignment, my immediate instinct was to separate all the different individual turtles and put them into
a separate module to create functions that would be called in.  My reason for doing this was because the original code was simply too long
and it was too difficult to separate which portions were doing what exactly.  By separating each of the specific turtles (whose purpose was
to draw a different portion of the gameboy), the code was cleared up significantly, and consisted primarily of a series of functions being
called.  I wanted to keep all these turtles within the same module, since it made sense to group the functions in the different modules by
what the different turtles were doing.

I had originally split the fin turtle functions (draw_screen, draw_grid, and fill_cell) into three separate turtles, but I discovered that
this was not an effective method.  It made the program run incredibly slow and eventually crash the browser.  I think this was because
the different modules and functions were communicating to each other constantly, which did not make the program as efficient as it should
have been.  I solved this by introducing fin outside these functions and then defining the functions individually.

I realized throughout the process of transferring these newly created functions to a second module that I needed to somehow have the colors
and pieces list available to all parts of the code.  With guidance from the hint in the instructions for the assignment, I realized that 
these were actually dictionaries.  I was not sure how they worked at first, but I tried importing them from another module and it surprinsignly
worked! This was pretty exciting, since it was an experiment on my part.  I will definitely use this as a tool in future programs.

With these two changes alone, the code from the original decreased from almost 300 lines to around 60.  I wanted to move the movement
functions moveLeft, moveRight, and moveDown into a separate module I had titled movements, but I discovered whenever I did so that this 
caused the program to not register keyboard input.  Perhaps I do not understand using keyboard input as much as I should, but this is a
goal that I intend to work towards better understanding in the future.  I was able to import the draw_piece function from movements, which
was nice and increased the organization of my program so someone new to the setup would be able to read through it and understand the 
parts that it had been separated into.

The changes that I made to the program helped make it more easily readable to someone interested in understanding the code, helped shorten 
the code, and made it easier to work with in the future.  It reminded me of the other exercise that we had where we had to go back through one of 
our previous homework assignments and turn the directions into functions; it looked a lot like my own code before and after this exercise.

