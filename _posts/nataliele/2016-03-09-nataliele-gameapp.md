---
layout: post
author: nataliele
title: "Natalie's game app"
---

Milestones:
 - [x] Screen background
 - [x] import shark image
 - [x] multiple sharks appears
 - [x] multiple sharks move horizontally 
   - [x] at different locations
   - [x] in different directions
   - [ ] sharks move to edge of screen then bounce back
 - [x] if Tommy touches a shark, Tommy loses 1 life
 - [x] if Tommy touches a treasure, count increase 1 point
 - [x] After collecting all treasures, Tommy can go to Tina to be reunited
Code:
 - [x] functions are separated in different modules
 - [x] codes are commented
 - [x] uses custom class

<iframe src="https://trinket.io/embed/python/9808eda78f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

There were so many problems that I encountered with this game app. The first obvious one is that the program is very slow to start up. I thought its because it's waiting to draw the background then show it but I did set the speed to 0 so I have no idea why it's like that. I spent quite a bit of time to figure out how to move the sharks to the edge and then bounce back and was able to make it work. However, that function seems to take over the program and I wasnt able to use onclick or onkey to navigate Tommy at all. So, bummer... Another thing that I couldnt figure out was when Tommy is stationery and a shark moves onto him, the distance command doesnt get executed. I tried putting it outside the onclick function and inside the shark's move() function but it still doesnt work.

Another major problem I had was this error. For some reason I couldnt import Tommy or some other variables into some modules. I also couldnt import anything from the main module. I wonder if I'm doing anything wrong?
![Game](http://nataliele.web.unc.edu/files/2016/02/game.png)

When I tried to use reset for example `myscreen.reset()` but even if I do `setup()` afterwards it still doesnt set things up right and just messes everything up.
![reset](http://nataliele.web.unc.edu/files/2016/02/reset.png)

I still have problem with global/local variables. I have no idea why this happened.
![reset](http://nataliele.web.unc.edu/files/2016/02/variable.png)

So because of all these problems, I have scaled down my milestones considerably. I think what I'm satisfied with this app is that I was able to use class to simplify and streamline a number of repetative things like writing messages, creating sharks etc.



