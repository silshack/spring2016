---
layout: post
author: jamesma560
title: "James' Refactored Turtle Exercises"
---

Original robot program:

<iframe src="https://trinket.io/embed/python/0b6bd5bf80" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Refactored robot program:

<iframe src="https://trinket.io/embed/python/73b047ab64" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Original treasure hunt program:

<iframe src="https://trinket.io/embed/python/0216c31ed3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Refactored treasure hunt program:

<iframe src="https://trinket.io/embed/python/8d171ab9bb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


By far the biggest puzzle for me was satisfying the return stipulation. In my treasure hunt program, I wanted to refactor my code in a 
way that defined the part of the code where an x and y treasure coordinate is randomly selected as it's own function. For that to be 
any use however, I knew that I needed to return and x and y coordinate, but I wasn't sure of how to do it. On my first attempts, whenever
I tried using the returned variables later in the script, I would get an error saying that the intepreter didn't recognize them. After Googling
around, I ended up learning that if you want to use returned function variables as variables, you have to "unpack" them. That is,
use a statmemt like this: variable_1, variable _2 = some_function() where some_function() returns 2 variables. As I said in my other
reflection, I'm glad we are building on prior work and I look forward to making both of these programs better because I think they 
could use a lot of improvement. 
