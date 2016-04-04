---
author: izayak
title: "Ruotong's Drawing App"
layout: post
---

<iframe src="https://trinket.io/embed/python/a0f2ab41d8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>  
  

**Milestones (Revised Lists)**  

- [x] Set up a basic sturcture (Trinket code)  
- [x] Build up functions for drawing shapes etc.  
- [x] Users can control the screen with keys  
- [x] Accepts users' clicks  
- [x] Have an entirely graphical user interface (i.e. no printed text input besides what turtle.write())  
- [x] Allow the user to select a drawing mode that changes the program’s repsonse to clicks and/or keys  
- [x] Display the current mode and other relevant information to the user  
- [x] Allow the user to choose and draw shapes, lines, and colors depending upon the selected mode  
- [x] Allow the user to clear the drawing and start over   
- [x] Utilize custom modules for readability and organization  
- [x] Utilize custom functions for modularity  
- [ ] Utilize definite loops (i.e. for loops)
- [x] Utilize multiple Turtle objects  
- [x] Utilize a named Screen object  
- [x] Run without errors  
- [x] Be well-commented  
- [x] Be well-organized and readable  



**Reflection**  

1. Have to make sure what can be put in a main.py and what can be put in a helper.py. Some functions that are commonly used can be put directly in another py, such as I put all the small must-have functions in shortcut.py. Some functions can be put in helper.py with the use of custom modules and functions, such as I put all the direction change and shape drawing functions in custom_class.py. The rest of them can only be put in the main.py, such as functions using two turtles e.g. fill() and back(), functions using both turtle and screen e.g. on_screen_click() and on_drag_function(), onkey and onclick funcitons e.g. screen.onclick() and someturtle.onclick().  
2. Refactor to make the program readable and clear to the user and other programmers. I put all the main functions in the main.py, all the functions for setting up the screen (instructions and display) in screen.py, all the custom modules in custom_class.py and all the small helper functions in shortcut.py. Putting all the left/right/forward/backward and drawing functions in the main.py can be very messy, and it can be solved by creating a custom module. That is way better. Now the program is much more concise than before.  



**Future Improvements**  

1. In clicks mode, I also achieve 'clear up and start again' feature by linking the clear() function with the 'z' key. If it is strict that in clicks mode no keys should be used, I have to improve that.  
2. I used another turtle jack for working in the function back(). I also want to switch its pencolor and fillcolor, but the toggle.color() does not work. Maybe it is because two onclik of two turtles cannot be used together?   
3. I haven't included a definite loop. I think that would be a good improvement, maybe can be used in cooperate with counting the number of keys pressed/clicks by the user.   
4. As I can create turtle custom modules, I can also create screen custom modules. I've tried also put screen.onkey() functions into the custom module, but in the screen.onkey() there are still turtle nested, which need to be solved first in order to move those screen.onkey() functions into custom module.  

