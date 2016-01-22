---
layout: post
author: hannahlwang
title: "Hannah's logical turtle"
---

Tina makes a bouquet of balloons!

<iframe src="https://trinket.io/embed/python/28c80d3d0a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This program is deceptively simple. It asks you to enter a number between 20 and 60, and uses that for the circle value for the main part of the balloons. The "tail" part of the balloon is also calculated from this input value, so that all parts of the balloon scale correctly. Additionally, the x and y coordinates of each balloon are calculated based on this input value.

The program also has a couple nested conditionals. The first one asks for a whole number between 20 and 60, and if you enter a string, a float, or an integer outside the range, you will get a corresponding error message. Inside this conditional, there is a loop that repeatedly asks you "what's the magic word?" until you say "Please" or "please".
