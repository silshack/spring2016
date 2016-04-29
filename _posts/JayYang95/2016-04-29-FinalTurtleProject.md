---
layout: post
author: JayYang95
title: "Jay's Final Project"
---

<iframe src="https://trinket.io/embed/python/12a50202d8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Milestones:

 - [x] Fully functional pause/resume
 - [x] Use of text file with difficulty settings
 - [x] Help dialogue button
 - [x] Cooler looking buttons
 - [x] Fully functional restart button
 - [x] Imported image
 - [x] Start with number of lives
 - [x] Use dictionary to keep track of level, lives, and coins
 - [x] Added more enemies
 - [x] Manage turtle states and variabels
 
For my final project, I chose to remake my original turtle game since I figured it would be more fun to do and there were already many things I wanted to improve on or implement the first time I made the game but didn't get the chance to. This was my chance to actually do them.

What it does:

This game is pretty similar to my old one, but with more features. The objective is to beat all 3 levels by collecting 5 coins in each level. Level 1 starts with 5 enemies. Every level after will increase the number of enemies by 1, their speed by 1, and their "reach" (how far they move forward at a time). The user starts with 3 lives in each level. When the user collides with an enemy, the user's turtle will flash red and black and will be invincible during that duration. The user may pause the game at any time by pressing "P" and resume by pressing it again. The user can also restart the game at any time by clicking the restart button and can have helpful tips pop up by clicking the help button.

Process:

Since I decided to recode my turtle game instead of just refactoring my old one, I started out with a blank trinket and used the old turtle game as a kind of template. Because I was redoing everything, I had to code the game in small steps. First, I started by simply designing the UI (i.e. the buttons and the display). Then I wanted to give the program some very basic functionality, so I coded tina's movement. For the next step, I wanted to develop a pause/resume function so I made a variable called paused in my variables module that was initially set to false. Whenever the button "P" was pressed, the variable would switch to the opposite of what it was (paused = not(paused)). I then made it so that tina's movement functions (up, down, left, right) only worked if paused was False. This seemed to do the trick for the time. I then created the enemy turtles and spawned a certain number of them according to whatever the current level was, which was stored in a dictionary called gamesettings. I reused the enemy random movement function from my old program. Here is where I ran into my first problem. I tried to pause the enemy movement the same way I did with tina's, but only tina's movement would pause. I later fixed this when I realized I had to use:

import variables

def function():

    variables.paused == True/False

rather than:

from variables import *

def function():

    global paused
    paused = True/False
  
This way allowed the pause function to pause both tina and the enemies. With both tina's and the enemies' movement functioning properly as well as the pause/resume, I decided next up would be to implement collisions and number of lives. I reused the collision function from my old program since it's just a distance formula and had tina check for collisions in her movement functions and also had collisions checked for in the enemy movement function. Here, I ran into another problem. Since tina's movement when holding down up/down is actually rapidly moving tiny amounts of space, running into an enemy would actually count as several collisions. To fix this, I made it so that whenever tina collided with an enemy, she would become invincible for 1 second using a boolean variable called invincible. Invincible would be set to false initally and set to true if there was a collision. After 1 second (time.sleep(1)), invincible would be set to False again. While invincible was true, tina would not check for collisions in her movement functions. If there was a collision, the player would lose 1 life, which was also stored in the dictionary gamesettings (gamesettings["lives"] -= 1). A function called checkifdead() would then be called, if lives <= 0, then the player would lose.

The next thing to do was to actually implement the collectible turtles so that the user could actually win the game. I made the collectible turtles much the same way as I did the enemy turtles. Tina would check for collision with collectibles in her movement functions (without the invincibility aspect) and the number of collected coins (turtles) was incremented by 1 if there was a collision. This was also stored in the dictionary gamesettings. After incrementing by 1, checkwin() would be called. If the current level was 3 and all 5 coins were collected, that means the user beat the final level and the game would end, else if the level was < 3 and all 5 coins were collected, the level would be increased by 1 (gamesettings["level"] += 1) and advancelevel() would be called to progress to the next level by restarting everything with new settings.

Finally, the only thing left to do was the help dialogue and restart function. For the help dialogue, I just created a turtle that wrote instructions on the screen and cleared it after a few seconds henever the button was pressed. For the restart funciton, I realized that 95% of it was already implement within the advancelevel() function. All I had to do was set the level back to 1 and a couple variables back to False, and advancelevel() would do the rest.

Possible/weird bugs:

Sometimes, before I even run the program (even if I refresh the page first), the entire trinket will freeze up if I use my mouse scroll button to scroll down my code. This does not happen if I hold down up/down keys to scroll through my code. I'm not exactly sure why this happens.

Another thing was that my code would sometimes run slowly or enemy movement will stop altogether if the program is re-run without first refreshing the page. I'm not sure if this is because of my computer, trinket, or my code. Logically, I don't know how this is possible in my code since enemy movement is called in a repeating loop and will only stop moving if paused is true. But if paused is true, tina's movement should also be disabled, which is not the case in this bug. Only enemy movement stops. This could be caused by me changing the code without pressing save and re-running the program while I was still working on it. Nonetheless, this can be avoided by simply not pressing the run button again, since there is no need to with a restart function and this does not happen too often anyways.

Final thoughts:

Overall, I feel like I was able to make vast improvements on my previous turtle game and had a fun time doing it. I'm actually quite glad that I ran into problems while working on this as it feels satisfying to finally figure out a working solution. I was finally able to effectively use variables from another module as well as making use of newer concepts like dictionaries and extracting information from text files and mixing them with older concepts to improve my original turtle program.
