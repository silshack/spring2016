---
layout: post
author: JayYang95
title: Jay's MOAR Dictionary Exercises"
---

Exercise 1:
<iframe src="https://trinket.io/embed/python3/81f2804330" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercises 2-5:
<iframe src="https://trinket.io/embed/python3/b46a041894" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection 1:
This was a simple enough exercise. I did run into an annoying bug where if the user entered in blank spaces, the program would check if the blank space was in the dictionary and then check if the prompt of the input() function was in the dictionary. I think I fixed this by just calling input() if the user's input was blank. The bug probably had somehting to do with a new line.

Reflection 2-5:
These were all straightforward and easy to solve with the mighty power of regular expressions. I opened the file and stored its .read() into a variable so that I could use .findall() on the variable to search for whatever the exercises specified for and store it into a list. I itered through the list and added them to a dictionary.
