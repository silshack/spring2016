---
layout: post
author: nataliele
title: "Natalie's drawing app"
---

Revised milestones:

 - [x] set up screen
 - [x] user is able to click on screen and choose mode
 - [x] Display the current mode and other relevant information to the user
 - [ ] Instructions outside of the drawing template
 - Mondrian mode
 - [x] user is able to draw squares with thick edges
 - [x] user is able to draw rectangles (standing up and lying down) with thick edges
 - [x] user is able to change shapes
 - [x] user is able to change color of the pen
 - [x] user is able to change size of the pen
 - [x] user is able to reset the drawing template
 - [x] user is able to exit to the main screen
 - [ ] all colors, shape, size default back when reset
 - Pollock mode
 - [x] user is able to change shape of image
 - [x] user is able to change direction of the pen
 - [x] user is able to change background color
 - [x] user is able to change size of the pen
 - [x] user is able to reset the drawing template
 - [x] user is able to exit to the main screen
 - [ ] all colors, shape, size default back when reset
 
<iframe src="https://trinket.io/embed/python/047571e62f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For the Pollock mode, I import an image and use it as the turtle. Originally I plan to let user create a brush effect by dragging the turtle but ondrag doesn’t seem to work I just let user stamp the ink image. Another drawback with using an imported image is that I cant change the image's color. So I can only have black and blue ink drops and user can only change background color.
The turtle manual has shapesize function to change turtle's size but the function doesn’t work in Trinket and I'm not really sure why. 

A feature that I havent had time to solve is how to reset the shape, size and color back to default. Right now reset in Mondrian mode only clears the screen and reset in Pollock mode clears the screen but doesn’t change my background color back to white.

I think the biggest challenge for me in this assignment is to figure out how screen works. It looks like the only screen I can have is in the main module. The custom modules can only contain functions and variables but not another screen. Also it looks like I cant have 2 screens on the main module. Because I was thinking of how to set the drawing template in a defined area and have the instructions outside it. I thought maybe if I have 2 screens I can set 1 screen to contain the drawing area and the other to the instruction. Similarly, I cant have a screen object on a custom module so I have to add the imported image to turtle shape in the main module. Also it doesn’t matter whether the turtle.onkey is in a function or outside a function, it will still work.

I think having the milestones has helped me a lot in knowing the scope of my app and keeping track of my progress. 

Sometimes small mistakes throw me off and I have to spend hours debugging it. Sometimes I was stuck on getting something right. For example I was trying to create a good Pollock effect and then got lost in the small details that eventually didn’t work out. It turned out my first choice was the best option and I finally went with it. So I felt like I wasted lots of time on that instead of figuring out the features that matter more like reset the screen. But maybe it is unavoidable because this is the first time I use the import image function and so I did have to spend some time to understand what it can do and what it cannot do. 
