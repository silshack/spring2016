---
layout: post
author: jamesma560
title: "James Drawing App Project"
---


Color Me Elmo:

<iframe src="https://trinket.io/embed/python/c6d43addf1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Milestones:

- [x] Have the user be able to interact with the screen using the mouse, as opposed to typing input through the bottom screen.
- [x] Create and use multiple modules. Have one main.py which references other refactored ".py" scripts. 
- [x] Use functions that I haven't used in previous programs
- [x] Draw something worth drawing (something aesthetically interesting/pleasing)
- [x] Have whatever the user 'draws' change color based off of where they click on the screen. 
- [] Use onkey to draw shapes
-[] Use a loop
- [x] use the .tracer() method to enhance my drawing app
- [x] Have a random element to the game

Revised Milestones:
-[x] Draw Elmo Stencil
-[x] Create a 'crayon'.
-[x] Have the user be able to drag the crayon and color in the stencil.
-[x] Give the user an option to switch colors based off key presses. 
-[x] Find a way to clear the screen.
-[x] Print the key to access different color modes.
-[] Display the current mode to the user

For my drawing app I initially wanted to do something simple for two reasons: 1. I'm not that skillful with Turtle drawings. 2. I'm not
that skilled with drawing in general, whether in the virtual world or the real one. So this initial inspiration ended up leading
to me wanting to create a "Color Me Elmo" app where I draw a stencil of Elmo and the user would be able to color it in. Sort of like
a Trinket coloring book. 

Another big goal of mine was to have this program be more refactored than my previous one. Off the top of my head I think across the 
other programs I’ve done this semester, I’ve used at most two .py modules, and therefore left a lot of refactoring to be desired. 
For this app though I’m proud of the fact that I have a more defined separation of concerns. If you look at my embedded code above, 
I basically confined all the screen specific stuff to the main.py file. I actually wanted to refactor this out some more but I had some 
trouble importing ‘screen’ from main.py to other modules so I just kept all the screen stuff in main. As far as the other modules go, 
elmo.py defines my drawing stencils, crayon.py handles the manipulation of the crayon, and colors.py handles the switching of different
color modes. 

Another thing I’m proud about is that I ended up using a lot of Screen and Turtle methods, which was one of the milestones I was most worried about. 
The most significant of the new functions I employed were the .ondrag(),.onkey(), and .listen() methods, since that’s what literally
made my drawing map interactive (I picked these tricks up specifically from watching your Chapter 2 Safari Book video). 

But as far as shortcomings go, I was disappointed with the fact that I wasn’t able to think of a good place to use a loop, or a good 
reason for the user to draw shapes themselves. And I also wasn't able to figure out a way to display the Color Mode my user was in 
aside from having them visibly see the crayon change color. 

But despite those shortcomings, I'm happy that my Color Me Elmo app could be seen as an extension of the intitial Robot apps
I turned in near the beginning of the semester, which I gues shows at least some evidence that I've progressed.

