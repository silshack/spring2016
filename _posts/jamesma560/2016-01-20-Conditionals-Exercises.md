---
layout: post
author: jamesma560
title: "Chapter Three Conditional Exercises"
---

Exercise 1: 

<iframe src="https://trinket.io/embed/python/23a034452d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 2: 

<iframe src="https://trinket.io/embed/python/f462b9650d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 3: 

<iframe src="https://trinket.io/embed/python/9abc798028" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection

I learned a lot this week from these exercises. For one, as I alluded to in a previous reflection, I was frustrated by the fact that it had taken me two steps
to accept a user's input and convert it into a floating point number. But in tinkering around for this exercise, I learned that if you nest the two necessary functions for this task like so, float(raw_input("Prompt: ")), you can do it in one line. 
In fact, I learned that it was much, much simpler to set up a try/except error catcher (perhaps even necessary) when you did this in one variable assignment. 

Other tricky things I ran into involved getting the overtime pay right. At first, when I ran my overtime program, I didn't get any errors, but I could tell the 
output was way off (I have lengthy experience calculating possible overtime pay from a past fast food job). So looking back at the code I realized that I was applying the
overtime rate to ALL the hours instead of only to the hours that exceeded the forty mark. In this sense, order of operations and semantic errors were too concepts for the reading
that popped up in this weeks exercises.

And finally, another cool thing I learned is that when building a try/except error catcher, it's useful to just use the reserved word ValueError
as an except stipulation. Through my first draft of the try/except wage program, whenver I would test the "except" by throwing in a string for the first input, 
the program would still go through the superflous step of asking for a second input before displaying an error message. But with my newfound knoledge of ValueError 
(which I found out after seeing it over and over in various try/except walkthroughs on the web), I was able to push the program to display an error as soon as it happened, instead 
of going through the pointless task of asking for another input. 
