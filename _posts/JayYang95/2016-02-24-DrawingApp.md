---
layout: post
author: JayYang95
title: "Jay's Drawing App"
---

<iframe src="https://trinket.io/embed/python/e9b9c9b95f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Shapes:

 - [x] Draw circle
 - [x] Draw square
 - [x] Draw triangle
 - [ ] Draw circle centered around point clicked 
 - [x] Draw square centered around point clicked
 - [x] Draw triangle centered around point clicked

Size:

 - [x] Allow 3 different sizes (small, medium, large) for shapes
 - [x] Allow 3 different pen thicknesses for line drawing
 - [x] Prevent current selected thickness of pen from affecting thickness of lines that shapes are drawn with

Line:

- [x] Allows user to click around without automatically drawing a line to that point while in line mode
- [x] Let's user drag the arrow/turtle to draw a line
- [ ] Have the arrow/turtle remain a static, different color from its pen colors so that it is visible under a lot of drawing

Color:
 
 - [x] Let's user select different colors
 - [x] Brings up a different interface for user to click on a color
 - [x] Once color has been selected, go back to original interface
 - [ ] Retain the mode selected before user clicked on color mode

Modes:

 - [x] Lets user select between different modes (Shapes, Color, Line) by clicking on them
 - [x] Lets user repeatedly draw whatever mode is selected until a new mode is selected
 - [x] Functioning clear button

Display:

 - [x] Displays current mode, color, and size on topright
 - [x] Have separate turtles setup the interface and have tina be the sole turtle that does the drawing
 - [x] Have different turtles update each property (mode, color, size) on the display

Organization and Code:

 - [x] Comments
 - [x] Use of functions and custom modules
 - [x] Definite loops
 - [x] Screen Object
 - [x] Keyboard + Mouse used
 - [ ] Generally readable and eye-pleasing
 - [x] Works with no errors

A thing to note about the checklist. I started with a very basic list including shapes, lines, color, etc and added on to it while I 
was coding. If I ran into some sort of bug or annoyance, I added it onto the list and checked it off later if it was fixed.

Reflection:

This is much like my snapshot work in progress Drawing App, but with a few additional features and some bugs fixed.
The app lets the user click on whichever mode they want (square, circle, triangle, C for color, and line). Once the user has
selected a mode, the display in the topright will change from "None" to whatever mode is currently selected. The user can then
draw as many shapes or lines of the current mode as they want until they click on another mode. 

The color mode is unique from the rest of the modes in that it brings up a separate interface for the user to select a color.
Initially, the display will show the current color as "black" since that is the default. Once the user clicks on the desired color,
the display will update, as well as the color, and the original interface will replace the color interface. One slight annoyance to 
the color mode is that once a color has been selected and the program exits out of color mode, the user will have to re-select a
mode to draw in. Since I did not code for it to retain the mode it was in before it enters color mode, I simply made the display
update the current mode to "None" after color mode is exited. It will re-update once the user picks a new mode.

I originally had the line mode simply draw a line from the current position of the arrow/turtle to wherever the user clicks.
However, this did not truly feel like "drawing". So, instead, I made it so that while in line mode, if the user clicks on an area,
the arrow/turtle will simply go there without drawing a line. If the user clicks and drags the arrow/turtle, then a line will be drawn
following the arrow/turtle until the user let's go. It seems to function pretty well. There is a minor "bug" where if the user 
continues to move the mouse even after letting go of the mouse button, the mouse will continue to drag the arrow/turtle and draw
until the user clicks on the screen. To avoid this, the user must have the mouse still before letting go of the arrow/turtle.

I also added 3 options for sizes: small, medium, and large. These are toggled between by pressing "1", "2", or "3" on the keyboard.
It will change the size of the shapes that the user draws as well as the thickness of the pen drawn in line mode. Initially, I ran
into a problem where if the pen size was thick, the appearance of the shapes drawn would also be affected (edges of shapes would be
rounded instead of pointed). This was fixed by setting the pen size to small temporarily when drawing shapes, then resetting it
back to what it was after the shape was drawn.

I am pretty satisfied with how it turned out. Although it definitely wasn't the most creative, I am pleased that all the functions
that I created seem to work properly. Though I would have to argue that I probably could have used more modules to clean up the
main code. The things that were not checked off were not imperative to the functionality of the program, but simply quality of 
life improvements that I would have liked to implement but didn't. I have to say I really enjoyed this assignment  
as it reminded me how gratifying it is to get a program to do all (or most) of the things that you wanted it to do.
