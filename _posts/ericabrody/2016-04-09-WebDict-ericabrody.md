---
layout: post
author: ericabrody
title : "Chapter 13 Exercise"
---

Here is the code:
<iframe src="https://trinket.io/embed/python3/b97e70f95d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
I hit a little bit of lift-off doing this assignment. when my program returned a list instead of an element (i.e., [’result’]), I figured out that I had to iterate through the list of items, so that it would just print the result without the surrounding brackets and quotes. 
Initially, I tried to print specific elements of the address components, but realized that different locations have different numbers of address components and the country might be element number 2 for one location and element number 3 for another location. So I altered the program to pull out the location names and types of all the address components, thus the data drives the number of results returned. This approach also avoids creating any traceback errors. When I trying to iterate through the list of address components,- i found i was trying to iterate first a dictionary and then a list (i.e., not integers), so figured out that i had to create a counter variable that would generate numbers that were iterable. Throughout the process, I was able to troubleshoot and identify errors in my program, such as unexpected indents and missing parentheses, etc.
