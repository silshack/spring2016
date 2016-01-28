---
layout: post
author: wagerpascal
title: "Polygons strike back"
---

Original:

<iframe src="https://trinket.io/embed/python/eb7273e016" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

New/Refactored:

<iframe src="https://trinket.io/embed/python/0ded6af6c6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I took my polygon drawer from the first turtle exercise and created two functions- polygon() and chaircolor(chair_color, filledcol). My goal for the polygon() function was to make it auto-generating; the side number is generated from random.randrange().
However, chaircolor still takes the colors specified through questions. I didn't notice it before, but the arrow's outline color does change, so the attribute is not entirely overwritten. In addition, I added try/except conditions for the color function in case of bad inputs.
For the objective to return something, I included that the function return "True" when done coloring/filling, which then activates an if statement and a print function that prints that the drawing is done.

This exercise wasn't too difficult as the Chapter 4 exercises had made sure that I understand how to use functions, as well as that I was lucky that this program was already somewhat cleaned up to start with.
The main issue that I ran into was that I was first attempting to directly print a function from the return function, but I realized that it could not be used this way, and used the if statement method instead.
