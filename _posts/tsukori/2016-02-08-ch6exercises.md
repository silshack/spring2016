---
layout: post
author: tsukori
title: "Ch.6 Exercises"
---

Exercise 1: 
<iframe src="https://trinket.io/embed/python/2ecbaa45e4" width="80%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise the rest: 
<iframe src="https://trinket.io/embed/python/569e4010ba" width="80%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection: I wanted to make the code easily readable so I declared length as a variable to use in the while loop

```
length = len(input)
while index < length:
    #prints string from end to front
    letter = input[length-1]
    print(letter)
    #increment/decrement
    index = index + 1
    length = length - 1
```

resulting in:

```
Please enter a string: hello
o
l
l
```

but instead it made the code only print out the string in reverse until index and length became the same value... So I just chucked that idea and went back to using len(input) in the while loop. The other problem I ran into was getting the first counter to count the instances of the letter you were looking for and not the entire string, but then I realized I left out an if statement and that fixed the problem. Python is pretty cool in the way you can splice a string, Java doesn't handle substrings nearly as well. 
