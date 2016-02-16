---
layout: post
author: ericabrody
title: "Erica's Turtle Tetris - refactor"
---

Here is my refactored program:
<iframe src="https://trinket.io/embed/python/0f1ac855ef" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This was a daunting task initially; however, as I started reading through the program, I noticed little fixes I could make which gave me confidence that I could do this refactor.

I used a bunch of different strategies to learn which parts of the code corresponded to the various drawings created:
1) I changed the speed of tracer to 10, i.e., very slow, to see the drawing action in slow motion,
2) Using showturtle or commenting out hide turtle, I unhid turtles to see the direction they were pointing, their location, and more clearly see the shapes being drawn 
3) I tested out specific lines of code in a test trinket ex. turtlename.circle(20,70)
4) I looked up the hexadecimal colors to identify which parts of the program/screen are matched to which names
5) Once I got the code to draw the main screen items, (body, bezel, speakers, keypad, and buttons) working in the module I created (see #8 in next paragraph), I commented them out so I could focus on the remaining parts of the program


I refactored the program in several ways:
1)	The program wouldn’t stop on click because “disp.exitonclick()” was below the while loop that never exited, so I moved “disp.exitonclick()” above the while loop.
2)	I changed color name from dpad to keypad for ease of reading
3)	I changed the names of turtles, sam and jay, so they correspond to the parts of the screens they draw, i.e., body and bezel
4)	I changed the variable names for the colors of these new turtles, body and bezel, to bodycol and bezelcol, to avoid having two variables with the same name.
5) Since it seems that dictionaries can be called up in the main program from another module, I moved colors to the setup module as well. 
6)	I deleted the color named Nintendo, since it was never called.
7)	I copied the constants (inset, left, top, grid, w, and h) to the module scrnset.py, so they are defined in two places. I realize that this is actually not good coding etiquette because it creates the potential that the variables get out of sync. However, I didn’t have a good solution for making them available in the module otherwise. 
8)	I moved the code to draw the static items on the screen, (body, bezel, speakers, keypad, and buttons), into functions in a new module to increase readability of code.
9)	I changed the one use of penup to up, so that this function was called in a consistent manner throughout the program.
10) Edited the J shape since it originally seemed to draw the L shape.

I considered but did not implement a couple of changes:
1)	I considered creating lists and loops to set the speed and hiding of the turtles that draw parts on the screen, but decided to put these items within the functions that drew each shape for ease of readability instead.
2)	I tried to Move text definitions of pieces to a separate text file. I started by reviewing how to call up a text file by looking at Exercise 1 of Moar ch 8 exercies. When I reviewed several stackoverflow items http://stackoverflow.com/questions/11026959/python-writing-dict-to-txt-file-and-reading-dict-from-txt-file, http://stackoverflow.com/questions/9314824/python-create-dictionary-from-text-file-thats-in-dictionary-format, http://stackoverflow.com/questions/20411685/python-reading-a-text-file-into-dictionary,  I realized that I couldn’t just read in the text file, I need to tell python that it is reading in a dictionary. I wasn’t able to figure out how to do this within a reasonable amount of time, so I moved the dictionary into its own python module called “letters.py” to clean up the main program.
Remaining questions:
-	why didn’t the disp.screensize(600,600) work? 
-	What would be a better way to assign the constants, e.g., inset, once and have them be available in both the main program and the modules?
