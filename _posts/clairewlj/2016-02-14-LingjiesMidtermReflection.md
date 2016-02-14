---
author: clairewlj
layout: post
title: "Lingjie's Midterm Reflection"
---

Generally speaking, this course is truly excellent and exactly what I expected as my first step in programming. I tried many times to learn on my own, but always stopped by problems so basic that there were no answers on the Internet or in textbooks. Fortunately, I now begin my journey, and trinket and github are really helpful.

I think that based on my understanding of programming so far, there are two main parts I’ve improved most and still need to work hard on: building up both more technically efficient and functional programs to achieve real-life goals, and also more interactive mode to allow for more specific demands from users. I believe both of them are necessary parts of a truly useful program.

Starting from zero, the improvements in programming skills are actually visible. In my first program, I used turtle to write “HELLO WORLD” on the screen. I spent much time calculating the suitable distances, directions and also radius and finally the program consisted of repeating penup/pendown/goto/forward/left commands, which made it an 140-line program. I think this is a great example of “learning python the hard way” – actually I still do not know how to significantly improve it as loops and functions may not be that useful under such circumstance – as during the process, I had a basic understanding of what the starting point and direction were, how turtle moved under specific commands, and I also made my first try in this course to find the instruction of drawing a semi-circle using online sources. 

This is the "HELLO WORLD" program:
<iframe src="https://trinket.io/embed/python/deb914d084" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Moreover, I left a question to myself on how to change the direction of drawing a circle without using extra command such as turtle.right(), and I figured it out in next exercises. In the chapter 3 turtle exercise, I really enjoyed drawing a funny moustache using turtle.circle() to draw a half circle, a quarter circle and an arc with central angle 50°. Then in the treasure hunting exercise, based on the combination of circle drawing and angle calculating, I could even draw a pair of eyes looking at the where the user clicked and moved according to the change of coordinates, which I was really proud of. It is important that I could see the actual improvement I made step by step, and that I could find pleasure when learning programming, when I was a little worried about whether it was late to start learning. The feeling of satisfaction is a necessary source of power to push me further in studying everything new including programming. 

The moustache:
<iframe src="https://trinket.io/embed/python/3e581ebd02" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The clicky treasure hunting:
<iframe src="https://trinket.io/embed/python/80b8b9f32d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I also learned a lot about functions. Not just the apparent advantage on the surface – getting help from smart and efficient functions already existed assists to avoid wasteful duplication of effort, which I heard about before taking this course; even better, I now know about the inside of functions, how I can create my own functions, how to import them from another module, and how to call them in different situations. As I’ve learned the basic principles instead of just knowing how to apply them, functions are now actually a tool I can use.

Recently, another amazing part I’ve learned is loops. Even though I do not know much about how the actual programmers write their programs, I believe loops is a crucial part as it saves tremendous time and effort to conduct repeating tasks. As for lists and strings, I still do not feel confident in using them deftly. They’re powerful and practical in handling more complex tasks than just drawing pictures, and I believe I still need to do more practices to get familiar with them, especially when they’re combined with loops and conditions. 

Generally speaking, the more knowledge and skills I’ve learned, the less limits I feel when I have specific goals to achieve. I don’t want to give them up and change to an easier task, so I’m studying hard.

Interactive mode is another important part of my progress. I only knew a little about the raw_input() function before, and at first, I just used it to ask for simple prompt from users, such as setting up pen color and background color accordingly. Then I saw a classmate’s quite creative work, where the program first asked the user for color options, then drew a flower using turtle and asked the user for appraisement, and then let the turtle express anger and run away if it was not praise. This was enlightening: communication between program and users were not just ordinary asking for and following commands; such interesting jokes made computer more humanlike and shorten the distance between them and users. Based on that, I made my chapter 4 exercise ask users whether they like KFC or not. If they answered yes, the turtle inside would draw a pair of glasses and a moustache (I tried my best to make them look like the logo) and say, “I like you, too”. But if them answered no, them the program would keep printing "Sorry did you just say 2? I think it's a system error. Please try again" and then ask for a new answer until the users answer yes. I hope everyone seeing this will enjoy it, as I was laughing the whole time when I was writing the program, and that’s what I want my works to provide.

The KFC program:
<iframe src="https://trinket.io/embed/python/31bff91f7f" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Another extremely useful part is conditional executions. The logic inside if & else is easy to understand, and with them I can go deeper to meet the needs of users by expanding the range of possible situations and providing related solutions. Try & except is also excellent, as I do not need to consider each type of error that may occur. Instead, I can just “try” to execute and if there’s any problem during the process, it will jump to the except block. I’ve used them a lot, especially when I need a numeric answer from users, I can now just try float(prompt). 

When conditions are combined with loops, infinite communications between program and user is enabled, and users will have more chances to follow the instructions, change answers until they give the right kind of input in each step without re-starting from the very beginning. The keyword “raise” and the more specific classification of except error types such as ValueError are also useful. I think I’ll use more in the future.

As for the future study, I’ll keep enhancing the two sides of skills discussed above. One useful but difficult part I want to learn more is click. We have already learned its basic principles, which is act according to the position where the user clicks, and make use of the coordinates. This is an important way to catch the react to the movement of users, and I think I still have some trouble using it proficiently, particularly when it’s combined with functions. Anyway, I’m happy to basically understand how it works, and I even think of it when I play games on my cellphone. 

Another thing I want to learn more is about the application of python into data analytics (yes I finally remember I’m a statistics student), and how it can work with other tools such as MySQL and R. I think the program in List exercise is a good example: filtering and picking up specific information we need from a txt file. And I want to know how to connect it with other types of files such as word, excel and R markdown, etc. As I also begin to learn R this semester, hopefully I’ll learn to combine them to apply to data analysis when this semester ends.
