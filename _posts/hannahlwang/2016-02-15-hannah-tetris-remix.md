---
layout: post
author: hannahlwang
title: "Hannah's Remixed Tetris Turtles"
---

Here is my tetris remix:

<iframe src="https://trinket.io/embed/python/22cfcde4d5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Basically I created 3 separate modules - one for setup (all the things that go into drawing the Gameboy), one for dictionaries (color and pieces) and one for variables (all the positional things specified at the beginning of the original code). To import all the variables in the variable.py file, I used the code "from _____ import *", which I found [here](http://stackoverflow.com/questions/17255737/importing-variables-from-another-file-python). I also consolidated all of the screen drawing parts of the code into one function, "screenStuff", in my main.py file.

One issue I ran into was trying to separate out lines 13-112 in my main.py file into another module. Here is my attempt at that:

<iframe src="https://trinket.io/embed/python/46f961a995" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

As you see, the setup loads ok, but the pieces don't actually move down the screen like they're supposed to. I'm not exactly sure why this was happening, but I think that's partly because I didn't understand exactly how the pieces were controlled by the code in the first place. I'm glad I attempted, though! It did help me parse through the code and figure out what was referring to what.
