---
layout: post
author: nataliele
title: "Natalie's Chapter 5 exercises"
---

Even though we havent covered lists, I feel it's impossible to finish the exercise without them so I had to consult stackexchange.

For exercise 1, I got the list and append code from stackexchange. After that it is pretty straightforward.
<iframe src="https://trinket.io/embed/python/125846c8b7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For exercise 2, I quickly figured out it is not as easy as it seems. When I tried a series with a double digit number, the program doesn’t recognize that it's a double-digit number. Then I realized that I have to convert the string of user input into numbers. Which means I have to delimit the user input first and then convert it to number. I got the codes from stackexchange. 
<iframe src="https://trinket.io/embed/python/4e9dec13ca" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For exercise 2, after delimiting, the series doesn’t become a list. It looks like 1 when printed out:
print(userinput)
['3', '4', '5', '6']
print(userinputfloat)
[3, 4, 5, 6]

Also this code to change from string to text using for i 
userinputfloat=[int(i) for i in userinput]
looks different than the one we learnt in the textbook? Previously I used to use "for i in range(3)" for example, what is the difference when using "range"?
