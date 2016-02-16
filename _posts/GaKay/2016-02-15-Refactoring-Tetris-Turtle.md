---
author: gao14g
layout: post
title: "Ga Kay's Refactoring Tetris Turtles"
---

Refactored Tetris Turtle:
<iframe src="https://trinket.io/embed/python/20b2d235b6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
For this assignment, I wasn't sure how much we should do to clean up the code. The main thing I did to clean up the code was to break the code up into functions. For all of the drawing functions (the buttons, the screen, keys, etc.), I created custom modules in another file and called those functions in the main file. This cleaned up the code a lot. I tried to figure out a way to make another custom module for the peices and the movements, but I found this to be more difficult. I tried to cut and paste certain parts of the code into new modules but there would always be some issue with variables missing. As a last resort, I tried to cut and paste the whole section into a new module, but I still couldn't get that to work. Since all of it was so intertwined, I decided to leave them in the main file page.
