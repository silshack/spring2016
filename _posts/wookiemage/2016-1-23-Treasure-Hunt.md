---
author: wookiemage
layout: post
title: "Colin's Treasure Hunting Turtle"

---
  Here's my turtle Indiana Jones.
  <iframe src="https://trinket.io/embed/python/0ca2e90164" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
  
  I did run into a few troubles along the way. The first time I tried to evaluate if the Tina was within 5 points of the treasure I ran into quite a bit of difficulty. It seemed like no matter what I did, I couldn't win. I even resorted to having the console print the value of each treasure location so that I could copy it, but when I would get to the right place, it still wouldn't trigger the success animation. So I had a look at my code and realized that at some point I had removed the if user_has_won condition. Woops. That means the user could never win. Once I found that, I was able to win. 
  I also had some difficulty with getting the try and except placed in the right spot. I wrote the rest of my code before putting the Try in. This meant I had to indent everything, which I did poorly. I indented the congratulate(tina) block into the while statement so no matter what coordinates I entered, I won. This took a few trials to figure out as it was possible I was just very lucky.
  I wasn't.
