--- 
layout: post
author: camazotz
title: "Navaneet's Peer Review!"
---

Since my partner is no longer in the class, I will be self-evaluating my own app according to the criteria listed in the peer review description.

The App:

The app has an entirely graphical user interface. The app does not have more than one drawing mode (it draws the same two shapes) but it does change the location at which it draws those shapes and alternates them depending on the user’s click location. Since there is only one drawing mode, there is only a printed output to the user to “click on the tessellation shape to draw more!” and it displays this message throughout the gameplay. 

The user can decide whether to draw a black tessellation shape or white tessellation shape depending on the location of the click. If the user clicks on a black shape, two white shapes will be drawn. If the user clicks a white shape, two black shapes will be drawn. There is no option to clear the drawing and start over.

The Code:

There are custom modules for the black and white shapes which are properly indented, commented and readable. Each of the modules has their internal functions to reduce redundant code. The main class has a for loop inside a function that is called upon every mouse click on the screen. A new turtle is instantiated every time a new shape needs to be drawn and there is a named Screen object which handles screen clicks. 

The program runs without errors if the user waits for the shapes to finish drawing before clicking again. If the user clicks on another shape whilst other shapes are still being drawn, one of the shapes that is drawn will not be inserted into the list and there will be an index bound error further down the line.

Self-reflection:

After evaluating myself on both the app and code, I feel that I could have designed a better user interface. Since the program causes errors if the user clicks while it is still drawing, I could have included that in the instructions to the user to warn him/her about it. It would have also been easy to allow an option to clear the screen and start over (maybe a small button at the bottom). Since my program had to deal with aligning tessellation shapes, allowing the user to choose different tessellation shapes would have involved a considerable amount of work since each tessellation shape would have to have its own code for alignment so I’m not sure if that would have been feasible.

I think if I had some more time, I would have made it so that the drawing function is not repeated if a shape has already been drawn in a particular location. Right now, a new shape of the exact same proportions and colors is drawn on top of the previous shape (which takes up time and is probably not conducive to a good user experience). So some code could be added in to check if a shape already exists at a given location and not draw if that is the case.

All in all, I do like the idea of fitting tessellation shapes so maybe it can be modified to allow the user to place multiple tessellation shapes on the screen to create their own unique drawings. I didn’t like the way I handled individual shape clicks by iterating through a list that stored their coordinates. There must be a more efficient way of doing that so that’s something I would look into if I were to make this app on a grander scale.
