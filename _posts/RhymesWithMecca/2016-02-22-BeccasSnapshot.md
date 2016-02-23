---
layout: post
author: RhymesWithMecca
title: "Becca's Drawing App Snapshot"
---

**Here is my Trinket:**

<iframe src="https://trinket.io/embed/python/efec14b438" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Here is my reflection:**

Looking back at my milestones, the only one that I haven't quite done is "user can choose and draw shapes, lines, and colors."  At the 
moment, these change based on coordinates clicked on and the random function.  This is Thing #1 to change for Thursday (or not, 
depending on how the other things I want to change go).  I could probably turn in what I have now and have it be fine, but I will 
tinker.  I'm going to create an entirely new Trinket as my final so I can keep what I have now.

Setup: This was pretty straightforward.  I need to work on carelessness though.  Sorry, Moony!

Changing Modes: I had trouble with the screen.onkey function to change the modes.  I had a function that took three arguments set up to
change the mode (h, f, or p, based on if the user wants Hagrid, Fleur, or Madam Pince Mode).  "if screen.onkey("h")", Hagrid Mode would 
be called. That didn't work.  I looked closer at the sample from the videos and used the make_gray function as a model.  I was close - 
screen.onkey needs two arguments, not one.

Functions: In general, it's useful to have hagrid.showturtle() to troubleshoot when you're coding the functions.  Also, 
commenting out tracer and update is helpful for the same reasons.  At fist, I was drawing my pine tree leaves as two right triangles 
because I forgot that I didn't need to start in the middle of a side to draw an equilateral triangle.  Then I started at an angle, 
made an equilateral triangle, and life was simpler.

I wanted to have Hagrid draw a maple tree for odd-numbered x-coordinates and a pine tree for even-numbered x-coordinates.  I remembered
Hannah doing something similar in the first clicky turtles exercise.  I had this:

---

  if int(x) % 2 ==0 and int(y) % 2 == 0:
     screen.onclick(pine)
  elif int(x) % 2 == 1 and int(y) % 2 == 0:
     screen.onclick(maple)

---

That didn't work.  I then looked back at my own clicky exercise and saw that I'd used one clicky function for all possible clicky things.
In this, I added if statements for the different coordinates, as well as a clear function (more on that later).  And then my one clicky 
function was screen.onclick(clicky).  In clicky, hagird.reset() didn't work (I'm not sure why, still) - I needed to make a clear 
function separately and call it in the middle of clicky (I had this idea at breakfast this morning.  Everything up until here
was done yesterday).  

Helper Turtles: I originally had Hagrid doing everything in his mode, but I then started to think about what needed to get cleared when
modes are switched.  I wanted to clear the drawing but be able to remind the user what keys to press to switch modes.  So the modes
at the top and the clear button are the responsibility of the helper turtle, and the instructions and drawings are the responsibility
of the non-helper turtle, for all three modes.  I think my helper turtle code could be cleaner (Thing #2 to change).

I'm Learning!: Fleur's mode was a lot easier than Hagrid's - I copied and pasted Hagrid and Fang's code and changed names and colors 
appropriately.  I would like to have the user navigate through the maze after drawing it (Thing #3 to change).  And maybe another
piece shape?  Madam Pince's mode is a bit simpler, but it was my first time using random.choice in a program (I got this from Jasmine's
clicky turtles).  The thing I'd like to fiddle with here is getting the orientation of the books to be consistent (Thing #4 to change).  
I had this problem with the maze pieces in Fleur's function, but it was less of a problem here since the maze can be in any orientation.

In all, I could submit what I have, but I'm a perfectionist, so I'm going to keep working on it.  I adapted a new tool over the weekend,
which involves setting a timer and making myself take a break after a certain amount of time (after adding comments to keep track of 
where I am, of course).  This was useful for this project in particular because there is SO MUCH CODE.  I usually take breaks, don't get
me wrong, but sometimes I'm bad at doing it at regular intervals.

