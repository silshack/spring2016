---
layout: post
author: hannahlwang
title: "Hannah's Game App"
---

<h3>Game App</h3>
<em>For best results, view in fullscreen</em>

<iframe src="https://trinket.io/embed/python/ed84a4ac97" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<h3>Revise Milestones</h3>
- [x] create screen setup with three buttons on the left side, one button on the left side (for display of computer's choice), and the score at the top
- [x] import images for RPS icons
- [x] create clicky function for user choice
- [x] create random function for computer choice
- [x] create capability for app to determine which value is greater - if statements using "and"
- [x] create counter to keep track of score
- [x] create screen clear
- [x] create win screen (one option in loop, in if statement)
- [x] create lose screen (other option in loop)
- [ ] allow user to start over

<h3>Reflection</h3>
This app was much harder than I had anticipated! The first 4 milestones were pretty simple and straightforward, and I had them figured out by the end of my first day of work. I had a problem for a while with getting the computer to choose a different random shape every time. I finally realized that this was because I had defined "computerShape" outside of the "oneTurn(x,y)" function, which caused it to call the same shape every time the user clicked. This revelation meant that I had to move around a lot of pieces of my code. Originally I had also called the scoring system outside of the "oneTurn(x,y)" function, but this had to be moved around and slightly adapted in order to work with the new placement of "computerShape". I was pretty pleased that I was able to track the userShape, using a return for playerChoice(x,y). This meant that I could compare computerShape and userShape in order to assign points to either side.

The one lingering bug in my program is the "enter to play again" button. For some reason, after the user presses enter to restart, that button pops up on the screen again. If the user presses enter again, THEN the button goes away. I have no idea why this is happening! 

Overall, I'm pretty pleased with how this app turned out. I'm obsessive about aesthetics, and I'm happy with the way that it looks. I can't say that it's very much fun to play... Since the computer randomly generates its choice each time, there's no strategy involved. If I understood game theory better, maybe I could have made a smarter computer and a more enjoyable game. But I'm happy that it works the way that I want it too!
