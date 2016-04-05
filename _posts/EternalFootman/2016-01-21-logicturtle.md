---
layout: post
author: EternalFootman
title: "Kit's Logical Turtles"
---
This is the first scene of "Alice In Wonderland" with turtles. Enjoy.

<iframe src="https://trinket.io/embed/python/ecb44ac508" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I'm looking forward to learning loops as I'd like to have the user decide how many flowers are drawn.
Here is the existing code:

```
alice.goto(140,0)
alice.pendown()
alice.goto(140,20)
alice.fill(True)
alice.fillcolor(flower)
alice.circle(5)
alice.fill(False)
alice.penup()
```

I'd like to have a relative direction instead of a coordinates; then it can repeat as often as I like (using conditionals to keep it within reason).

I'd also like to see if strings can be used with conditionals to eliminate the number versions of yes and no. Here is my solution until I can do that.

```
z = raw_input("Should Alice follow the rabbit? Type 1 for yes and 2 for no.")
if int(z) == 2:
  print("How dreadfully unadventurous. She'll just stay in the meadow forever, then. I hope you're happy.")
elif int(z) == 1:
  alice.goto(100,-100)
  alice.hideturtle()
else:
  print("You had one job. Now the universe is frozen in indecision.")
```

Finally, I'm not sure how to go back to the question if the answer doesn't work.
Apart from these issues, I enjoyed this program very much. Perhaps I'll design the whole book.
