---
author: wookiemage
layout: post
title: "Colin's Peer Review of Becca's Drawing App"
---
Let's start with the assigment requirements:

The assignment stated that the app should:

Have an entirely graphical user interface (i.e. no printed text input besides what turtle.write())
 It does!
 
Allow the user to select a drawing mode that changes the program’s repsonse to clicks and/or keys
 It does!
 
Display the current mode and other relevant information to the user
 It does!
 
Allow the user to choose and draw shapes, lines, and colors depending upon the selected mode
 It does!
 
Allow the user to clear the drawing and start over
 It does! Well, most of the time. If you follow the directions and hit clear before switching modes, it does. If you switch before clearing then you're left with a mess. I think this is because each mode instantiates it's own screen and the mode switching function doesn't interact with the screen for each mode. We talked about this during our meeting, but ultimately it wasn't a deal breaker for the app and overall the app was super creative and fun.
 
I really like this apps functionality. It does three different and creative things. I don't much like the user interface because I feel like it's kind of always in the way. We have such a small area to work with, so I would prefer to get it a little more out of the way. This of course, is personal preference.

Let's talk about code:
The assignment stated that the code should:

Utilize custom modules for readability and organization
It does!

Utilize custom functions for modularity
It does!

Utilize definite loops (i.e. for loops)
It does!

Utilize multiple Turtle objects
It does!

Utilize a named Screen object
It does!

Run without errors
It does!

Be well-commented
It is!

Be well-organized and readable
It is! One thing I'm not sure of: why have your main.py be all but empty. There isn't really any code that lives in the main section other than importing functions from other modules which in turn import from other modules. It would seem to me that you could run at least the setup routine in the main.py file or call the other functions from the other modules directly there. It seems like an extra layer of abstraction.

Overall, her code was very clear and organized. It was commented at the function level for almost all the functions. It was very readable. The modes.py module had no comments on it, nevertheless it was fairly straightforward once you went into the other modules to see what the functions that modes.py called did.

Milestones and reflections:
Becca's milestones were all accomplished. She seems to have created them more as a checklist of the assignment requirements instead of thinking of them as different accomplishable blocks of code to create. For example: "is creative" is a difficult milestone to hit. How do you measure when you've accomplished being creative. Conversely, "can clear drawing and start over" is a good milestone because it's a function you can implement and check off when done.

I like the way Becca reflects on her process. She breaks her thoughts down into different things she wants to change. I like this because it's easy to group each thought that way and easy to understand what things irked her. I don't really get a good idea of her process from this reflection, but I can tell it was definitely iterative. Make something, think about it, change it, etc...
It's clear that Becca was very ambitious with this project and stretched herself to accomplish it. 

