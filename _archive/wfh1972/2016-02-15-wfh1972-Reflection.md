----
author: wfh1972
layout: post
title: "Wayne Homan's reflection"
----

Reflection:

BLUF: 
1) Things that are harder than thought: 
     a.	Understanding loops
     b.	How variables work
     c.	I have had my differences with trinket
     d.	The book is a little soft on examples
2) Things that are going well:
     a.	I like python
     b.	I can see how I can get to my end goals
     c.	I am actually happy when I can get things to work
     d.	This class seems to be pointing me in the direction I want to go

Background:
I have very little (read none) experience in coding or programming unless you count basic that came with the vic-20 back in the early 80’s. I am situationally aware enough to understand that coding and programming is one of the critical skills of the future (if not the present). Almost every job out there could be made easier/more efficient with a little programming skill. I am a physician and there are so many places that I can think of that a short bit of code could make my job easier (e.g. a short bit of code to search the medical record and return major diagnoses that I should be aware of but don’t want to read the entire medical record to find). 

Things that are harder than I thought they would be:

Understanding loops: I have yet to truly understand try/except or any of the other loops. I can usually get them to work after I look them up in the book or google. It is a major impediment because I know what I want them to do but I don’t have the programming language to accomplish it. 
# initial set up of variables

  # x is the total variable
x = 0
  # y is the number variable
y = 0
  # z is the average variable
z = 0

# a and b are my mins and maxs
a = -10000000
b = 10000000

# c is a dummy variable used to stop the loop
c = 1
# getting the input
while c > 0:
  # getting the input
  try:
    input_number = raw_input("Input a number between -1000000 and 1000000:")
    if input_number == "done":
      c = -1
      #stops the loop
    else:
      input = int(input_number)
      if input > a:
        a = input
      else: 
        a = a
      if input < b:
        b = input
      else: 
        b = b
      # does my math for me
      x = x + input
      y = y + 1
      z = x/y
  except ValueError: 
      print("Error, please enter numeric input")
  
print (a, b, z)

Example of code, above, that I could make work but don’t necessarily understand. I understood when ValueError was discussed in class but haven’t really applied it since (and hence forgot how it works). 

How variables work: because I don’t truly understand what values will be returned from a loop or input I have had to develop work arounds. For example, the when True feature of an input can help me to weed out erroneous inputs but every time I have tried to use it, it turns into a session of looking up examples and then using trial and error until it works. And, oh yeah, I don’t know why it works.

# initial set up of variables
  # x is the total variable
x = 0
  # y is the number variable
y = 0
  # z is the average variable
z = 0
  # b is a dummy variable used to stop the loop
b = 1
# getting the input
while b > 0:

  # getting the input
  try:
    input_number = raw_input("Input a number:")
    if input_number == "done":
      b = -1
      #stops the loop
    else:
      input = int(input_number)
      # does my math for me
      x = x + input
      y = y + 1
      z = x/y
  except ValueError: 
      print("Error, please enter numeric input")
  
print (x, y, z)
	
	This code is an example of the work around (using the variable b) I have to come with to direct the code. If I understood True I would be better off (more elegant). 

I have had my differences with Trinket: trinket is a neat application.  I can definitely see how it will be useful in the academic environment and how it can be monetized. It is getting pretty good reviews online as well (assuming Elliott didn’t leave them himself). The only drawback to using Trinket right now is that there isn’t a lot of documentation or google-ibility to application. This has limited me somewhat in my ability to understand what I am doing. As an example, I have yet to make the remix feature work. Maybe it can make my life easier but I just cut-and-paste now. I know Elliott explained this in class but I can’t remember how to use it.

The book is soft on examples: the book is barebones. I like that it is free but without a few more examples, I have difficulty understanding the material. Additionally, the book doesn’t give a proper name to some things and so when I try to look it up in other books/google I get no hits (e.g. guarding).

I hate github.


Things that are going well:
I really like Python. It looks to be a very dynamic language that is relatively easy to learn. Every time that I have thought of an application that I would like to be able to write google has shown me that it is possible (i.e. someone has already written it). An example is that I would like to be able to write a stock screener that a python program would update for me using data from the web. Totally doable and totally a time saver. I look forward to more python work.
# set up of the program
import turtle
from animations import setup


# setup the turtles like I want them
tina = turtle.Turtle()
tina.shape("turtle")
tommy = turtle.Turtle()
tommy.shape("turtle")
tina.color("red")
tina.penup()
tina.forward(25)
tommy.color("blue")
tommy.penup()

myscreen = turtle.Screen()
setup(myscreen)

# clicky (x, y)
def clicky(x, y):
  tina_loves = raw_input("Does tina love tommy? (type 'yes' or 'no')")
  if tina_loves == "yes":
      x1 = x - 25
      y1 = y
      tina.goto(x, y)
      tommy.goto(x1, y1)
  else:
      x1 = 0 - x
      y1 = 0 - y
      tina.goto(x, y)
      tommy.goto(x1, y1) 
  
myscreen.onclick(clicky)

	This is an example of code that worked and made me excited. I know it is simple but I actually got Tommy to follow Tina around. It was painful for me (i.e. need a session with Elliott but it worked and I am happy). 

I can see how it can get me to my end goals: see above. Also, I like to think that this class is a good introduction to coding. Since I have absolutely no background (or language) skills, everything is new to me and I feel that it has been on a level is appropriate to my level.

I am actually happy when I can get things to work: it isn’t often that I am actually happy when I do homework for a class. This class is an exception. There is something in the limbic cortex that must be linked to solving a frustrating problem. My only complaint in this department is that there are often many different ways to solve problems and my way isn’t always the most elegant (I figure this out after looking at some other people’s submitted work).

This is class seems to be pointing me in the direction I want to go: I truly feel that I will have a good grasp of the material and will be able to self-teach by the end of the class. I don’t think I will have time to take any other coding classes before I leave and so this is my one chance to find the resources I will need later in my learning. I fully plan to use python to write some code to make my life easier (hence the book Automate the Boring Stuff). Since it would be impossible to learn all of the things I need in one semester, resources and places for help later are paramount.





