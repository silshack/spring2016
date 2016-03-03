---
layout: post
author: ericabrody
title: "Erica's Game Milestones "
---
Premise of game: 
To get points, the player uses the keyboard to move around and pick up berries around the screen and put them in a basket at the top right-hand corner of the screen. Player gets 1 point for each berry. Level 1 will have 5 berries on the screen to get in the basket. At the end of Level 1, there will be a win screen. I hope to get to a second level where there is a bird that moves around randomly, and if the bird intersects the player, then the bird takes the berry and the player misses that opportunity for a point.

Priority: Develop nice user interface

Milestones
 - [ ] Put the instructions at top of screen and leave them there - along with Level and Score
 - [ ] Find or draw berry, person, person with berry, basket
 - [ ] Setup screen - background  = green, place 5 berries in random places, create/place basket 
 - [ ] Set initial default score and level, Score = 0, Level 1
 - [ ] Allow person to move around screen with arrow keys.
 - [ ] Create code to define an intercept between person and berry and intercept of berry and basket

When berry intercepts basket, 
  - [ ] Change state of basket - like color flip for 10 times w
  - [ ] Increase score by 1 point
  - [ ] berry disappears or change image back to person only (from person with berry)
  - [ ] Allow berry and person to move together toward basket OR change image once berry and person intersect

Stretch goal: Level 2 of game
 - [ ] reset screen with 10 berries available to pick
 - [ ] create bird object that moves around screen 
 - [ ] if bird intercepts with person who has berry, bird takes berry
