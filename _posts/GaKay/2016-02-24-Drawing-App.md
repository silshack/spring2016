---
author: gao14g
layout: post
title: "Ga Kay's Drawing App"
---

## My Drawing App:
<iframe src="https://trinket.io/embed/python/aa76638dcf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Revised Milestones
- [x] include turtles that allows users to choose what to draw when they click a certain key
- [x] include a free draw mode that allows users to click and drag a turtle
- [x] include turtles that allows users to choose color
- [x] include clicky turtle that clears board
- [x] display current mode to users
- [x] include at least one custom module
- [x] include at least one loop
- [x] include multiple Turtle objects
- [x] include a named Screen object
- [x] has commented code
- [x] all on-screen clicky turtles accepts user clicks
- [x] runs without errors
- [x] allows users to cycle through background colors when key is pressed

## Reflection:
So far, I think this assignment has been the most difficult. It definitely took me quite a long time to create my drawing app. I think one thing that made this assignment particularly hard was the fact that we had no code to go off of. We were building this drawing app from scratch. Before I started started coding, I already knew what I wanted my app to do. The hard part was figuring out how to get there. To start off, I coded all of the simple things such as where the turtles were going to be set up and what shapes were going to be drawn. Then, I started to tackle the actual funcational parts of the app. This is what took me the longest. One of the first things I got stuck on was my free draw mode. I wanted to have the drawing turtle change to the color of the turtle that was clicked. I kept watching the videos we were assigned to watch for class, and I decided to mess around with classes. To my surprise (after working on it for a while), I was able to get that to work. I remember feeling so happy because I was able to use this new code that we haven't really messed with before. After I finished the free draw mode, I went on to the shapes mode. I tried to have a similar clicky function where when you click on a certain turtle, it'll change to that mode and wherever you click, it'll draw that shape. I worked at this for a while, but I was unable to figure it out so I switched my idea a bit. Instead of having a click function, I used the onkey function so that when a certain key was clicked, it would switch to a certain shape mode.

My code runs with no errors, but there is a slight glitch in the code that I haven't been able to figure out. It deals with clearing the board. I first tried to use the .clear() function, but then I was unable to allow the users to keep drawing since none of my stuff worked. Instead, I made a clear screen function for both modes that reset and hid all the turtles on the screen. The problem occurs with the shapes mode. When you click clear on the shapes mode, it'll occasionally glitch and draw a stray line or shape. I'm not sure what the issue is here. I tried for a while to fix it, but I don't know what the problem is. There are also a few the things the user can't do or it'll mess up the code. The user can technically have both modes on the screen at the same time (if they click 1 and 2), but they don't work together so it messes up the funcationality of the program. Also, whenever the user clears the board for the shapes mode and later chooses the free draw mode, if they try to click the keys assigned to the different shape modes, it messes up the program. Overall, my code works how it's supposed to and it does what I want it to do, but there are just a few little bugs that I haven't been able to figure out.
