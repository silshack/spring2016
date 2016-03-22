---
layout: post
author: wagerpascal
title: "Jason's Files Exercises"
---

Exercise 1:
<iframe src="https://trinket.io/embed/python/c13b32f7ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 1 was pretty similar to the Exercise 8 question that we also had to do with the mbox text files, minus the need for splitting 
the lines into individual strings (overall counterproductive to take apart strings, just to put them back together again). However, it 
is possible to apply the ".upper" method to each string to put them into all caps.

Exercise 2:
<iframe src="https://trinket.io/embed/python/5f0f78a0ee" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

One of the examples in the reading showed that there's a ".startswith" method that looks for lines that begin with the inputted string.
Therefore, I used this to filter for lines that begun with "X-DPSAM-Confidence", and split apart the resulting lines to isolate the 
numbers. After that it's just a matter of calculating the averages. It was enlightening to learn of the .startswith method.
Also, at first, I accidentally split the lines one level too deep (at the words level), so I ended up isolating individual characters.

Exercise 3:
<iframe src="https://trinket.io/embed/python/6371471219" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Fairly straightforward, as it only needed an if/else conditional to separate the cases. Though one strange thing- my print statement
differs from the original example as the commas carried over when I ran it. I still haven't really figured out why though.

Exercise 4:
<iframe src="https://trinket.io/embed/python3/fcaed28a4a" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It was tricky getting a grasp of the lists of lists' properties (especially the fact that breaking apart the list gives entire rows
that are able to be indexed theselves). It's overall a lot closer to human thinking that I initially thought (I thought that the 
"rows" were equivalent to pointers, rather than the whole row itself).
