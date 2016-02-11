---
layout: post
author: hannahlwang
title: "Hannah's Chapter 6 Exercises"
---

<b>Exercise 1</b>

<iframe src="https://trinket.io/embed/python/cf830f9efb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this exercise, you just had to take the code <a href="http://ils.unc.edu/~eah13/textbook/06-strings.html#for">here</a> and adapt it to go through the string from end to beginning, rather than beginning to end. This required starting the index at the end, changing the "while" loop to work while index>=0, and have it traverse the string backwards.

<b>Exercise 3</b>

<iframe src="https://trinket.io/embed/python/8554c9d69e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here, you had to take the code <a href="http://ils.unc.edu/~eah13/textbook/06-strings.html#counter">here</a> and turn it into a generalized function that takes two arguments. My two variables were 's' for 'string' and 'l' for 'letter'. I essentially copied the original code and replaced 'word' with 's' and the letter 'a' with the generalized 'l'. I realized that I also had to add another variable for the 'for' loop, to stand in for 'letter', so I used 'ltr'.

<b>Exercise 4</b>

<iframe src="https://trinket.io/embed/python/ce3eedf718" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

At first, I wasn't exactly sure how to implement this string method. After some trial and error, I realized that I just had to define 'str' and 'sub' as the word and the letter, respectively, and that the 'start' and 'end' arguments were unnecessary for this implementation.

<b>Exercise 5</b>

<iframe src="https://trinket.io/embed/python/6a089634e0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this exercise, I used 'find' to find the colon in the string, which I defined as 'x'. I was then able to use x as an index number to do string slicing. However, the string slice had to start 2 positions after the colon, so I used 'x+2' to start the slice, and had it go to the end of the string.
