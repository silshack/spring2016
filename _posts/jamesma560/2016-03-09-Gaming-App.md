---
layout: post
author: jamesma560
title: "Gaming App"
---


<iframe src="https://trinket.io/embed/python/c885376a7d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


So frustration kept me from sleeping so I ended up working on it more. And I'm glad I did because I actually ended up with a game that works. 

If you look at the embedded trinkets in the previous pull requests, I had originally wanted to do a game where a player ("Marcus Paige") ended up competing against an automonomous moving turtle (Grayson Allen) to collect the most basketballs. However, this avenue ended up being unsuccessfull because for one, when a user intersected with the ball the score would increment inconsistently (sometimes by 1, by 5, or not at all), and also when a user intersected with a ball the ball wouldn't disappear. I tried really hard to solve these problems, but upon exasperation, I just ended up giving up and trying to get some sleep.

Fortunately I wasn't able to get to sleep, and instead came up with an idea to sort of 'hide' my limitations. Instead of having there be a bunch of visible basketballs, I decdied to make even more and make them all invisible. Therefore, the inconsistent score incrementer looked more correlated to the user's movement (the more the user moves the more stamps they cross, and thus the higher score). I then changed the point of the game from trying to out-collect Grayson Allen, to just trying to avoid him while moving as much as possible (kind of like Snake).

In the end, this isn't at all what I wanted to begin with, but I am proud of the fact that I was able to adapt and to come up with a working game to present. Especially considering the fact that a couple of hours ago, I didn't know I would even have one. 



Milestones: 

- [x]	Use a custom class (pass in coordinates, variables, whatever) 
- [x]	Use custom methods with those custom class 
- [x] Create screen. 
- [] Fullfill all assignment requirements. 
- [] Include both key and click events. 
- [] Have a .congratulate() that appears when the user wins. 
- [x] Have a turtle .write() game instructions to the screen 
- [x]	Use a custom turtles to display information to the user 
- [x]	Just have good user feedback 
- [x]	Try to implement a loop. 
-[x]	Have a turtle that is controlled by the user’s arrow key. 
- [x]	Have a turtle that moves independently of user input. This may be something which the user has to dodge. 
- [x] Have a turtle that moves based off of for loop to obtain constant motion. 
- [x] Put in condition that prevents infinite loop. 
- [x] Have an event triggered when the user controlled turtle intersects with the independtly moving turtle. 
-[x]	Use a method that I have never used before (perhaps .seth() or .towards()) 
-[]	Have an option to reset the game to it’s “starting” state.
Stretch milestones 
-[]	Have there be different levels. Higher the level, the more stuff (turtles) the user has to dodge 
-[] Include a story -
-[] Have a “collecting coins” aspect





