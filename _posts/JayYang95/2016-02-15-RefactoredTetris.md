---
layout: post
author: JayYang95
title: "Jay's Refactored Turtle Tetris"
---

<iframe src="https://trinket.io/embed/python/b7ea74fab1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this exercise, I created several modules and moved over some functions from main. The first module was titled setup and initialized the speed of the turtles and hid them. It also drew the body and buttons of the gameboy. The second module was titled topscreen and included the functions that drew the screen and grid. I was going to stop at this but I took a peek at other students' work and noticed some had trouble creating a module for the pieces as they would run into errors with the variables. Thus, I decided I would attempt to modulize the piece functions as well and managed to do so by migrating all the variables and functions that had to do with pieces over to the pieces module. Then, in the while loop in main, instead of directly using the piece variables which would cause errors, I simply copy and pasted the original code in the while loop into a new function defined in the pieces module and called that function instead in the while loop. Overall, I found this to be challenging but fun, and it SEEMS that my refactorization of the code is working.
