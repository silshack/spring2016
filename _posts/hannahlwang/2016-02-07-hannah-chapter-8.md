---
layout: post
author: hannahlwang
title: "Hannah's Chapter 8 Exercises"
---

<b>Exercise 1</b>

<iframe src="https://trinket.io/embed/python/e7abe245c3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In this exercise, you had to create a function called 'chop' that deleted the first and last elements of a list and returned 'None'. If you specify 'return t' in your function, it prints the middle section of the list that was not deleted. However, when you take this out, the function still works, but it print 'None'. I'm still not entirely sure what 'None' means in this context, though.

<b>Exercise 2</b>

<iframe src="https://trinket.io/embed/python/19bf3262e0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This was an exercise in debugging and guarding. This was a little difficult for me, because it seemed like there were many potential lines of code that could cause it to fail, depending on the text file. However, I decided that the most problematic one was 'print(words[2])', because there is nothing checking whether the word in the 2th position was a day of the week. I made the code fail by adding 'From' to the beginning of line 61 in the text file. This made the program return 'automatic' among the list of days. I solved this by creating a list 'days' with all the possible days of the week, and adding another 'if' statement using 'not in', which I learned from the chapter in Automate the Boring Stuff.

<b>Exercise 3</b>

<iframe src="https://trinket.io/embed/python/d9e0f683ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this exercise, I essentially combined all my 'if' statements into one 'if' statement, using 'and'. I also made all of them 'negative' - '==' became '!=' and 'not in' became 'in'. If all of these statements were true, it would print the word in the 2th position.
