---
layout: post
author: ericabrody
title: “Erica's strawberry game"
---

The game:
<iframe src="https://trinket.io/embed/python/b21ac85c5f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Milestones:
 - [x] create modes for easy/hard mode
 - [x] easy mode works with screen clicks
 - [x] hard mode works with arrow keys
 - [x] Put the instructions at top of screen and leave them there - along with Level and Score
 - [x] Find or draw berry, person, person with berry, basket
 - [x] Setup screen - background  = green, place 5 berries in random places, create/place basket 
 - [x] Set initial default score and level, Score = 0, Level 1
 - [x] Allow person to move around screen with arrow keys.
 - [x] Allow person to move around screen by clicking on screen
 - [x] Create code to define an intercept between person and berry and intercept of berry and basket
 - [x] berry has to disappear when get to basket
 - [x] change picker image to be picker with berry 

When berry intercepts basket, 
 - [x] Change state of basket - like color flip for 10 times w - 
 - [x] Increase score by 1 point
 - [x] berry disappears and change image back to person only (from person with berry)
 - [x] Allow berry and person to move together toward basket OR change image once berry and person intersect

Stretch goal: Level 2 of game
 - [ ] reset screen with 10 berries available to pick
 - [ ] create bird object that moves around screen 
 - [ ] if bird intercepts with person who has berry, bird takes berry

Reflection:
Coding this game required taking a lot of breaks to come back and troubleshoot problems. I created a little starter code to help outline
some of the tasks to be done in the Trinket. I built the program using a modular approach. Specifically, I built setup and then got it debugged. Then built other pieces. I realized i had a turtle named setup and a module called setup and i think that may have caused problems, so I renamed the module. Initially, the program was just going to have one mode, moving around with keys. To satisfy the requirement that the game respond to keys, I created a second mode where the user moves around the screen with clicks.

My Writer class evolved while I was programming - I realized that I had to keep telling the turtle where to go to before writing and keep changing penup and pendown, so I just put those items into the write_me method in the Writer class, to make the programming faster and easier. This brought me great satisfaction.

Building the intercept code was challenging. I was not sure whether to call the intercept checking methods on Picker or berry or basket. Ultimately, I chose picker so it could be used with berry or basket. As I got into programming this, I realized that I had to track more state in the game that I may have wanted to track. Since I created the 2 game modes, I left out my stretch goal of game level 2.
