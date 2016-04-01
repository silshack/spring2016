---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Logical Turtle Exercises"
---

  For me, this was probably the most challenging assignment that we have done so far for this class.  The hard part wasn't so much not 
understanding the code we'd learned as it was compiling everything into one program and trying to figure out how to fit the different 
pieces together. From this exercise, I discovered that I'm better at focusing on one specific area (for lack of a better word) of code
at a time, but this task challenged me to think about how programmers might actually work with the code to make productive output.

  As for actually creating my Trinket, I (for once) didn't look up any code to make different shapes that I'm so fond of.  Instead, I 
played around a little bit to try to create a peppermint shape.  This didn't work so well at first...I tried do small semicircle curves,
but I discovered that I should probably just save that battle for another day.  I kept things simple and decided to create a circle with a few
different divisions inside it to give it a peppermint effect without the curved swirls in the middles.  This is the code that I came up
with to make circles with divided sections:

```
  tina.penup()
  tina.forward(100)
  tina.pendown()
  tina.color("red")
  tina.circle(50)
  tina.left(90)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right (90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right (90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(135)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
```
It's really long, but to be honest, it was just a lot of copying and pasting the code that I'd already written and figuring which angle
Tina was positioned. Overall, this made a pretty satisfying peppermint.

The conditional that I incorporated into my Trinket was based on the number of peppermints that the user chose to "eat," but the catch
was that they couldn't eat more than 3.  After all the peppermints were drawn on the screen, they disappeared to simulate the eating 
process.  Here is a sample of the conditional that I used (to avoid making the post too long, I pasted from the conditional if the user
selected the 2 option):

```
elif int(peppermints) is 2:
  tina.penup()
  tina.forward(100)
  tina.pendown()
  tina.color("red")
  tina.circle(50)
  tina.left(90)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right (90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right (90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(135)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)

  
  tina.penup()
  tina.goto (-100,-50)
  tina.pendown()
  
  tina.color("green")
  tina.circle(50)
  tina.left(90)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right (90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right (90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(135)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  tina.right(180)
  tina.forward(50)
  tina.right(90)
  tina.forward(50)
  
  tina.reset()
```

One of the areas that I had difficulty of thinking where to put it into the Trinket were the operators, so for lack of any better idea,
I decided that we would calculate the calories of peppermints.  I wish I could have thought of something more creative, but it served
the purpose of this task.  Here's how I set up my equation:

```
print("They're all gone! Looks like someone was hungry!\n.")
  eat = raw_input("Remind me how many peppermints you ate?")
  if int(eat) is 3:
    calories = int(eat)*2
    print("Since there are 2 calories for each peppermint and you had" + " " + str(peppermints) + ", you have consumed" + " " + str(calories) + " calories. You should eat more peppermints.") 
  else:
    print("I know you're lying! Now we have to start from the beginning..")
```

One of the hardest parts for me is remembering to put the str before variables in the print command, but in operational equations making
sure these are either int or float.

This was a pretty fun task once I figured out which direction I wanted to go.  One thing that I think would be interesting to learn (
and maybe I already had the ability to do it and didn't know) was how to set the program back to the beginning if the user entered a
value that was not a part of the conditional I created.  

Here's is the code for my full Trinket:
<iframe src="https://trinket.io/embed/python/fe6d9480e5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
