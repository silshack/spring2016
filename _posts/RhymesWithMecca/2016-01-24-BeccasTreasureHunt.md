---
layout: post
author: RhymesWithMecca
title: "Becca's Treasure Hunt"
---

<iframe src="https://trinket.io/embed/python/394c2838f8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I did a fair amount of troubleshooting with this assignment.  I went through three stages:

Stage 1: User X and Y Input for Coordinates
I had to tinker (pun intended) with the ands and ors here.  I didn't realize I needed an "else" statement for a while, and I had less than and greater than signs instead of less than or equal to/greater than or equal to signs.

Stage 2: User Feedback for How Far Away
It took me a while to realize that I needed to start with the specific and then get broader (i.e. "You won!" to "You are far away.") instead of vice versa.  I did learn, quite by accident, that you can do 0 < x < 5 all in one line rather than 0 < x and x < 5, which made my code considerably shorter.

Stage 3: Combining Them
I needed to enter a few possible coordinates and have them fail/navigate to unexpected places in my code before realizing I needed to nest the User Feedback conditional inside of the "between -100 and 100" if part.

Also:
I'm not sure I understand while loops or the random function at this point, but I'm pretty sure we're going to go over those things in more depth later, so I'm not too worried.
