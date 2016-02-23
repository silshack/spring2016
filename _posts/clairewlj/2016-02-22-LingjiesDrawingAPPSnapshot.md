---
author: clairewlj
layout: post
title: "Lingjie's Drawing APP Snapshot"
---

This is my drawing app:
<iframe src="https://trinket.io/embed/python/ecc6b62e17" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection: I thought it was a very simple program, but I actually used a lot of functions for screen.onclick and screen.onkey, as I want to enable the users to both click on buttons to choose shapes and click on screen to draw it wherever they want - it included two types of clicking processes. Also, clicking on the "restart" button would clear the screen without changing the basic settings such as the background. The very useful tool I used was turtle.Screen.onclick(None). With this I could simply break the link between screen and one function each time after the user clicked, and then use turtle.Screen.onclick(fun2) to attach screen to another function, function2. 

Also, global was very useful, as I wanted to use key to control fillcolor. So I just created  fill_color=(a,b,c), and a/b/c would change according to the key pressed, and then in the drawing process, I let tina.fillcolor(fill_color) so as to control it.
