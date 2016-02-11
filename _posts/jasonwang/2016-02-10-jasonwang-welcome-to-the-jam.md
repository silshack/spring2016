---
layout: post
author: wagerpascal
title: "Come On and Slam"
---

<iframe src="https://trinket.io/embed/python/84966596b1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Very similar exercise to to set up as the chapter 8 in-class exercises initially.
The While loop takes a string and initially compares if it is the "done" command. If not, it adds the string to a list. From there, it adds each part of the list to a new string, where it is stripped and printed as an intact, combined string.

The only thing I could not resolve is the little space that precedes the printed phrase. A minor formatting issue, but I couldn't fix it.

I was curious afterwards and looked for a method that could to a similar job, and found stringname.join(list). Interestingly, each example uses a dash to mark boundaries between each string.
http://stackoverflow.com/questions/12453580/concatenate-item-in-list-to-strings-python
