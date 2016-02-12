---
layout: post
author: jamesma560
title: "James' Clicky Turtle Exercise"
---

ClickyTurtle exercise:

<iframe src="https://trinket.io/embed/python/1479b5dac3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

This exercise was challenging. At the outset, before I even thought of the "game" I was going to create, I made a goal to refactor my code as 
much as possible. Unfortunately, it didn't work out so well. I ended up getting confused with all the returns and parameters that I ended up
having to combine multiple functions into one just to avoid running into errors. 

The toughest part for me was the "click" requirement. The trouble I was having was that I couldn't figure out a way to get the game 
to "pause" and wait for the user to click on the screen and interact with the game. If you look at my code, the first iteration of the clicky()
function was actually multiple functions (again, I was trying to refactor the code so that each function did ONE thing). The first function 
was meant to handle the "click" part; where the user selects what they think is the "evil twin" with their mouse. However, whenever I would run
the program, I wouldn't get any errors that stopped the script, but my script always skipped the "click" function and went straight to the 
subsequent functions, not allowing the user to click.

So to fix this, I basically had to combine all the functions that came after my "clicky" function into one clicky() function, and have that 
function be activated by a click (i.e. when the user selects an evil twin). There's probably a more elegant way to do it, but this is the 
only way I could get the program to pause and let the user make their selection. 
