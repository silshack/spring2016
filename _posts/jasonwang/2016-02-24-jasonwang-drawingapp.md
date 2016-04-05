---
layout: post
author: wagerpascal
title: "Jason's Drawing App"
---
Before Midnight:
<iframe src="https://trinket.io/embed/python/312c77f0f7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Version After Midnight:
<iframe src="https://trinket.io/embed/python/fb26078dc9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> (Created Example Mode)

While I stated in my midsemeter reflection that I needed to have better foresight, it seems that I still had some issues envisioning the scale of this project. I was able to meet the major parts of this project, but I am in no way 100% satisfied with this result.

From my last milestone:

- [x] No printed text in final product.
- [x] Select drawing mode with clicks onto buttons.
- [x] Select colors with keys. 
- [x] Display relevant information at all times.
- [ ] Select line thickness.
- [x] Click button for clearing/resetting the board.
- [x] Uses custom modules and functions.
- [x] Use multiple turtles.
- [x] Uses Definite loops.
- [x] Uses screen method of some kind.
- [x] No errors
- [x] Be organized. 
- [ ] Establish a theme of some sort. (Optional)
- [ ] Animated Transitions. (Optional)
- [ ] Zoom in/out functionality. (Optional)

As before, the goal of this project was to create a microsoft paint-esque application where you can mainly freedraw, and post shapes at certain points. However, one of the major issues that I could not reconcile was the fact that since I had two different turtles managing the pen and the position of the shapes, they both end up being in the same place (turning it into a reverse connect-the-dots), and don't have the functionality of a program such as Microsoft Paint. Much of the difficulty lies in how to separate the "click" and "release" functions of the mouse; however, if one were to click down, it is also the same place for the "release" function, leading to each line connecting the shapes when pressed.

I also initially attempted to have the shape icons be clickable for selection, but it still leads to an issue of reconciling the clicking mechanism. I also attempted to plan out a method of creating a system where clicking a button would be determine a different mode (drawing vs. shapes setting). However, I still was unable to figure out the logic regarding this part.
As for the line thickness, I was attempting to determine a method of counting button presses so that I could use the arrow keys as a sort of "slider", but this also did not work out in time.

Oddly enough, loops and the screen functionality did not mix; most of the cases that I tried resulted in Trinket freezing (implying that something might have been looping forever). I decided to avoid the scenario as much as I could.

I learned a lot about myself under immense stress regarding programming, and think I handled it well considering my working time was cut in half due to traveling. However, my choice of project could have been more suited for the amount of time.
I also learned that drawing/art-driven projects aren't quite my cup of tea, and find it sort of hard to work with sometimes.
