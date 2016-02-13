---
layout: post
author: wagerpascal
title: "Jason's Reflections"
---

	I came into this class with some coding experience- mostly with Arduino pseudocode and some embedded programming, as well as some data analysis things from a Matlab class I took 4 years ago. I decided to take this python course due to my interest in networking and socket programming, as Python is one of the major languages that is used for it.
	Content-wise, I came in knowing about the basic nature and logic of most things up to loops. However, I knew near to nothing about the specifics of Python and how it was structured. Let’s take a peek at my “Logic Turtles” post from way back when:
```
chair_color = raw_input("What color should Chair be now?")
chair.color(chair_color)

try:
  side_number = int(raw_input("How many sides are in this polygon?"))
  total_angle= 180*(side_number - 2)
  #print(total_angle)
  #print(total_angle/side_number)

  side_number_1 = side_number

  world_size = (side_number/2)*100
  chair.getscreen().setworldcoordinates(-world_size,-world_size,world_size,world_size)

  boardcount = int(raw_input("How many boards would the Mongol horde hoard, if the Mongol horde could hoard boards?"))
  
  if boardcount % 2 == 0:
    chair.fillcolor("blue")
  else:
    chair.fillcolor("red")
  
  desptimes = raw_input("Is your drawing full of determination?")
  if desptimes == "yes" or desptimes == "Yes":
    chair.speed(10)
```
The way that variables were set up, in that the way of which new variables replaced other variables, was a bit sloppy. While it is conceptually easier to follow what is going on, the code can be cleaned up so that the input directly feeds into all of the processing that occurs. It’s still a problem for me sometimes. The example I just showed may not be the best example, as our assignments typically do not require a large quantity of various variables that may be changing, but it is still an issue that appears in my code; defining more functions might help some of the problem.
The most exciting part of this class are the options; coming from a background that only really demanded one correct way to do the problem correctly, it is refreshing to be able to sit and consider “Well, how about I try it this way?”
For example, I (incorrectly) did the poetry slam exercise by approaching it from a pure lists standpoint, rather than use the turtle library. However, I would argue that this code performs at the same capacity as a classmate’s code that uses Turtle. In some cases, it might seem that it takes less code to display it, as drawing is no longer a concern:
```
words = []
count = 0
words_new = ''

while True:
  try:
    answer = raw_input('Gimme a word\n')
    if answer.lower() == "done":
      break
    
    else:
      words.append(answer)
    
  except:
    print("Invalid input")


for pieces in words:
  words_new = words_new + " " + words[count]
  count = count + 1

words_new.strip()
print(words_new)
```
Of course, the downside of such freedom is knowing where your limits are. Let’s take the Clicky Turtles Exercise for example (incidentally an assignment that a lot of people seemed to have overextended). My original idea for this assignment involved a turn-based game of tag, where the user would have a “line of sight” where the target will move (similar to a treasure hunt, but more fast-paced in the end). During the process, I realized two issues: first, I needed to construct either a two-dimensional list or two separate lists that update themselves with the coordinates of where the turtle will go (also requiring predetermined coordinates at the beginning of the run). In addition, the timing/cooldown of which the turtle turns needs to be strictly timed (occasionally with poorly timed/smaller spaced clicks, the turtle starts spinning around due to the rapid updating of the points. These issues (especially the turtle pointing control) demonstrate the dichotomy between a conceptual idea and the actual execution of said idea. It may be simple to explain what the program does, but some of the things that humans take for granted: tracking moving objects, depth calculations, etc., are things that can’t be easily implemented in a few lines of code.
I would say that after that exercise, I’ve taken a lot more precautions of ensuring that I am not overextending or being too ambitious about what I would like to take on. Before, I would simply just open Trinket and start coding with the hope that eventually I will reach the end. However, since that assignment, I’ve taken the time to draw out what I’m expressly trying to do; rather than try to tackle a goal that may encompass various tasks, I can instead break everything apart for better planning and management. 
Of course I still have a ways to go. An issue that I would like to work on is that often times with these assignments, I hope that there is a roundabout method of implementing some kind of function or method that can solve my problem quickly. While this tactic may work for basic exercises or simple projects, it immediately begins falling apart with problems that are multifaceted or require a number of goals. For example, in the Turtle Clone Treasure assignment, I needed to calculate the distance between the user-inputted point with the point of the treasure. For this, I used:
```
while still_going:
  # Get user X and Y coordinates.
  # Make sure to handle bad inputs.
  user_x = int(raw_input("Choose an X coordinate between -100 and 100"))
  user_y = int(raw_input("Choose an Y coordinate between -100 and 100"))
  
  if abs(user_x) > 100 or abs(user_y) > 100:
    print("Input Coordinates too large, please try again.")
    still_going = True
  
  # Make Tina go to the user's X and Ys here:
  
  tina.goto(user_x, user_y)
  
  # Give the user feedback on how close they are to the treasure here:
  
  pytha_x = treasure_x - user_x
  pytha_y = treasure_y - user_y
  
  dist_1 = math.sqrt((pytha_x**2)+(pytha_y**2))
  dist = round(dist_1 , 2)
  
  print("You are " + str(dist) + " units away.")
```
I didn’t think this at the time, but I now realize that I just could have easily used the turtle.distance() method and saved myself the time of doing it manually. However, the act of first doing it all yourself leads to you better remembering how to do it, and potential methods or ideas that ca be used in future programs. Bit of a nuanced example, but I occasionally hang out/work with computer science majors, so I end up hearing snippets of their thoughts. There was a person who was attempting to import a library that would allow him to do a square root in his program, but it simply wasn’t working. So he just manually made a function that calculates the square root, rather than continue to fiddle with the library. In the end, he probably saved more time and project momentum than fiddling with it. While it may not be practical, it is still important to do things the hard way the first go-round. Therefore, I should really start approaching problems from this angle.
	For this upcoming half-semester, I’m planning on really focusing on learning the basics, especially regarding cutting down on abusing specific methods or functions when doing assignments (while ones that may cut down on small calculations or actions are okay, the ones that solve a huge portion of an assignment are considered “roundabout”). While I was just sketching out quick diagrams of my plans on scrap paper or a whiteboard, I will try to begin keeping a notebook to start sketching ideas out, and commenting my code to divide up sections and their functionality. However, judging from the Tetris game that is due soon, it looks like this class will be picking up the pace of complexity, which is rather exciting. 


Referenced Programs:
Logic Turtles:
<iframe src="https://trinket.io/embed/python/5bc9bc9035" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Turtle Clone TreasureHunt:
<iframe src="https://trinket.io/embed/python/f7a67a2556" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Poetry Slam Turtles:
<iframe src="https://trinket.io/embed/python/84966596b1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
