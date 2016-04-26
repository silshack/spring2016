---
layout: post
author: JayYang95
title: "Jay's Project Update 3"
---

<iframe src="https://trinket.io/embed/python/7bd48e1a72" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

To do list from last week:

 - [x] Manage states of turtles to allow a restart function to be easily implemented
 - [ ] Put the text file I created to use
 - [x] Use the rest of my dictionary
 - [ ] Create collectible turtles
 - [x] Check for collisions
 - [ ] Restart function
 - [ ] Beating a level restarts the game with updated gamesettings (more enemies, more difficult)
 - [ ] Make "Help" button print something helpful
 
While creating the enemy turtles, I had a problem getting the pause/resume function to get the enemies to stop moving but found out I was using a variable from my variables module incorrectly. Now, the pause/resume is fully functional. I also implemented a collision check as well as player lives (3 to start with). At first, colliding with an enemy turtle would take away several lives because collision is called everytime tina moves, which is a lot when you hold down the movement key. To fix this, I gave the user a short frame of invincibility upon impact and now the lives are functioning properly. Although there are quite a few things left to do, I think I've finished most of the hard part so the rest shouldn't take too long to code.
 
Last goals:
 - [ ] Use text file
 - [ ] Make collectible turtles
 - [ ] Restart function
 - [ ] Increase level/difficulty after winning
 - [ ] Print help dialogue
