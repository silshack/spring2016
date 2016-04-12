---
layout: post
author: jamesma560
title: "James Chapter 13 Exercises"
---

<iframe src="https://trinket.io/embed/python3/147f63c5ca" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

The tricky part about this assignment for me was how to navigate the JSON that the starter code left for me to work with. As with many of these
assignments, the key to figure out how to work with the JSON is to pinpoint exactly what data types I was working with. By simply printing
the JSON out to the console, I easily got lost in all the brackets and curly braces. But with the handy type() function, I was able to understand
that I was working with a dictionary of lists. And to access anything that I wanted to display in order to complete the assignment, I basically
had to follow this pattern: [key][index][key][index].

Now although my code works for most situations, for a few special inputs that I put into the program, it ended up getting the county and 
state wrong. For example, when I input the string "Chapel Hill, NC", the script lists the state as Orange County and the county as Chapel
Hill. At first, I thought that it was because Chapel Hill contained two words (most of my one word cities seemed to work fine, except Charlotte). However, 
when I used an example like Santa Clara, CA, the script worked correctly. Very interested to see what the solution is.
