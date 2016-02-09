---
layout: post
author: nataliele
title: "Natalie's chapter 8 exercises"
---

Chapter 8 - Exercise 1
At first I tried to use del with indices but quickly realize that list indices must be integers, not object. So I tried loop but the way we refer to items in loop is also by index. Took me some time to realize We can use -1!!!

<iframe src="https://trinket.io/embed/python/1951ebd69a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Exercise 2: So I think if the line starts with "From… or <From etc the program wont return the date on that line. But I feel it's not what this question is getting at...


Chapter 8 - Exercise 3
I tried 
if words[0] == 'From' and len(words) != 0:
at first and got an error with an empty line. The only way there could be an error is that the program never reaches then len(words) != 0 part. I thought Python cant be that weird and it would have to evaluate the 2 terms together. Well turns out Python WILL evaluate first term first and switching the 2 terms solved the error.

<iframe src="https://trinket.io/embed/python/a762692c30" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
