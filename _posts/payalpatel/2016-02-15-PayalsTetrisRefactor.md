---
layout: post
author: payalpn
title: "Payal's Refactored Tetris Turtle"
---

**Tetris Refactor:**

<iframe src="https://trinket.io/embed/python/bc1892eb7a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


**Reflection:**

For this program I choose to move the functions into different modules which I could then import into the main module.  I did this in order to make the code more readable on the main module.  I created different modules including handheld, bezel, and topscreen.  These modules consisted of functions that were used to help create those parts of the program.  I grouped the functions in this way to make each module readable and to make sure the names of the modules could be easily understood by anyone who looks at the program or works on the program.  I also got rid of the colors dictionary in order to create modules consisting of the different functions needed for this program.  This allowed me to reduce some of the extra code from the main module and it allowed me to place the functions into different modules without having to place the colors dictionary in the module as well.  

I tried to move the puzzle dictionary to a different module (and other various functions towards the bottom of the program, such as, the move functions), however, I keep getting errors that I just can’t seem to get past at this moment.  With the previous functions I was able to figure out the errors, but not for the ones I just mentioned.  For example, some functions required other variables so I had to make sure they were included in the beginning of the module.  Also, I found with some functions I needed to create an input for the function and rename the variable (based off of the input) to make the functions and modules perform the same as the original program.  These strategies and techniques were effective at first, however, when I tried this with the pieces dictionary and the functions following that in the original program, I didn’t receive the same output.  At one point I was able to get it where the game looked the same, but the tetris shapes would end up coloring the entire row they moved down.  After this experience, I decided to create a function, movement, which consisted of disp statements calling the moveLeft, moveRight, and moveDown functions.  I then placed this function close to the top of the program as a way to declutter the bottom of the program (and then I just called the movement program when it was necessary).  
