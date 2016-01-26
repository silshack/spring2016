---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Treasure Hunt Turtle"
---

Creating this program was quite the experience.  I'm not completely sure that I understand why I had to format the code in some of the ways 
that I did, but at least it is finally working! I'll elaborate on some of the lessons that I learned along the way.

First of all, I really had to get the hang of the try and except dynamic.  In the end, I discovered that I needed to put all the code that
I wanted to work and all its various scenarios into the try bit, and then leave the except portion for other things that a user might put 
in (like letters instead of numbers).  

Figuring out what elements I was not supposed to include was one of the easier parts of creating this program for me.  Rather than limiting
what could go into the program, figuring out how to eliminate the bad input was one of the less challenging parts.  I lumped this bit of
code down at the bottom of my program, so that after it tested the winning scenarios, it could move on to what didn't work.  Here's
what I have:

```
    elif int(user_x) > 100 and int(user_x) < -100 and int(user_y) > 100 and int(user_y) < -100:
      print("Please start from the beginning, and enter X and Y coordinates between -100 and 100")
    elif int(user_x) > 100 or int(user_x) < -100:
      print("Please enter a proper x coordinate between -100 and 100")
    elif int(user_y) > 100 or int(user_y) < -100:
      print("Please enter a proper y coordinate between -100 and 100")
```

The biggest learning curve for me was understanding that I simply couldn't just show a range of values and expect the computer to interpret
them as I would.  It sounds vague using words, so I'll demonstrate below.  Here is what I thought was the correct way to demonstrate a 
range:

```
 if int(treasure_x)-15 <= int(user_x) <= int(treasure_x)+15
```

Instead of this:

```
if int(treasure_x)-15 <= int(user_x) and int(user_x) <= int(treasure_x)+15
```

Maybe there is a way to create a program with a range like this, but if so, I was unable to figure it out.  I also discovered that instead of 
coding out a range between two numbers, it was much easier (and how I found the only way that worked) to use the upper limit of what I
was working with and give the user feedback this way.  So here is (an abbreviated version) of what I thought was right initially:

```
if int(treasure_x)-15 <= int(user_x) and int(user_x) <= int(treasure_x)+15 and int(treasure_x)-6 <= int(user_x) and int(user_x) <= int(treasure_x)+6
```
When this is really the best way to do it:

```
int(treasure_x)-15 <= int(user_x) and int(user_x) <= int(treasure_x)+15
```
In the first option, I was going for a range between 6 and 15, but in the second option, I just lumped everything together under 15.  Related
to this discovery, I also found out that I needed to write my ranges in ascending order.  So as the user guessed further away from the 
treasure, the lower down I put this into my code. If I had done it the opposite way, then I never would have gotten to the other steps,
since everything would fall within 200 coordinates of the program.

I think that I likely made the user feedback process more complicated than I needed it to be.  I wanted Tina to be a certain color within
a certain range for the x coordinates and Tina to be a certain color within a certain range for the y coordinates.  Hopefully, the user
would figure this out, and realize that when Tina changes colors there is a method to it.  Here's a sample of how I set it up:

```
 if int(treasure_x)-15 <= int(user_x) and int(user_x) <= int(treasure_x)+15: 
          if int(treasure_y)-15 <= int(user_y) and int(user_y) <= int(treasure_y)+15:
            print("Your x and y are both extremely close to the treasure.")
            tina.color("red")
            our_screen.bgcolor("green")
          elif int(treasure_y)-25 <= int(user_y) and int(user_y) <= int(treasure_y)+25:         
            print("Your x is extremely close to the treasure, and your y is very close to the treasure.")
            tina.color("red")
            our_screen.bgcolor("yellow")
          elif int(treasure_y)-50 <= int(user_y) and int(user_y) <= int(treasure_y)+50:
            print("Your x is extremely close to the treasure, and your y is close to the treasure.")
            tina.color("red")          
            our_screen.bgcolor("orange")
          elif int(treasure_y)-75 <= int(user_y) and int(user_y) <= int(treasure_y)+75:
            print("Your x is extremely close to the treasure, and your y is somewhat close to the treasure.")
            tina.color("red")
            our_screen.bgcolor("purple")
          elif int(treasure_y)-100 <= int(user_y) and int(user_y) <= int(treasure_y)+100:
            print("Your x is extremely close to the treasure, and your y is not very close to the treasure.")
            tina.color("red")
            our_screen.bgcolor("black")
          elif int(treasure_y)-200 <= int(user_y) and int(user_y) <= int(treasure_y)+200:
            print("Your x is extremely close to the treasure, and your y is not at all close to the treasure.")
            tina.color("red")
            our_screen.bgcolor("blue")
```

As this sample demonstrates, Tina is red when the x coordinates are within 15 of the treasure, and the background color varies by
how close or far away Tina is to the treasure as well.  A change in background color is a sign of progress in a way.  I based the rest
of the treasure hunt around these principles.

Here is my finished product of Tina's Treasure Hunt:
<iframe src="https://trinket.io/embed/python/2cfdce2f0e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Overall, this was a really challenging program to write, and I think I learned a bit about while loops and how they should be formatted.
My main question is whether or not there is an easier way to do this, since for the sake of all the current programmers out there, I hope
that there is.
