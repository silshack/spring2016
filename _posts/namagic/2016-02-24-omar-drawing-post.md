---
author: namagic
layout: post
title: "Omar's Drawing App"
---
<iframe src="https://trinket.io/embed/python/8d21dcdc53" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Going about the design of a full application, I realized that there was a lot of room. The instructions left a lot of room for integrating different design features. I believe that I have hit on all the required features. 

There are three main modes in my program, one with clicks, keyboard with the pen up, and keyboard with the pen down. The red turtle draws lines and responds to clicks and keys. The black turtle moves where the user would like the turtle to move to and draw shapes without drawing lines in its movement except for the drawing of the shape.

One thing I tried to get to work is the option to choose a background color, but I resorted to just have a random color chosen when the user presses the key “c” (bonus: if you hold down c, looks like a dance party). 

Regarding the two turtles, I couldn’t figure out how to have the turtles appear or disappear based on the mode.  I believe that the turtle that does draw lines couldn’t at this point because this turtle responds to both keys and clicks. I can’t hide the black turtle because I didn’t want to define the turtle in the function that defines its movements so I could use that turtle to draw shapes.

There is one strange feature that I haven’t figured out. I thought I had programmed this so that both turtles could draw shapes; however, but both turtles draw different shapes even when I select the right mode. I also really wanted to let the user be able to pick different size objects but I couldn’t think of a way to do that.  

Very quickly through designing this, I can see why programmers utilize milestones, pair programming, and how quickly, at least for me, excitement for certain features becomes disappointment when you realize you can’t actually incorporate that feature.

- [x] run without errors
- [x] separate into different modules for readability
- [x] include comment for every major function
- [x] ensure function and variable names make sense
- [x] create screen object
- [x] allow users to make shapes based on keys
- [x] entirely graphical user interface
- [x] allow user to select drawing mode that changes the program’s response to clicks and keys
- [x] display current mode and other relevant information
- [x] allow user to clear drawing and start over
- [ ] option to choose length of side(s) (small, medium, large)
- [x] utilize multiple turtle objects
- [x] utilize a named screen object
- [x] utilize define loops
- [ ] allow user to pick background color

