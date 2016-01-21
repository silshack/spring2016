---
layout: post
author: wagerpascal
title: "Jason's Turtle Logic"

---

<iframe src="https://trinket.io/embed/python/5bc9bc9035" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I revisited my polygon program as I felt there were more things I could change. The main changes are that there is now a "try/except" case where an error message is outputted in the case of a bad input.
In addition, two conditionals were added:

```
boardcount = int(raw_input("How many boards would the Mongol horde hoard, if the Mongol horde could hoard boards?"))
  
  if boardcount % 2 == 0:
    chair.fillcolor("blue")
  else:
    chair.fillcolor("red")
```

This part was added as a test for even/odd numbers by using the modulo operator. I thought it was a nice challenge in which to determine the easiest way of doing so.

In addition, I added:

```
desptimes = raw_input("Is your drawing full of determination?")
  if desptimes == "yes" or desptimes == "Yes":
    chair.speed(10)
```

For this section, I investigated if strings are able to be compared as they are for conditional statements. If the user decides that their drawing needs to go faster and input "yes" or "Yes", the drawing proceeds at the maximum possible speed.
Something initially went wrong, however. I initially tried to set up a fill-in-the-blank question with a similar answering system; however, the ending result would have changed the background color. However, it never ended up working... it may be due to the Screen().bgcolor("") function, but I'll have to look into it later.
Working with strings so much was a little tricky for me, especially as I had no clue if I even could compare them in a manner similar to numbers. On a side note, using "is" may be able to get similar results, but there are minor differences (namely it can differentiate how two strings were constructed).

