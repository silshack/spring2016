---
author: clairewlj
layout: post
title: "Lingjie's Game App"
---

This is my Game App:
<iframe src="https://trinket.io/embed/python/622f893d28" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The picture source:http://nuclear-news.net/2013/08/13/fukushima-protest-contest-win-a-gold-bar-from-ebisu-studios/

Milestones:

- [x] Draw background of 2 or more different difficulty levels of gold mine
- [x] Draw different sizes of gold and barriers on the screen.
- [x] Write functions related to change game mode
- [x] Write functions related to screen.onkey for controling directions of hook/turtle 
- [x] Write congratulating function
- [x] link shooting speed with click. 
- [ ] create "Win" animation
- [ ] Write functions related to change scores according to user’s gold mining result

Reflection:
I’ll have to apologize first for the game looking too simple right now, as I failed to spend enough time on it. I’ll keep working on it during the Spring break.

As I also cannot see the requirements of the reflections right now (the course web page of game app project is not shown), I’ll just write something about the game app.

Initially, I was trying to make a game that would be a simpler version of the famous Gold Miner Game. Basically during the game, the player needs to change the direction of hook, and then send it out to try to reach gold and win scores. To get to the next stage, the player needs to win enough scores. Obstacles include stones that have low scores and bombs that will not only force the hook to go back immediately, but also clear all gold near them. The restrictions of the game also include time limit.

However, setting time limit is still something I have to work more to figure out. And also, I do not have enough time to do math problems related to the locations of stone obstacles. So I just create two modes, and for the easy mode, the more distant the gold from start point is, the larger the size of gold is. Then in hard mode, all gold has the same size. Players need to catch all gold to win.

For the code, I use screen.onclick() to let players choose between modes, and use screen.onkey() to let players change the directions of turtle and also to send it out. For congratulation function, I insert a background picture.

In the future, for game I'll add more obstacles and other items such as diamonds, and set up the different speeds when dragging different items; for code readability I'll shorten the helper.py module and create more modules.
