---
layout: post
author: touchwick
title: "Ian's Refactored Tetris Turtle"
---
This is my Tetris turtle:

<iframe src="https://trinket.io/embed/python/1a204748eb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

When refactoring, I decided that the first things that needed to move were the functions that depended on turtles. They take up a good deal of space, and with a simple comment and a good name for the functions, it's not hard to make it clear what they're doing while making the code significantly readable. At the same time, I moved the dictionaries. They, too, take up a crazy amount of space and can easily be called in from another module. The functions connected to piece movement stayed in ```main.py```. They are dependent on having ```piece```, ```piece_x```, ```piece_y```, and ```piece_h``` defined. The ```while``` loop depends on it as well. As the movement functions are short and relatively clear, I left them where they were in order to avoid complicating the structure of the program. 
