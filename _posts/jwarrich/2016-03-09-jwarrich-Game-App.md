---
layout: post
author: jwarrich
title: "Javairia's Game App"
---

Here is the Game App:

<iframe src="https://trinket.io/embed/python/d74c2f6fee" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Reflection:

Originally, what I wanted to do with my game app was create something similar to PacMan. What I ended up creating is something very similar to my original idea but not to the scale that I planned it to be. My game app allows the user to move around the screen using the key and clicks and collect food. The user can click to get close to the food but ultimately needs to use the keys to eat the food. The user wins when they have collected all the food. If they bump into the wall, they lose and their score is shown. What I also wanted to do was have enemy turtles on the screen and if the user touched them, they would also lose. Although I got the enemy turtles on the screen, I couldn’t get the player and enemy turtle intersect to work. A small issue that I have with the app is that I have to wait until the enemy turtle takes one lap and then it allows the player turtle to start moving.

Earlier I said that this was not to the scale that I originally planned. What I meant by this is that I had planned a more intricate maze with more enemy turtles. Instead of making the maze with a turtle, I had to stick with objects, similar to what Elliot showed in his game app videos. I originally drew the maze by using a separate turtle. When I tried to find the intersection point (when the player hits the wall) it would only work at the turtle end location. This is why I had to stick with objects. Something that I gained from this assignment is the notion that I should do everything in small steps. Writing a bunch of code only to have it not work (my original maze for example) wasted time and patience. I should’ve focused more on the functionality of the game earlier on in the process and not so much the visual aspects. 

Original Milestones:
 - [ ] Display welcome message
 - [x] Create maze/boundaries 
 - [x] Make food 
 - [x] Create score by counting how much food is eaten 
 - [x] Create other turtles 
 - [ ] Create multiple levels
 - [x] Take in user input (up/down/right/left)
 - [x] Identify when user hits wall or is eaten by other turtles
 - [x] Have win screen
 - [x] Have lose screen
 - [ ] Have quit/reset (optional)
 
 Added Milestones:
 - [x] Create intersect functions
 - [x] Make objects for food and maze
 - [x] Have click function
