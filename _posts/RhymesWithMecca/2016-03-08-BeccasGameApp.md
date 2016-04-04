---
layout: post
author: RhymesWithMecca
title: "Becca's Game App"
---

**Here is my Trinket:**

<iframe src="https://trinket.io/embed/python/cca7028409" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Here is my reflection:**

Set-Up: I was fine with making the Founder turtles by a custom choice_turtle class, thanks to the james_turtle in-class example.  It took me a little bit to figure out how to pass x coordinates into the draw_choice_button function.  This was a lot faster for the write_choice_letter function, and the custom classes are very efficient on the whole.  I had an error message when I tried to set the world coordinates before picking a screen color - why is this?  They are very helpful, though - math is a lot easier with only positive numbers.

Clicky Questions: I'm glad I figured out how to put writing the question and writing the options in one question - again, much less code since I can just pass every query and four options into the function four times.  I had a bit of trouble with specifying the coordinates for the first clicky function.  My square worked the first time around, so I never slowed it down/had showturtle() to draw the square.  Turns out I had the coordinates wrong (I set clicky to work on coordinates from 0 to 400 to troubleshoot) and just needed to fix that to make it work (oops).

Originally, I called the Question 1 function, then the appropriate clicky function, then Question 2 all by themselves.  I had a problem where Question 2 would be called before the user had selected their answer to Question 1.  To solve this, I nested the Question 1 function and appropriate clicky function in the same function.  I then nested the entire Question 2 function inside the clicky function for Question 1.  This meant that I could have only one question whose answer was A, one question whose answer was B, etc.  I'm not sure if there is a way around this.  I'm glad I figured out the counter, and I like the user feedback for each question.

Key Functions: These annoyed me.  I initially wanted the user to be able to press 's' for start, but since Trinket won't let me import everything from setup.py into functions.py and vice versa, this didn't work (I needed setup in functions for the Turtles and background, and I wanted functions in setup to call Question 1 once the user pressed s).  My next idea was to have a second set of questions where the user presses a, b, c, or d to answer the questions.  I got all the way through clearing the screen, calling the first question, and answering it correctly before I realized that there isn't a way to deal with wrong answers, aside from making 16 different functions for all possibilities (i.e. you need a separate screen.onkey(function, 'b') for each question so it can call the subsequent one).  So I settled on the user calling their surprise/trophy, but I wish I'd been able to do something more involved without too much of a headache.

Surprise: Since the trophy is called only after all four questions have happened, I made a separate Trinket window to draw the picture so I wouldn't have to go through the whole program every time I messed up the geometry.  And no, I am not professing any art skills.

Overall, I am satisfied with what I have.  I'm curious if there is a way around my two posed problems.  And if my trivia questions are the right level of difficulty.

**Here are my milestones, with x's in the ones I think I completed successfully, and with some phrasing changed from the original pull request:**

**Required**

 - [x] interface is entirely graphical
 - [x] game uses key events (to display the surprise)
 - [x] game uses click events (to play the trivia game [clicking on certain spots on the screen to guess answers - spots drawn by extensions of Python's turtle class])
 - [x] game has a reason to play (winning points and a trophy)
 - [x] game displays win screen
 - [x] game keeps track of state - keeps track of points
 - [x] game displays information that updates - tells you if you got the question correct and adds points as you go
 
**Stretch**

 - [ ] game uses key events to change turtle/player (I'm not sure if this is possible)
 - [x] game has point accumulation
