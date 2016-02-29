---
author: izayak
title: "Ruotong's Drawing App Peer Review"
layout: post
---

**App**  
My partner's program is a completely graphical user interface, and allows the user to draw different lines and shapes (including square, triangle, parallelogram, circle and even a spoke!), change background colors and clear screen to start over again. If the user forgets which keys relate to which functions, he/she can see the instructions again by pressing the keyboard. There is only one thing that I am not sure. It seems that there are 2 modes that the user can choose: with or without pen traces. But due to my practice, which I am not sure if I did it right, only the parallelogram is drawn under the no_line mode and it is not selected by the user.  

**Code**  
Overall, the progrma is well-organized and well-formatted with comments, modules, functions. My partner uses the for loop to deal with one replicate function (to set up two turtle function at the same time), multiple turtles to separate modes and a named screen object.  

**Process**  
My partner's program's milestones are updated and the new milestones serve the program better. He left some advanced features which can be improved later such as choosing background color by picking quadrant and drawing shapes with different sizes. These features need more advanced methods, at least custom modules. All in all, his milestones divide the task into small parts well and are achievable. 

**Self-reflection**  
What my partner's program inspires me are:   
1) Instead of using custom modules to deal with the shape functions and move functions, we can do it by nested functions. That is, put one function with arguments in a py other than main.py, then define a function without argument (since we have to link this one with a key via onkey function) in main.py and call the one defined before.  
2) My partner uses two turtles to separate the clicks and keyboards features.   
3) I like that "spoke" shape a lot!  
But at the same time, I think it would be better to leave instructions on the screen for the user. 
