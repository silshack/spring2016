---
layout: post
author: jamesma560
title: "James' Poetry Slam Turtle Exercise"
---

Poetry Slam Exercise:

<iframe src="https://trinket.io/embed/python/b08f09ad58" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

This exercise was pretty straightforward. The only thing that annoyed me was how
to make Tina write multiple lines of poetry in a poetic way, with each
line of poetry actually being on a seperate line. At first I tried this:

count = 0
for line in poem:
  tina.goto(0, count - 10)
  tina.write(line)
  tina.penup()
  count = count + 1
  
Where "poem" is my list of poetic lines from the user, but no matter what I tried Tina would just end up writing
the lines of poetry over each other. So I ended up just doing a simple tina.write(poem). 
Although it prints it all on one line at least it's readible.I've had this problem before (getting Tina to write multiple lines 
of text on different lines) so I'd be interested in techniques on how to do this. 

