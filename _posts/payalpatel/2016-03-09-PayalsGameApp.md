---
layout: post
author: payalpn
title: "Payal's Game App"
---

**Game App:** 

<iframe src="https://trinket.io/embed/python/657bfe8fc6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Revised Game Milestones:** 

- [x] user can use up/down/leftright arrows to move on the screen  
- [x] create menu bar at the top 
- [x] create key buttons for menu bar
- [x] allow users to click screen to change background 
- [x] import images for backgrounds
- [x] have hidden treasure at random location 
- [x] show/display user's position in the corner (OR counter for # of objects collected)
- [x] create individual location tools for each user at the bottom of the screen—in order to allow each user to determine how close (or far) they are to the treasure 
- [x] create two turtles to find hidden treasure 
- [x] create animated win screen 
- [x] create instructions screen
- [x] create countdown timer 


**Reflection:**

When starting this game app I decided to start with the basics of the game before going on to the detailed stuff.  The basics included creating two users and making it so they were both able to find the hidden treasure.  I then worked on creating a way for each user to receive feedback in order to determine how close they were to finding the treasure.  In order to do this I treated each user independently of one another.  This allowed me to display information relevant to each user at the same time during the game, respective to each user’s position/location.  I wanted to have two users in this game because I felt that would increase the competitiveness of the game.  Once I created the two users and the code necessary for each user to participate in the game, I decided to create a timer.  I decided to add a timer because I felt that would make the game more interesting and it would add a bit more difficulty to the game.  I knew I wanted to create a timer, however, I wasn’t entirely sure of how to go about doing so.  I first decided to use a for loop to add 1 to a variable I created that was set equal to 0.  I then realized it would be better if I started with the amount of time given as the value of the variable and then subtract 1 each time in the for loop.  After doing this I found that my timer was going very fast—it wasn’t aligned with actual seconds.  In order to fix this I added “time.sleep(1)” into my for loop, so my timer would according to actual seconds.  

For this game app I imported several pictures.  I imported pictures for the background screen and stored them in a list that I used in a clicky function to allow users to click the screen for a different/random background.  I had to make sure the pictures I selected were large enough so that the screen wouldn’t change size whenever the user clicked the screen.  I also tried using an image for the treasure (I was planning on using an image of a treasure chest), however, that idea didn’t go as planned.  When I tried using the image, whenever it was called in the game, the image would take up the entire screen.  (I am assuming this is because of the size of the original image).  I tried to see if there was a way to alter the image in trinket or through the code I had written, but wasn’t able to find an effective way.  In hindsight, I probably could have resized the image before uploading it into trinket and that may have helped.  I instead ended up creating a for loop that alternates between different colors for the treasure (to make it look a little more exciting than a single color).  

