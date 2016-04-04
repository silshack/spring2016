---
author: clairewlj
layout: post
title: "Lingjie's Drawing App"
---

This is my drawing app:
<iframe src="https://trinket.io/embed/python/af8de342d7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflecton: 
While working on this drawing app, I experienced the whole process of starting thinking about possible and creative ideas, breaking them down and transform them into practical steps or procedures to be done, and making changes now and then to complete the project.

At first, I wanted to create a drawing app allowing users to choose preset shapes when clicking corresponding buttons, to draw those shapes on wherever they clicked on the screen, and also to change the filling color. I was thinking about letting the user draw a complete Chinese landscape painting or create their own universe including donut/orange/apple planets, etc. However, it was too difficult for me to make them look beautiful enough, so I finally decided just to draw simple shapes such as sun-circle, moon, cloud and whirl.

During the process, I've learned much more about the screen object, particularly the turtle.Screen.onclick and .onkey. The most useful thing I applied in my program was assigning value None to .onclick() to breaking the link between screen and current function, and then I could re-link screen to other functions if I needed to. I also think Jasmine's solution is very smart, which is simply calling different function at the end of each click.

I haven't changed much of my program from Tuesday. I realized that without setting boundaries, the drawing might exceed the edge of screen, so I put some conditional executions to avoid that. But I'm not sure if it's appropriate. What's more, I changed the size of instructions at the bottom.

Milestones:

- [ ] Drawing instructions and background
- [ ] Creating functions to draw preset shapes
- [ ] Creating functions to change the value of fillcolor
- [ ] Creating clicky functions related to screen.onclick()
- [ ] Setting changing color functions to screen.onkey
- [ ] Creating restart function and Add it in
