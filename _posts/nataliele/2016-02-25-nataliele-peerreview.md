---
layout: post
author: nataliele
title: "Natalie's peer review of Kit's drawing app"
---

<iframe src="https://trinket.io/embed/python/9e2395502d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

 - [x] Have an entirely graphical user interface: I like the use of an additional screen for instruction before the drawing start and how it waits for the user to finish reading and press "s" to start. I also like the counting down screen. Very nice use of `for` loop!
 - [x] Allow the user to select a drawing mode that changes the program’s repsonse to clicks and/or keys: click to draw and press keys to change colors in Wonderland mode.
 - [x] Display the current mode and other relevant information to the user: the app displays modes and the keys to press to change colors, reset and quit to main screen
 - [x] Allow the user to choose and draw shapes, lines, and colors depending upon the selected mode
 - [x] Allow the user to clear the drawing and start over
 - [ ] Utilize custom modules for readability and organization: As Kit mentioned, he tried separating the codes into smaller modules but that messes up the app somehow.
 - [x] Utilize custom functions for modularity
 - [x] Utilize definite loops (i.e. for loops)
 - [x] Utilize multiple Turtle objects
 - [x] Utilize a named Screen object
 - [ ] Run without errors:
So when I press c or w out of order or in the main screen or in a different screen than im supposed to, the screen is kinda messed up.
![croquet](http://nataliele.web.unc.edu/files/2016/02/croquet.png)

I think these codes below might have caused the problem. Because it's an `if` statement, pressing these keys anytime in any mode will call those functions and cause errors. I think they should be moved outside the function and should still work.

```python
def switch():
  if pitch.onkey(conventional,"c"):
    conventional()
  elif pitch.onkey(restart,"w"):
    restart()
  elif pitch.onkey(wonderland,"x"):
    wonderland()
  elif pitch.onkey(select,"q"):
    select()
```

 - [x] Be well-commented
 - [x] Be well-organized and readable

Kit had a very clear idea what he wanted the app to do right from the beginning and the final product wasnt too different from what he originally envisioned (save for the surprised ending and winning sequence). The final codes are much easier to read with better use of functions. The milestones also did not change much though they could have been more detailed.

I think Kit and I definitely approach the assignment differently. I set up shape of pen for users to draw on blank space whereas Kit had a template with hoops so users move through them (conventional croquet). This makes my code more function-intensive because I need to create functions and the users can handle the rest ie the drawing. Kit's codes are more drawing-intensive itself because he had to calculate coordinates, write codes to draw hoops, write numbers.

I kept all the screen functions right on the main module for example calling the screen_helper turtle into the main screen, keeping all the `turtle.onkey`, `turtle.onclick` on main module. Kit moved all of them into the custom module and only called the functions in the main module. I'm not sure but it could be the reason why he couldnt separate the codes into smaller module.

He also decided to have the colors randomly selected and not cycled through in an order so he didnt have the issue I have about reseting the default properties to the drawing pen.

He did remind me about creating functions to reset and switch between mode. I also added the instructions on the screen following his example. We both still have the problem of drawing over the instructions because they're on the same screen though.

Overall, I think we both did well on this assignment.
