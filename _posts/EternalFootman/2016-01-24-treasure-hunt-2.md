---
layout: post
author: EternalFootman
tite: "Kit's Treasure Hunt"
---

<iframe src="https://trinket.io/embed/python/daedf07389" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Working out effective formulas took some time, and I'm certain that mine are not the most efficient possible. For example:
```
(int(user_x) >= int(treasure_x) + 75 or int(user_x) <= int(treasure_x) - 75) and (int(user_y) >= int(treasure_y) + 75 or int(user_y) <= int(treasure_y) - 75):
```
Technically the game works, but there are holes where one coordinate is close but one is not; then the program just asks for more without giving feedback. A solution would involve many more formulas or an entirely different approach.
One early problem was that I hadn't ordered them from smallest to largest, so the program took the first true statement and never got as far as winning.
Another was that try/except is the only way that seems to work for filtering out letter input when an integer is needed. Is this correct?

I've been working out some kinks in my Alice in Wonderland program (previously Logical Turtles); the while function solved most of the issues, but a few remain.
I was terribly excited to make this bit work:
```
bad_daisies = True
while bad_daisies:
  try:
    flower = raw_input("How many flowers are in the meadow?")
    if int(flower) <= 2:
      print("That is not enough to be useful.")
    elif int(flower) > 18:
      print("Who are you, Miss Rumphius? Go, and take your invasive species with you.") 
    elif int(flower) > 2 and int(flower) < 18:
      for flower in range (int(flower)):
        alice.forward(20)
        alice.fill(True)
        alice.fillcolor("yellow")
        alice.circle(5)
        alice.fill(False)
        alice.back(20)
        alice.left(90)
        alice.forward(20)
        alice.right(90)
        flower = int(flower) + 1
        bad_daisies = False
  except:
    print("That makes no sense in this context. Please enter a number.")
```
However, this is less effective:
```
grass_color = True
while grass_color:
  grass = raw_input("What color is the grass at this time of year?")
  try:
    myscreen.bgcolor(grass)
    grass_color = False
  except:
    print("That is not an acceptable color. Consult a botanist if you must.")
```
I'm attempting to tell the program to loop if the input is not a recognized color, but I'm not sure how best to do that. Experiments with 'class(grass) = color' proved ineffective.
