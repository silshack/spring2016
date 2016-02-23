 ---
layout: post
author: ericabrody
title: "drawing prog for peer clinic"
---
 Here is my drawing program in its current state:
 <iframe src="https://trinket.io/embed/python/e033f28477" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 
 Here is my progress on my milestones:
 
 - [x] create setup screen - set screen size and then draw black square around edges of the screen so users can see them
 - [x] create setup screen - draw set of 4 square shaped buttons at upper left of screen with black edges and different color fill- i   ended up using circle buttons
 - [x] when user clicks on the button, the background color of the screen will change to that color
 - [x] When user presses the 'z' key, the turtle object shape will cycle through 3 options (turtle, arrow, circle)
 - [ ]to display shape mode to user, use unique (non-drawer) turtle object to make a stamp in the lower right hand corner of screen
 to display shape mode to user, when the turtle object changes shape, clear previous stamp and make a new stamp with the new shape, perhaps using "clearstamp"
 - [x] When user presses the 's' key, the turtle size will cycle through 3 or 4 different sizes to draw thinner or thicker lines
 to display turtle size, use unique (non-drawer, non-shape indicator) turtle object to write small or medium or large at bottom left hand corner of screen
 - [x] When user presses the 'c' key, the turtle will draw a small circle size = 20 pixels in diameter
 - [x] when user presses the 't' key, the turtle will draw a triangle
 - [x] when user presses the arrow keys, the turtle will go forward and backward & turn left and right
 - [x] when user clicks on the screen, the turtle will draw a line to the x,y coordinates of the part of the screen clicked
 - [x] when user clicks spacebar, the screen will clear the screen and allow the user to start over
 - [x] when user clicks on turtle object, the turtle object will change to a different color, cycling through 4 preselected colors
 
 A few things left to try to fix:
 - [ ] refactor code for creating buttons and creating size mode indicator into loops or functions
 - [ ] figure out if there is a way to avoid drawing lines away from the buttons after selecting background color
 - [ ] figure out how to redraw the border and buttons after I clear the screen with the spacebar
