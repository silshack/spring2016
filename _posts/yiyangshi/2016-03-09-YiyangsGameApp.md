---
author: yiyangshi
layout: post
title: "Yiyang's Game App"
---

Here is the program:
<iframe src="https://trinket.io/embed/python/2802271ec1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Milestones:

- [x] draw shooting barrel and ice stack
- [x] link shooting barrel with keyboard control. Make shooting barrel rotate by clicking "Up" or "Down"
- [x] make turtle move along the direction of the shooting barrel in straight line
- [x] make turtle move along the direction of the shooting barrel in parabola
- [x] define "hitting the target"
- [x] make the game delete one ice when the user hit the ice stack
- [x] link shooting speed with click. 
- [ ] create "Win" animation

Optional Milestones:

- [x] make a welcoming manual
- [ ] create turtles with different mode 
- [ ] allow clicking to choose turtle modes and change speed control to keyboard control.


Reflection:

With limited time, I created the game that met my basic expectations. The game is very much like an angry bird game where users can choose the shooting position of the turtle. The shooting position is changed through keyboard control. The game also allows users to choose the speed of the turtle through onscreen click. To add more fun to the game, I created limited turtle lives. In order to win the game, the user will need to hit the three ice blocks within 4 tries, which is challenging. 

I strived to make the game run with no bugs. The game does not go crazy when clicking too fast. This is achieved by unbinding keys when the keys are called and executed, and binding them back when the execution is done. Also, when the manual is displayed, the users will not be able to use the onscreen click and the keys. This is achieved by simply changing the order of the codes.

Originally, I want to make a more complicated game. I wanted to create different turtles where their shooting arcs are different. For example, some arcs are more flat than others. Also, the shooting arcs for the current game do not look natural because they are just a piece of a circle not an actual parabola. In the future, I want to use physics functions to make the arcs look natural. However, I am still proud that, within my crazy schedule of this week, I am able to create a game with no bug and met my basic milestones.  
