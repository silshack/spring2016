---
layout: post
author: RhymesWithMecca
title: "Becca's Tetris Refactor"
---

**Here is my Trinket:**
<iframe src="https://trinket.io/embed/python/a36745646e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

*Here is my reflection:*
I'm still a bit fuzzy on some of the details of this assignment.  The parts we've learned about (functions, conditionals, turtle 
things, etc.) made sense.  I had to look up some terms, like "tracer" and "onkey."  I'm not sure how the pieces dictionary works, exactly.  
And I hope this is cleaner, more readable, and more hackable.  Modules helped, a lot, as did making each turtle its ownfunction (in 
modules).

The first thing I looked at was the background shapes.  I first tried to move Jay into his own module, which didn't work.  Then I put 
everything that is relevant to Jay in its own Trinket, to see what he (and eventually, the rest of the setup turtles) did.  I went back 
to this later and the module worked the second time.  It also made "main.py" a lot shorter.  I did change the name "but" into "button,"
since it made more sense.

I discovered that the two dictionaries (colors and pieces) could be their own module, so I did that also to tighten up "main.py."

Also, the turtle named fin does three different functions, which all got their own module, since those are functional rather than
aesthetic like the functions in "setup.py."

For a while, I had an arrow attached to the Tetris pieces as they moved down the screen.  I realized that I had neglected to hide fin,
and it wasn't an arrow, it was a turtle!  

The one thing I would have liked to do that I didn't do was move the pieces functions into a module.  I kept getting error messages when 
I tried this.  I'm not sure how to fix it or if it's fixable.
