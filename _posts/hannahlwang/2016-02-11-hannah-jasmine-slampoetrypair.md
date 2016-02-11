---
layout: post
authors:
- ShyArmadillo8
- hannahlwang
title: "Slam Poetry Turtles Pair post"
---

Here is our finalized slam poetry turtle:
<iframe src="https://trinket.io/embed/python/be8514f0ef" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This was a great exercise that allowed us to expand on our initial slam poetry program and work together!  The meat of our program was found in this section of code:

```
 for line in poem:
    count = count + 1
    if len(line) > 38 :
      tina.write(line[0:38], font=("Verdana", 16, "normal"))
      tina.forward(30)
      tina.write(line[39:], font=("Verdana", 16, "normal"))
      count = count + 1
      tina.forward(30)
    else:
      tina.write(line, font=("Verdana", 16, "normal"))
      tina.forward(30)
    if count >= 12:
      time.sleep(3)
      tina.clear()
      tina.goto (-180, 160)
      count = 0
```

The biggest realization for us was that we needed Tina to go through every line of the poem in order to ensure that our spacing
for the program both vertically and horizontally fit on the page.  We accounted for any lines that were more than 38 strings
long and those that were not to make sure that the code was fitting horizontally on the program.  As for the actual vertical
space of the program, we realized that we after twelve lines we needed the program to begin again from scratch. Overall, this
was a good exercise.
