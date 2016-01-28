---
layout: post
author: wagerpascal
title: "Jason's Chapter 4 Exercises"
---

Exercise 6:

<iframe src="https://trinket.io/embed/python/2ae2751ceb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Fairly straightforward, except that when running the function, the initial variables should be determined before the use of the function, requiring the placement of the user inputs outside of the function (but before the intialization of the function).

Exercise 7:

<iframe src="https://trinket.io/embed/python/c80cda6ba5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Similar setup to that of Exercise 6, but I initially was having issues with the "except" case for non-numerical inputs (I was getting error messages). However, I realized it was because I had removed the float() function away from the "try" case, and therefore was unable to connect to "except".
