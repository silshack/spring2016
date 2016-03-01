---
layout: post
author: RhymesWithMecca
title: "Becca's Drawing App Peer Review and Self-Reflection"
---

When Colin and I talked on Tuesday, he told me he had problems with modes and switching them.   I said I had problems with that as well, but I did eventually figure it out. I mentioned that he could improve his user interface by having an option for the user to click on “press h for help,” as well as moving the button labels for the set color buttons.  The set-up functions should have turtle.tracer() so they are drawn instantaneously.  

When I told him I had screwed up my snapshot by editing it after we had talked on Tuesday, he said he made the same mistakes.  So the “press h for help” note above applied to the version that existed on Tuesday morning, but the current snapshot has that changed, since he changed accidentally it afterwards.

**The app:** 

Colin’s user interface is entirely graphical.  He still has the issues with modes that he discussed on Tuesday, in that there aren’t different modes.  The program does respond to clicks or keys.  One thing I’m not sure about is why the turtle returns to (0,0) every time the color is changed.  The current mode also is not displayed, as there aren’t modes.  The user can draw different shapes and change the turtle’s color – I really like the flower!  The user can successfully clear the drawing.  Overall, the app is not very creative, but it does the trick.  The one thing that I would do differently is to have the options displayed in a clearer fashion.  At the moment, the user can press h for help and the program cycles through the options, but this user had trouble remembering what the options are.

**The code:** 

Colin’s code doesn’t have modules (modules were part of the assignment).  In his final reflection, Colin discussed this and said he had trouble with it (similar to what he told me on Tuesday).  A strength of the program is the clarity of functions and the amount of them.  He is doing a lot with not very many lines of code.  There are a lot for loops in the code for the shapes functions, and they are used well.  There are multiple turtles (for me, calling these something other than the colors would be a little less confusing, but that might just be me).  The screen object is used as well, and the user can change the background color by cycling through the list of colors (I like this code).  The code does run with an error – Line 182 calls a “press0” function, which Trinket doesn’t find, so a Name Error happens.  I looked through the program and couldn’t find a function with this name, so I commented it out, ran it again, and it worked.  I assume that a press0 function existed in some version of this assignment that existed between the snapshot and the final one.  Everything is very well-commented and well-organized.  I had recommended that Colin add the tracer functions to the set-up portion with the buttons so it shows up instantaneously, which he didn't.  This is just another aspect of user interface to work on.

**The process:**

All of the milestones were met, but the milestones didn’t really reflect the assignment requirements.  A few things were adapted, but the user interface could definitely be improved, as I suggested (see above).

**Self-reflection:** 

Colin utilized higher-level Python that I did (I’m not entirely sure what class DrawTurtle(turtle.Turtle):  def __init__(self): means), but my app had more parts to it than his did.  I think there are things to be said for both methods.  The ideal code would be a combination of the two strategies (but would probably take a lot of time).  I think we both did a good job on this assignment.
