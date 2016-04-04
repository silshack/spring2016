---
author: yiyangshi
layout: post
title: "Yiyang's Turtle Refactory"
---

Here is the program:
<iframe src="https://trinket.io/embed/python/b5e8e21f01" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

1. I pulled out the functions for Nintendo game body drawing, gray screen drawing, screen light drawing, button drawing, keypad drawing, and speaker drawing from main.py into a separate file called screen.py. In the screen.py, I also created a function called draw_nintendo() that houses the six functions above. I did this because all of those functions are part of the screen setup. The codes are long but not relevant to the game itself. 

2. I also created a separate file called pieces.py to house the seven types of pieces and their width. The pieces codes take a lot of space in the main.py and prevents the readers from understanding the main body of the code easily. 

3. I created an additional file called playscreen.py to house draw_screen, draw_gride, and fill_cell functions. All of the aboved functions are finished by turtle fin and are the main pieces of the game display. 

4. I fixed the issue with the game where the "Z" can go exceed the screen on the right while the "I" cannot get to the last column of the screen. I fixed it by introducing another library called piece_width.
