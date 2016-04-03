---
author: wookiemage
layout: post
title: "Colin's Clicky Turtle"
---
## Here\'s my turtle:

  <iframe src="https://trinket.io/embed/python/79598a49b9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
  
  
  I had a hard time figuring out what I wanted to do with this one. And really, it still isn\'t great but it meets the requirements.
  I approached this one function at a time. First I made the setup function draw a sun. Then I took that sun drawing code block and turned it into it\'s own helper function.
  Having set up the screen, I decided to keep things simple by having my onclick function use my newly made sun drawing function.
  Next I needed to have Tina react. So I had her move to the opposite quadrant of wherever the sun was drawn and change colors based on which quadrant she is in. This doesn\'t really have any significance for the user: she just changes colors because she needed to do something.
  When that was all working, I needed a win condition, so I set a comparison using distance from the sun. If she\'s far enough away, you win.
  Finally, I shortened the congratulate function (by having the loop repeat fewer times) and then offered the player the chance to keep playing.
