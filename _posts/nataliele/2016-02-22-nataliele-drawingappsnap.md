---
layout: post
author: nataliele
title: "Natalie's drawing app snapshot"
---

Updated milestones:

 - [x] set up screen
 - [x] user is able to click on screen and choose mode
 - Mondrian mode
 - [x] user is able to draw squares with thick edges
 - [x] user is able to draw rectangles (standing up and lying down) with thick edges
 - [x] user is able to change shapes
 - [x] user is able to change color of the pen
 - [x] user is able to change size of the pen
 - Pollock mode
 - [ ] create blobs of different styles
 - [ ] user is able to change blob style of the pen
 - [ ] user is able to change color of the pen
 - [ ] user is able to change size of the pen


<iframe src="https://trinket.io/embed/python/4078223e56" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


So I was able to finish the code for one drawing mode (Mondrian). For the other one the codes should be similar, I would just need to create different shape of drawing.
I thought of another mode which is Warhol which would let user create an image and then multiply that image. This would require recording turtle's movement somehow but I dont think I have enough tools to do this.

I struggled a little bit with the screen methods. I was having a problem for more than 1 hour and then I realized I was missing "()" after the screen command T_T. 
In this app I'm using global variable, which is different from the class method shown in the O'Reilley. I'm not sure what are the advantages and disadvantages of these 2 methods. I also dont understand the class method very well...

I was also not sure why shape1/shape2 dont need to be global here while pensz has to be global. In addition, I have to define the variable pensz before defining the function whereas in my previous Clicky turtle, I didnt.
![global](http://nataliele.web.unc.edu/files/2016/02/global.png)

Clicky turtle:
![clickyglobal](http://nataliele.web.unc.edu/files/2016/02/clickyglobal.png)

Things I think would improve user interface: A way to let user know which shape or color they are on or a list of colors and shapes that they can cycle through.


