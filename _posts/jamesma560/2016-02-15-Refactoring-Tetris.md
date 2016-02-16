---
layout: post
author: jamesma560
title: "James Refactoring Tetris"
---

Refactoring tetris exercise:

<iframe src="https://trinket.io/embed/python/c528fcb995" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

So I couldn't quite figure this one out in time. I think I got most of it done by refactoring the original code
individual actions. So for example I ended making functions out of the pieces, buttons, and keypad respectively. Once I refactored
everything I refactored, I copied and pasted the function definitions to the animations.py file. From there I ran the program, intentionally
running into errors, so I could find out when something needed to be returned or when I needed to pass something to a function. 

However I ran into a road block on line 272 (as you'll see when you run the code) with handling the pieces part of the program. I've tried returning
both p and pieces from pieces() and passing it into the draw_piece function but to no avail. I really feel like I'm close however. 
