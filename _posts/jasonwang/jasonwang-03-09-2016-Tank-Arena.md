---
layout: post
title: "Jason's Game App"
author: wagerpascal
---
<iframe src="https://trinket.io/embed/python/d532a75fb4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I came into this project thinking that it would be simple- perhaps only several inclusive classes and some math and I'd be done.
I think I was a victim of scope creep.

##Milestones
- [x] Make Tank figures or sprites.
- [x] Be able to move the tank.
- [ ] Set limit on movement per turn.
- [ ] Adjust angle of fire.
- [ ] Adjust firing speed.
- [x] Generate map for Tank.
- [ ] Set tank health.
- [ ] Determine method of awarding damage.
- [x] Animate tank shell trajectory.
- [ ] Create turn-based system (based on whether you have shot).
- [ ] Have tank turret indicate angle (Optional).
- [ ] Create dumb "AI" for other tank (Optional)
- [ ] Make craters for where shells land (Optional)
- [ ] Generate multiple maps (Optional).

Looks like I didn't get a lot of milestones this time. The major issue that resulted in this many blanks was the fact that apparently,
functions in screen.onkey don't seem to work when trying to pass parameters through. Each time I would receive a null error. After
attempting to get parameters working, I attempted to see if I could use a function like a trigger (for example: on press, something = True),
in order to see if I could use the keypress to begin a calculation; this unfortunately didn't work either. I am not 100% sure on why,
but I do think it's related to something with the screen.onkey method and how it enacts functions.

This issue led to me being unable to have alterable stats for the tank, as I needed the values to calculate the traveled distance(kinematics, anyone?).
Therefore, I used preset values, and changed the game from a turn-based game to a real-time arena mode game. For the turn-based portion (not in the code),
I had a rough draft of code that alternated between True and False states, and disabled key bindings for the other tank during the opponent's turn;
this can be accomplished through screen.onkey(None, "key of choice"). Ideally key bindings would be reset again at the next turn.

The biggest issue I definitely faced during the last phase of development was the integration of using classes to do complicated 
functions in parallel. For the score and collision functions, I attempted to run separate methods to keep the calculations for each 
object isolated, but it seemed that values were still leaking into each other. I will admit that this is probably bad form, but I 
created separate classes, which did allow each object to remain isolated.

However, since the last drawing app, I'm proud of the fact that I approached the development modularly. I started with general 
tank development and setup, shell setup, shell trajectories, and tank movement (all for one tank). Once I was able to have one tank
performing well, I put in a second tank (no functionality), and did the setup of the functions. I ended with consolidation of the 
second tank's functionality.

Also, I took a page from my last reflection and separated everything into a lot of modules. Unfortunately, since I had to keep the 
object names local to the screen.onkey functions, I was forced to keep a lot of the general game framework in the main.py file.

Overall though, I did learn a lot about the classes and especially global variables (it was the first time I've used them, and 
I learned a ton about scope interactions).
