---
layout: post
author: ericabrody
title: "Erica's peer review of Payal's app & self-reflection"
---

THE APP

Payal’s drawing app is fun to use because it takes a food that I love and lets me play with customizing it with 7 different fun toppings that create a colorful drawing. I particularly like having so many different topping/drawing options. I also enjoy that the ice cream flavor changes randomly each time you run the program. This was such a creative idea. The user interface is very easy to use with the initial instructions on the screens and pressing the button for each topping is intuitive. The app also shows very clearly which mode the user is in by changing the color of the button associated with the active mode to pink. The titles of each topping run off the screen to the right a bit, but this doesn’t interfere with usability or functionality.

This app meets all the requirements of the assignment. One small piece of functionality that could be improved is that one has to press the “Start Over” button twice before the screen clears, rather than just once. And, there is one addition feature I would put on a wish list – for the toppings that are in liquid-ish form like fudge, caramel and whipped cream, it would have been fun to be able to drag the mouse around to draw these toppings approximating real life just a tiny bit more.

THE CODE

The code uses customized modules and functions that organize the code well. In addition, the program is well-commented so it is very easy to follow. The app also complies with all of the other code requirements, using for loops, multiple turtle objects, a named screen, and runs without errors. The variable and function names are descriptive and appropriately matched to their use. Most of the functionality used to introduce the app and set up the screen is found in two modules, ice cream.py and helpers.py. I wonder if the code for the definer turtle that writes labels for the different turtle buttons could have worked if it was located in the helpers module, since this is also an element of the initial set up of the screen for the app. 

Main.py is a bit long, so perhaps some more of the code (e.g., functions that create each of the toppings, SprinklesTopping, etc.) could have been placed in a additional modules. However, if this strategy was used, I think (but am not sure that) the functions would have had to be defined a bit more generically, for any turtle (e.g., def sprinklesTopping(a_turtle,x,y):  rather than for the single “maker” turtle. 

Nice use of a global variable! 

One question about the code: I am not sure what functionality the tracer(0) and tracer(1) provide in the functions named cone and ice cream.

THE PROCESS

Initially, Payal created a small set of milestones that described overall functionality of the app. Later, she created a more detailed set of milestones detailing the tasks required to create each of the app features. These milestones were clear, achievable and sufficient to satisfy the program requirements. Between the check-in on Tuesday and the final app on Thursday, Payal made significant changes to her code to improve the app functionality. Specifically, she transitioned from using mode buttons that she drew that did not allow a user to change mode to a set of turtles as buttons that let users click to reliably change mode. The functionality and code of the app reflect creative use of applying the programming tools that we have learned so far in the semester. In addition, it is clear that Payal thought very carefully about all the mini-steps needed to develop the functionality for the program to run. 

SELF-REFLECTION

My partner’s app was a more creative approach to the assignment than mine, which was a drawing program similar to that shown in the videos we watched prior to the assignment. Our code was somewhat similar in that we used separate modules for defining functions related to setting up the app, e.g., drawing the background. Looking back, I would have liked to create an app based on a different premise than just drawing on a blank canvas. My app included both keyboard keys and mouse clicks for drawing, whereas Payal’s ice cream app relied on mouse clicks only, which is probably easier for users. At a minimum, since I didn’t leave my introductory instructions on the screen, users may not have seen or remembered which keys they could use on my app. I think both our programs might be able to benefit from some refactoring with additional functions or loops to “automate” some of the repetitive parts of our code; however, I think both of our programs are well done given the amount of time we had for the assignment.
