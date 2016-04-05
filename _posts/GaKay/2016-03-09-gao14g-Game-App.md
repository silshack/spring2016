---
author: gao14g
layout: post
title: "Ga Kay's Game App"
---

# My Trinket
<iframe src="https://trinket.io/embed/python/c5901db926" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Required Milestones
- [x] have an entirely graphical user interface
- [x] have at least one key event
- [x] have at least one click event
- [x] have a ‘Win’ screen
- [x] show user ‘state’
- [x] have at least one custom module
- [x] use at least on definite loop
- [x] have at least one custom extension of Python’s Turtle class
- [x] have a named Screen object
- [x] have at least two Turtle objects
- [x] run without errors
- [x] have comments
- [x] have ‘enemies’ that the user can ‘kill’ (keep count of number of enemies killed)
- [x] have a larger enemy the user can’t kill that will hurt the user (keep count of lives)
- [x] have enemies randomly move around
- [x] have larger enemy slowly chase the user

## Optional Milestones
- [ ] have at least two to three levels the user can play
- [x] allow the user to choose what their character will look like
- [x] let the user restart the game without using the Run button
- [ ] have randomly spawning coins the user can collect
- [ ] have randomly spawning powerups that will help the user (maybe increase speed) 
- [ ] make the game Zelda themed

# Reflection
Now that I’ve completed this assignment, I’m pretty proud of my game. It’s amazing that I was able to pull this all together in about a week and half. It was definitely a great learning process. Once I came up with my idea for my game, I started my typical problem-solving technique. I start with the easy stuff first, which in this game, was getting the game screen set up. After I had my game set up how I wanted, the hard part came: the functionality of the game. I first created the different classes for all my turtles and defined the functions I thought I would need. I remember getting stuck on getting all the turtles to move. At first, I used a “while True” statement, but I switched to using the screen.ontimer function. For a while, I wasn't able to get my turtles to stop moving after the game had finished. With the help of Elliot, I realized that I needed to use a global variable in order to call the variable I was trying to change. Fixing that part wasn’t as bad as I thought. One of the harder parts I got stuck on was figuring out the intersections of my turtles and getting those intersections to work with my different game functions (such as the counter function and lives function). I first used one of Elliot’s complicated code to check for intersection, but then in class, he mentioned using “.distance” so I decided to try that out, and it was much easier to implement.  I slowly worked at the check intersection functions until I was able to get everything to work correctly. I also ended up changing my approach to the “life” turtles I had in my game. At first, I had three separate turtles to show the lives, but then Elliot said I could try to use the “.stamp” function. I feel like that made my game run better and made it easier to work with.

While working on this assignment, I noticed that I would slowly tweak my program to make it better. I didn’t complete it all in one sitting. I would work on it a little bit each day. Once I had my main functionalities working, I would run into little bugs. I would try to fix them, and if I was unsuccessful, I would come back to them later. Once all my main bugs were fixed, I would notice little things about my game that I didn’t like. I would tweak my code some more and get my game to run how I wanted. After I had my code the way I wanted, I started for my reach goals. I was only able to get two of my reach goals done, but I’m glad that I was able to tackle at least some of those goals. I feel like there are probably better ways to code my game, but overall, I’m happy with it.
