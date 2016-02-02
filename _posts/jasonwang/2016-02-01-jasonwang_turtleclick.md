---
layout: post
author: wagerpascal
title: "Clicky Madness"
---

Now don't get me wrong, it's not the game that's crazy, I'm the one who went crazy.

<iframe src="https://trinket.io/embed/python/eb252deff4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I hit a real creative block regarding what exactly I wanted to do. The original plan was to have a game of "tag", where the user-controlled turtle guess where the red circle goes. To help, the turtle points at the next point where it will go.
However, after a bit, I realized that it is a whole lot more difficult to create a system where the turtle has foresight with what we currently know. Also, the turtle's color will change based on its proximity to the last red point.

I believe that the only solution that I can think of is where I generate 3 random coordinates, and construct them into an array. From this array, I can still use randomly generated numbers, and know what value is next.
Unfortunately, I don't know how to use arrays in Python.
In addition, the array gives the user a limit of possible turns until failure, which would be nice for this type of game.

I would also like to note that the correct behavior of the game is highly dependent on the timing of the clicking (clearly more regulated clicking/slower clicking will yield intended results). For this program, rapid clicking will make the circles turn into a 3-D figure 8's, or something like that. This may be rectified through implementing a cooldown method (time.sleep()?).
