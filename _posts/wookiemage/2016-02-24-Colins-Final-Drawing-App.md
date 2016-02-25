---
author: wookiemage
layout: post
title: "Colin's Drawing App
"
---
  So here it is:
  <iframe src="https://trinket.io/embed/python/8c362a2928" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
  
  I had a heck of a time getting it to do different things when keys were pressed. Originally, my goal was to have a variable change which method in a list of methods disp.onlick would call.
  ```
  class DrawTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shapesIndex = 0
  ```
  I created a variable inside the class DrawTurtle that I created so that the variable would be invoked every time the class was instantiated. But, no matter what I did I could not get the disp.onclick method to see that variable. Or rather it would see the variable, but would only see its initial state instead of the new state that I set that too. I was able to write methods to change the variable and even print the variable and show that it was in fact different, but I just couldn't get the onclick method to see it.
  If I had to guess why, I would guess it had something to do with the screen object being different for each turtle. 
  Instead, I had tina go wherever you clicked, and then I had the methods draw things where ever her current position is. That way you can draw wherever you want.
  I also created turtle buttons that changed Tina's color and reset the screen. The positioning of these was a little tricky, but once I got them in the right place it wasn't too bad. Mostly it was just figuring out how to get the words the right distance from the turtle and from the "bottom" of the screen.
  Oh, and drawing flowers is difficult. I had to find a new turtle method so that the stem on the flowers would always face down. Fortunately for me, turtle.setheading exists. If it didn't, then I would have had to create some sort of variable to track the turtle's current direction and set it back to 270.
  
  Here are my final milestones and their status:
  - [x] Create a main.py that creates a screen and calls other functions
  - [x] Create a function that draws a circle
  - [x] Create a function that draws a square
  - [x] Create a function that draws a pentagon
  - [x] Create a function that draws a flower
  - [x] Create a function that changes the color drawn -- I actually did more than one of these
  - [x] Create a function that changes the background color
  - [x] Create a function that reacts to a click on a turtle -- Again I used this a lot
  - [x] Create a function that reacts to a click on the screen
  - [x] Create a function that reacts to button being pressed -- Lots of these too
  - [x] Create a function that moves your drawing turtle to the place clicked
  - [x] Move functions to modules where they make sense (animations.py, setup.py etc....) -- I think I could probably clean this up more, but I was having difficulty moving some of these functions out of the module that created the screen.
  - [x] Write User instruction text using a turtle -- And even better, I made a function to do this too!
