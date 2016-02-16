---
layout: post
author: wagerpascal
title: "Jason's Tetris Turtles"
---

Refactored:
<iframe src="https://trinket.io/embed/python/c4e8b72588" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My main goal for this part was to limit the amount of code that was in the "main" page. By moving a lot of the setup code to the setup.py file, most of the main file concentrated the actual rules/behavior of the game, which aided in the enhancing part.
To separate each drawing cursor for each part, individual setup files were created in the setup.py file. Due to the amount of materials that were moved over, I learned the importance of import * (which imports everything in the referenced file).

The only major thing that was changed in the main.py file was that the actual initialization of the turtles was set up there, as a loop that sets the speed and show/hidden state of the turtle is used.
Although, I believe it would be possible to also initialize each turtle in their respective setup functions, although each setup function would need its settings manually set.

Much of the frustration lies with trying to figure out what each part does. As there isn't a lot of documentation in the code, I sometimes had to resort to intentionally breaking certain functions to pinpoint what certain things done. Also, when moving blocks of code over, it was difficult to know if indents were messed with without comparing line-by-line. This led to a 30 minute hunt where I was combing through the code attempting to figure out why only 1 speaker showed up, rather than the regular 6.

Enhanced:
<iframe src="https://trinket.io/embed/python/6dad3e8dcd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

While organizing the code was fairly simple to understand, changing the code was a tad harder. I honestly had to go play tetris for a few minutes to figure out the non-movement controls at http://www.freetetris.org/index.html . 
I initially was looking into if it was possible to individually rotate each piece when pressing "UP", but I couldn't find any documentation of whether or not it was possible to rotate entities in a dictionary. At some point I read that they were immutable, so I was largely stumped on how to approach that problem. I was attempting to avoid a scenario where I had to make 4 different dictionaries for each rotation case, but is that the only solution?
So I decided to try and tackle if the tetris pieces are capable of doing the hard fall (where the piece automatically warps to the "floor", rather than the soft fall that occurs when you press "down".
However, much of the issue lies with the issue that the threshold is dependent on the type shape. My solution is sort of "hacky", as it is most reliant on the length of the longest piece (the 4 block vertical piece). However, it overcompensates for every other piece, most notably the square piece.
I attempted to define a global variable in a method similar to the other Move functions to make it more flexible, but it began to break the floor of the game.

However, refactoring cleared up the code so that it is easy to differentiate where things are. As I was primarily altering values pertaining to where the piece cuts off, I knew I could stay primarily in main.py. To finish this game, I need to figure out and fix the floor so that the hard fall will land at "piece_y - piece_h = 0 " for all cases.
In addition, the game will need a memory of what pieces landed where, a function to check if a row has been completely filled, a function to take away said row if it is filled, and a way to rotate pieces. Points and a losing case would be desirable as well.
