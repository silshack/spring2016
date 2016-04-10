---
author: yiyangshi
layout: post
title: "Yiyang's Web Dictionary Exercise"
---

Here is the program:
<iframe src="https://trinket.io/embed/python3/0d3d96f9da" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

I spent a while writing out the structure of the result to understand where each piece of information is located and how they are embedded in the large list under "result". For this exercise, I first print out the number of locations that are matched. Then, for each location, the detailed address, county, state, country, and postal code is printed. If any pieces of address components is missing, an "NA" will be printed. 

To get the computer to print specific value or "NA" for each pieces of address components, I first created a dictionary to store the available address components(as keys) and its index(as values) for the location. Then, the program will decide if the component I want to print is one of the keys in the dictionary. If yes, the program can use the index (the value of the key) to directly take out the information. If not, the program will print "NA".

At first, I only created a list to store the avaiable address components. Then, each time the program wants to print out a piece of information, it has to read through the whole "result" to find the matching address components and then print out the value. This is very inefficient. 
