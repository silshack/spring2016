---
author: izayak
title: "Ruotong's Treasure Hunt Turtle"
layout: post
---

Here is the embedded link from Trinket:
<iframe src="https://trinket.io/embed/python/8ea9579e8d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Problems encountered:
1. Distance between two points' representation in Python [solved]
http://stackoverflow.com/questions/5228383/how-do-i-find-the-distance-between-two-points
There are two ways: 1) use a specific function called 'hypot' 2) directly use the Pythagorean theorem with 'sqrt' function.
Do not forget put 'math.' before 'sqrt'. https://mail.python.org/pipermail/tutor/2002-March/013249.html
2. String and variable print at the same time [still have question]
http://stackoverflow.com/questions/17153779/how-can-i-print-variable-and-string-on-same-line-in-python
There is one way like this: print "If there was a birth every 7 seconds, there would be: {} births".format(births). I tried, but this did
not work.
3. Round function [solved]
https://docs.python.org/2/library/functions.html#round
