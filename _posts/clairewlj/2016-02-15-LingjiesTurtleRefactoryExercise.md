---
author: clairewlj
layout: post
title: "Lingjie's Turtle Refactory Exercise"
---

This is the program:
<iframe src="https://trinket.io/embed/python/1b2aa9384a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Generally, I make some changes to in order to make the main.py clearer and more readable, and I also try to fix the problems in the game that some pieces may exceed the screen board and some may fail to move to the right edge of the screen board.

For making the program cleaner:
I used a loop after 6 turtles were created and needed to set up the speed and hide turtle, and thus delete some repeating commands. 
Then I created a helper module named “names” to store library of colors and pieces, and another helper module named “background” to store drawing functions for every specific part of the graph. I also created a draw_bg() function to include all 5 functions of drawing body, board, button, keypad and speaker, so that once this function was called, the total background could be drawn. However, I kept this function in main.py in order to easily find and change it when needed to.

For fixing game problems:
I fist found that when the piece was ’S’ or ‘Z’ and I kept pressing “right”, the piece would keeping moving and exceed the right border of the game screen. Moreover, when the piece was ‘I’, it could not move to the last column. So I added two conditional executions to solve this problem.
Then I realized that if the piece in last loop was ‘I’, when it went down at the right edge of the game screen and the random choice for next piece was anything but ‘I’, the next piece would still exceed the screen edge. Also, similar problem occurred when the piece in last loop consisted of 2 columns and the random choice of next one consisted of 3 columns. Thus, I added detailed conditional executions to solve this problem.
