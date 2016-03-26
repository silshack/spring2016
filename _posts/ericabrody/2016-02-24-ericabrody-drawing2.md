---
layout: post
author: ericabrody
title: "Erica's drawing program"
---

Here is my drawing program:
<iframe src="https://trinket.io/embed/python/e033f28477" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Milestones:
 - [ ] create setup screen - set screen size and then draw black square around edges of the screen so users can see them
 create setup screen - draw set of 4 square shaped buttons at upper left of screen with black edges and different color fill - these ended up being circle shaped buttons because I used turtles as buttons instead of drawing buttons as originally planned
 - [x] when user clicks on the button, the background color of the screen will change to that color
 - [x] When user presses the 'z' key, the turtle object shape will cycle through 3 options (turtle, arrow, circle)
 - [ ] to display shape mode to user, use unique (non-drawer) turtle object to make a stamp in the lower right hand corner of screen - 
 to display shape mode to user, when the turtle object changes shape, clear previous stamp and make a new stamp with the new shape, perhaps using "clearstamp" - couldn't figure out the code and this seemed like an unnecessary feature because people can see the turtle shape on the screen
 - [x] When user presses the 's' key, the turtle size will cycle through 3 or 4 different sizes to draw thinner or thicker lines
 to display turtle size, use unique (non-drawer, non-shape indicator) turtle object to write small or medium or large at bottom left hand corner of screen
 - [x] When user presses the 'c' key, the turtle will draw a small circle size = 20 pixels in diameter
 - [x] when user presses the 't' key, the turtle will draw a triangle
 - [x] when user presses the arrow keys, the turtle will go forward and backward & turn left and right
 - [x] when user clicks on the screen, the turtle will draw a line to the x,y coordinates of the part of the screen clicked
 - [x] when user clicks spacebar, the screen will clear the screen and allow the user to start over
 - [x] when user clicks on turtle object, the turtle object will change to a different color, cycling through 4 preselected colors

Reflection:
This project drew upon my knowledge of turtle and screen commands and the new information presented in the videos. I liked creating the list of milestones for the app. I did this after watching all of the videos and pulled out the functionality that I wanted to include in my program. I included a few items that I wasn’t sure I could figure out, like controlling the screen size of the drawing area. When I reviewed my milestones with Natalie, she made some helpful comments that validated my thinking on about the program. 

For troubleshooting: I used a separate trinket to test out code and get it working and then re-integrated it into the real program.     

I worked first on getting brute force code working, recognizing that some parts of the code could probably be refactored with more functions to be cleaner.

I was never able to figure out how to manage the screensize

After some trial and error, I figured out that a turtle can only be assigned to one class at a time, so you have to define all the functions for the functionality you want the turtle to be able to do in that one class. The keyboard prompts were not too difficult to implement. I used the Color Toggle code from the text to build my change color and change shape functionality. I may not have adapted the code as heavily as prescribed by the assignment, but I think I understand how it works.

I looked at tommy the turtle clicky turtle to figure out how to use "extra" turtles as buttons and how to avoid drawing lines to the buttons. But then I had to think about the problem differently to determine how to avoid drawing lines from the buttons to other places on the screen once the user changed the background color. I realized that the turtle didn't actually have to move the button area when the user wanted to click a button to change background color, so I restricted my clicky function to work only outside of the button area.

When i couldn’t figure out how to get the key functions working in their own "helpers" module, i added them to the class used to extend the turtle functionality.

Initially, I used the screen.clearscreen function to clear the screen; however, once the user pressed spacebar and cleared the screen, none of the drawing functionality worked and the frame and buttons would not be redrawn even though they were called in my clearscrn function. After a lot of time and several failures, I remembered that turtle has a clear function and tried that which happily worked.

Once I got the clearscreen functionality working, I noticed a turtle artifact in the middle of the screen. It was a turtle that sat at the coordinates, (0,0), but was not the turtle that was doing the actual drawing. i needed to figure out where it was created so i could eliminate it, i commented out frame - turtle was still there, i reinstated frame and the commented out buttons and it was still there. I noticed that it was drawn before anything else, so it seems to be a turtle artifact but I was unable to figure out its origins or how to hide it.

I refactored the code a bit to clean it up. Originally, the code for the sizemode turtle that writes the size of the pen on the screen was very long insert here
```
    if size_counter == 0:
      sizemode.goto(-185,-185)
      sizemode.clear()
      sizemode.write ('thinnest pen', None, "left", font=("Helvetica", 10, "bold" ))
    elif size_counter == 1:
      sizemode.goto(-185,-185)
      sizemode.clear()
      sizemode.write ('thicker pen', None, "left", font=("Helvetica", 10, "bold" ))
    elif size_counter == 2: 
      sizemode.goto(-185,-185)
      sizemode.clear()
      sizemode.write ('even thicker pen', None, "left", font=("Helvetica", 10, "bold" ))
    else:
      sizemode.goto(-185,-185)
      sizemode.clear()
      sizemode.write ('thickest pen', None, "left", font=("Helvetica", 10, "bold"))
```
and I was able to see the parts that were repeated and create more efficient code in the final program
```
    if size_counter == 0:
      message='thinnest pen'
    elif size_counter == 1:
      message='thicker pen'
    elif size_counter == 2: 
      message='even thicker pen'
    else:
      message='thickest pen'
    sizemode.goto(-185,-185)
    sizemode.clear()
    sizemode.write(message, None, "left", font=("Helvetica", 10, "bold"))
```
I would have liked to figure out how to refactor the button function to be cleaner but I didn't manage to do that.
I am looking forward to getting feedback and any guidance about hiding the turtle in the middle of the scren or refactoring my button code or managing the screensize.
