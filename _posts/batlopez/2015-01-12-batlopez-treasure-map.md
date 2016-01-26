--- 
layout: post
author: batlopez
title: "Nat's Treasure Map"
---
I seriously struggled with this assignment. The actual strategy as to how to enable the user to win  within 5 pixels was really hard to think through. Initially, I actually defined a treasure area and wanted to see if I could create a list of coordinates that were compared to the coordinates inputted by the user but that became clunky and I had no clue how to search within a list or if that's possible. I ended up using ranges for the x and y coordinates because it seemed like the simplest next step. 
<iframe src="https://trinket.io/embed/python/9f0293a5c1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

One thing that really tripped me up was the loop. I didn't realize that I had to indent everything below it, which in retrospect makes a ton of sense now, but I was stuck there for a long time. One other issue that keeps bugging me is how to return an error message if someone writes in a word instead of a number. I got it to print an error message but the whole program would stop because the subsequent codes called for integers for all the coordinate numbers.
