---
layout: post
author: RhymesWithMecca
title: "Becca's Drawing App"
---

**Here is my Trinket:**

<iframe src="https://trinket.io/embed/python/5c2462921b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Here is my list of milestones from last week, with an x in each box that I think I completed successfully:**

##### User...

 - [x] will not type - graphical interface only
 - [x] can select drawing mode (program changes) using clicks and/or keys
 - [x] can see current mode
 - [x] can choose and draw shapes, lines, and colors
 - [x] can clear drawing and start over

##### Program...

 - [x] uses custom modules
 - [x] uses custom functions
 - [x] uses definite loops
 - [x] uses multiple turtles
 - [x] uses a named Screen object
 - [x] is creative
 - [x] runs without errors
 - [x] is well-commented
 - [x] is well-organized and readable

**Here is my reflection:**

I'm going to organize this based on the list of things I wanted to fix from last time, and then something else that I thought of at the 
end.

Thing 1: I wanted the user to be able to control Fleur's color.  I both did this and ended up changing her entire mode a lot.  Now, 
the maze is preset and the user moves the turtle through the maze. My original plan was to do this, but after I'd made Hagrid's 
mode and started on Fleur's, I clicked in Fleur's mode and the trees from Hagrid's would appear.  I thus gave her multiple clicky 
functions, instead of just the "Clear" one (which would have fixed the problem, although I didn't know this at the time).  The maze 
pieces were weird, and it was hard to put them in a consistent, maze-like pattern.  I like its current state a lot more than the pieces.

Thing 2: I wanted to clean up my helper turtles code and the general look of the code.  I tried making separate functions for each turtle 
use (i.e. Gabrielle, Fleur's text, and the maze all had their own function), but then I got a blank screen.  So now the helper turtle
code is grouped together in each mode, before the main turtle is called.  I also added a lot of comments, which will hopefully
help with readability.

Thing 3: I wanted to be able to make Fleur move in the maze using the arrow keys.  This works.  I can (usually) make her move so as to 
avoid the hedges.

Thing 4: I wanted to make the orientation of Madam Pince's books consistent - they had been mirror images previously.  This required 
making her doing a 180 at the end of each book function.  To fix this, I commented out the corresponding tracer and update code and 
added a show.turtle so I could see where she was moving.  I used this technique a fair amount to debug throughout this project.

Also: The one thing that I am annoyed about is the clear functions.  The main turtle draws and clears the drawing when the user clicks
the clear button.  The helper turtle text (H = Hagrid Mode, F = Fleur Mode, and P = Madam Pince Mode) is supposed to go away once the user switches mode, based on the code in the change_mode() function, but this isn't happening.  I added text to the instructions at the bottom of the screen in each mode telling the user to clear the screen before switching modes.  I need the helper turtle text to stay after the drawing is cleared so the user knows which keys to press.  I can't revert to a universal set-up function because I indicate with colored text which mode the user is currently in.  One way to rectify this is to completely redo the interface, but that would be a bit of a headache.  The program **works**, so I think I can stop.  
