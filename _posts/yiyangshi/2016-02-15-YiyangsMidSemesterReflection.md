---
author: yiyangshi
layout: post
title: "Yiyang's Mid Semester Reflection"
---

It is exciting to look back at each programs accomplished and see the codes becoming more complicated with logic controls, functions, and loops. It is even more exciting to see how much more the turtles can do. While reviewing all my coding programs done so far, I noticed the power of continuous code revising, which is to continuously revise an existing program and make it more concise and powerful. In fact, I have learnt the most from revising the very first turtle exercise I have written, the coolest turtle, and from revising others’ codes through pair programming.

Here are the three turtle exercises:
<iframe src="https://trinket.io/embed/python/99ab53d1b7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
<iframe src="https://trinket.io/embed/python/5292f2db95" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
<iframe src="https://trinket.io/embed/python/f517596f4a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For my very first coolest turtle program, I had the turtle draw four stars on the screen, one enclosed by another. I wrote separate codes for each star drawn on the screen. As a result, there are a lot of repetitive codes with no more functions other than drawing four starts. When we had the chance to create a logic turtle, I decided to improve the coolest turtle program by using logical controls and loops to equip the coolest turtle with more functions. 

```
for number_of_star in range (1, 5):
  if previous_color=='yellow':
    current_color='white'
  if previous_color=='white':
    current_color='yellow'
  tina.color(current_color, current_color)
  tina.penup()
  tina.goto(start_point_x, start_point_y)
  tina.pendown()
  tina.fill(True)
  for number_of_edge in range (1, 6):
    tina.forward(length_of_edge)
    tina.right(angle)
  tina.fill(False)
  previous_color=current_color
  start_point_x=start_point_x+(5-number_of_star)*10
  start_point_y=start_point_y-10
  length_of_edge=length_of_edge-(5-number_of_star)*20
  number_of_star=number_of_star + 1
```

The “for” loop efficiently decreases the lines of codes from 70 to 25. The logic controls within the “for” loop allows the color to change between yellow and white with each iteration. The program also allows user input so that it is more interactive. However, as more functions and loops are added, the program becomes a little harder to read. So, for the function turtle exercise, I came back to this program again and revised it. This time, I defined a function for star drawing and pulled the drawing process out of the loop. The color switching process was also pulled out from the loop to add readability. This time, no other functions are added but the number of lines within the star drawing loop was decreased from 25 to 8.

```
for number_of_star in range (1, 5):
  tina.color(yellowandwhite(previous_color))
  tina_draw_star(start_point_x, start_point_y, length_of_edge, angle)
  previous_color=yellowandwhite(previous_color)
  start_point_x=start_point_x+(5-number_of_star)*10
  start_point_y=start_point_y-10
  length_of_edge=length_of_edge-(5-number_of_star)*20
  number_of_star=number_of_star + 1
```

By looking at the code evolution, it becomes clearer to me the advantages of using logic controls, functions, and loops. Another advantage of code revising is that it allows me to discover deficiency and pushes myself to fix it. When reviewing my code for the treasure hunt turtle, I noticed that the user input for x coordinates and y coordinates are not parallel in which users need to type in x coordinate again if the user accidently types an invalid value for y coordinate. 

```
while still_going:
  user_x = raw_input("Choose an X coordinate between -100 and 100")
  try:
    float(user_x)
    if float(user_x)<=100 and float(user_x)>=-100:
      user_y = raw_input("Choose an Y coordinate between -100 and 100")
      try:
        float(user_y)
        if float(user_y)<=100 and float(user_y)>=-100:
		…...
        else:
          print “y not between -100 and 100"
      except:
        print “y not number"
    else:
      print "x not between -100 and 100"
  except:
    print “x not number"
```

With the help of the professor, I not only fixed the issue but also learned the technique of “while true”, which I implanted in the poetry slam exercise.

```
good_x = False
while not good_x:
  user_x = raw_input("Choose an X coordinate between -100 and 100")
  try:
    float(user_x)
    if float(user_x)>=-100 and float(user_x)<=100:
      good_x = True
    else:
      print "not between -100 and 100"
  except:
    print "not number"
    
good_y = False
while not good_y:
  user_y = raw_input("Choose an Y coordinate between -100 and 100")
  try:
    float(user_y)
    if float(user_y)>=-100 and float(user_y)<=100:
      good_y = True
    else:
      print "not between -100 and 100"
  except:
    print "not number"
```

In the poetry slam turtlehack exericise, I also had the chance to make big changes on my original poetry slam programming. In my original program, I created a “poetry_line” variable, which is to be rewritten by the new input line and appended to the main poetry through each iteration. Thus, the separate lines are not stored but only the whole poetry. In the turtlehack exercise, however, each line of the input needs to be splitted for printing so the original program is not very compatible. Admittedly that it is difficult at first to delete codes, but the process of realizing which part of the codes are incompatible gave the change of better understand the functionality of each line of codes. 

The value of code revising includes not only revising one’s own programing, but also revising others’ program. Revising other one’s programs contains the reading part as well as the revising part. I find reading other’s program valuable as it introduces new ideas on solving the same problems. For example, for the score computing exercises, I learned from others’ codes that we can also use the length of the input to evaluate if the input is valid or not. I also learnt the sort function in an in-class pair programming exercise. More than that, reading other’s program opens me to new ideas. I am always amazed by others’ creative ideas using similar tools. Clicky turtle can mean drawing flowers wherever user clicks, it can mean finding a way to the treasure and avoiding evil turtles, it can also mean triggering fireworks.

However, I find that reading and understanding others’ codes can be a difficult job, especially since we are all entry-level programmers. As entry-level programmers, we may create variables with uninformed names; our code structures can be messy; we may have very few comments to help readers understand the functionality. All of the above can increase the difficulty of understanding someone else’s codes. Also, I find that I am reading codes in the wrong way. I tend to read codes line by line instead of finding out the main body of the program and then read the helper functions. Such way of reading codes does not help with understanding the functionality quickly and it can cause frustration. For the next half semester, I would like to read more codes for practice. I believe that being able to quickly understand someone else’s codes also makes a good programmer. 

Another frustration I had is to edit someone else’s codes. I felt this frustration strongly with the latest refectory exercise. When the code is complicated, I find it difficult to figure out the scope of the variables and the functionalities of each function. I tried to cut out a piece of codes and run it separately in an empty program, but, since there are too many related variables and functions called, there are always a lot of bugs to fix. It is also difficult for me to figure out the main part of the codes and then read the according functions called in the main body separately. Editing directly on the original codes can always create more bugs. I find two ways to help with the process. One is to comment out the original codes and run the program with replacement codes. It can be time consuming but it prevents the program from being completely messed up. Two is to add comments to indicate the functionalities of each trunk of codes. However, I believe that the best solution is just to practice more. 
