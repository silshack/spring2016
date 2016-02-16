---
layout: post
author: tsukori
title: "Tetris Refactor Exercise"
---

<iframe src="https://trinket.io/embed/python/cb8a648b80" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So coming into this my design strategy was to separate everything into clean modules that made as much sense as possible. So here is what happened:  

* First thing I did after reading the code was creating a new module called `gameboy.py` that had everything in it that had to do with creating the gameboy. Then I took the giant code blocks and turned them into functions with intuitive names so I could delete the comments and clean up the code. 
* This was still really messy so I ended up creating another module called `turtles.py` that kept all of my turtles in it. My `turtles.py` was still messy and I realized that fin was a cut above the rest so I put fin in his own module and all of the others went into one together. I realized I wanted to import stuff without having to type out each thing so I googled it and found this (http://effbot.org/zone/import-confusion.htm) which showed me the `from module import *` and that was extremely useful. 
* I created a function `set_turtle` to cut down repetitive code, I looked for more code to refactor into functions but this was all I saw.
* My `gameboy.py` then basically became empty since I imported everything I needed into it using the functions from my turtles. 
* Realizing that the blocks can be further separated they became their own module: `blocks.py`
* I placed all of my constants into one module and imported those constants into `blocks.py`, `finturtle.py`, and `otherturtles.py`
* The last thing I tried was to place the moveDirection functions into a separate module but that ended up breaking everything so I just left in the main module since they were integral to how the game plays. 
