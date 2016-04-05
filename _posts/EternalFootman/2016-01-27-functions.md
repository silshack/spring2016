---
layout: post
author: EternalFootman
title: "Kit's Functional Turtles"
---

<iframe src="https://trinket.io/embed/python/ecb44ac508" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This is an extension of my logical turtles excercise. The first function is below.

```
def daisy():
  alice.forward(20)
  alice.fill(True)
  alice.fillcolor("yellow")
  alice.circle(5)
  alice.fill(False)
  alice.back(20)
  alice.left(90)
  alice.forward(20)
  alice.right(90)
```

This actually streamlines the code a little; it plugs into a while loop which lets the user decide how many daisies to draw.
I had some trouble coming up with a place for the second function; nothing else in this story is appropriately repetitive. It ended up being a needless bit of antagonistic user interaction.

```
d = raw_input("How many feet deep do you suppose this rabbithole is?")
def rabbithole(d):
  e = int(d) + 12
  return e
c = rabbithole(d)

print "Your depth perception is dreadful. It is actually ",c," feet deep."
```

I'm not sure the code is correct, but it seems to work.