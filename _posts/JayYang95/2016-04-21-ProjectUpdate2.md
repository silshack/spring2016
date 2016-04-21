---
layout: post
author: JayYang95
title: "Jay's Project Update 2"
---

<iframe src="https://trinket.io/embed/python/b407498747" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Goals for Thursday:

 - [x] Functioning pause/resume
 - [x] Have a text file containing settings
 - [x] Create a dictionary of game states (current level/difficulty, # of lives, # of enemies)
 - [ ] Cleanly manage states of turtles so that restart function can reset these states
 - [x] Add more enemy turtles
 
I didn't have much time since Tuesday to work on this, but I have managed to get the game so far to pause/resume by pressing "P". I have also created a text file with some settings for each level, though the file itself is not in use yet. I have also created a dictionary to manage game states including level, lives, and number of collected items, but only the "level" key is being used currently to determine how many enemies to spawn and I have created more enemy turtles. So far I feel like the milestones I have set are reachable.

To do list:

 - [ ] Manage states of turtles to allow a restart function to be easily implemented
 - [ ] Put the text file I created to use
 - [ ] Use the rest of my dictionary
 - [ ] Create collectible turtles
 - [ ] Check for collisions
 - [ ] Restart function
 - [ ] Beating a level restarts the game with updated gamesettings (more enemies, more difficult)
 - [ ] Make "Help" button print something helpful

Stretch goals:

 - [ ] Improve enemy random movement
 - [ ] Power ups
 
Possible changes:

 - [ ] Spawn each enemy in set location rather than at random
