---
author: namagic
layout: post
title: "Omar's Refactored Tetris"
---

<iframe src="https://trinket.io/embed/python/099dfc7804" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

To refactor this game, I first created additional modules for the colors, pieces, and several key variables. This immediately made this program easier to read. I then saw that the turtles were doing some similar things, so I appended the turtles to a list and performed the identical actions through a for loop. After that, I created more functions for each part of the drawing. I was not sure what to do after this because when I moved code to different modules to clean up the text a bit, I would have to import functions, variables from other modules. Not that this is challenging, but I don't think it necessarily made it easier to read. If someone were to read this from the bottom up, they'd see initial actions before they'd see all the drawing code.
