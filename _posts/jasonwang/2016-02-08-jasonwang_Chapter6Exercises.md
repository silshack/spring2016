---
layout: post
author: wagerpascal
title: "Jason's Chapter 6 Exercises"
---

Exercise 1:
<iframe src="https://trinket.io/embed/python/fe79e56f35" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I learned that it is possible to index a list backwards through a negative system (where the letter right before the last one is -1, the second one -2, and so on).
I was playing around with slices when I came across the double colon method [start:end:step]. -1 as a step can be used to indicate direction from the back. From here it is clear: [::-1] has both last letters and start letters as the end points (blanks indicate keep running until the end), while -1 indicates negative direction.
A counter is used to keep track of the length of the word.

Exercise 3:
<iframe src="https://trinket.io/embed/python/2351569a69" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The design of this counter involves splitting the string into a list of "letter", where each letter is compared to the specified "char". Like the first exercise, if a hit is made, then the counter increments.

Exercise 4:
<iframe src="https://trinket.io/embed/python/97ed404465" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Rehash of exercise 4 using the stringname.count(desired_character) function. It is nice to know that a specific function exists for this application.

Exercise 5:
<iframe src="https://trinket.io/embed/python/2d3ba69d10" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

As there is only one case of "0" in the string at the beginning of the desired number, the .find method can be used to separate the number. As the number is also the last object of the statement, the rest of the string can be sliced out of the string without any issue.
The float function can be used directly after slicing the numerical string out, and was tested by running a quick calculation to prove it (if it remained as a string, it would have equaled "0.84750.8475", rather than 1.695.
