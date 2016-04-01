---
layout: post
author:
  - touchwick
  - jamesma560
title: "James and Ian's Regex Exercises"
---
This is exercise 3, which we completed together:

<iframe src="https://trinket.io/embed/python3/323ceeff04" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Our most significant issue here was formatting the regex correctly. After working with Python for the last couple of months, working with regex feels foreign in a way I don't think we'd anticipated. This leads us to Exercise 2, which Ian completed:

<iframe src="https://trinket.io/embed/python3/254570144b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It did not take that long to complete the code. Bits and pieces of it worked quite well right from the get-go. The issue was, again, formatting the regex. For whatever reason, when the numbers were appended to the list from which the mean would be determined, the brackets were appended as part of the item. Stripping those out was an immense pain, but it does work now. This is absolutely a case in which there is very likely a simpler way for us to do this, but! It works now! Which is fantastic! 

This is Exercise 1, which James completed:

<iframe src="https://trinket.io/embed/python3/dbc8f34ddd" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

This does work, in that it finds the phrase the user enters inside the line indicated. It does, however, interpret any portion of a regex phrase as part of the string to be found. We can't figure out why it does this, especially given that Exercise 3 does interpret the commands correctly. Ultimately, though, we think this is a minor bug, considering that the code does us a regex method to find the given string.
