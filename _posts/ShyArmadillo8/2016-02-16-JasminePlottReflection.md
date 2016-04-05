---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Midsemester Reflection"
---

  When I came into this class, I had very little and mostly unpleasant experiences with learning how to program.  I had been scarred by the Intro to Computer Science class that I had taken as a sophomore in my undergraduate years.  The class had started out simple enough, but as the semester progressed, that class slowly became my nightmare; there were no readings to help us better understand the concepts, the lessons were primarily centered on watching the professor type different code on the screen and exclaming it "Well look at that!", and there was no feedback on our assignments so if we did something wrong, there was no real guidance as to why it was incorrect.  Needless to say, I was very concerned that I would have a similar experience in this class, but I knew that learning how to program was an important skill that I needed to be comfortable with and understand during my time in library school. 

  Fortunately, this class has not been nearly as horrible as I feared it would be.  I would still definitely consider this my most difficult course, but I feel that I am learning practical skills that I can put to good use and that will be applicable to my future career.  I was so pleased the other day when a librarian visited one of my classes and demonstrated a visualization tool that he and a team had created using Python. Aside from how this class applies to my future as a librarian, I also find that I appreciate the end products of finished programs because I can understand how much time and effort went into them.  I would have to say that the reason I have come to enjoy this course so much though is because of how far I feel like I've already come, and it has not even been half a semester!

Here is the first Trinket program that I created for our first homework assignment:
<iframe src="https://trinket.io/embed/python/9475228430" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  I remember looking at this code and thinking about how I did not understand it that much, but I knew that it did what I wanted to (which was creating semi-circles and a star).  Back then, my knowledge about Python and what you could do with it was limited to moving forward, left, right, etc., but when I was going through my Trinkets I had created in preparation for this assignment, I realized that I actually understood what all the code in the Trinket meant and that, if asked to, I would be able to talk someone through it. This is the code that I used to draw semi-circles:

```
for x in range(180):
    tina.forward(1)
    tina.right(1)
```
  
  At the time, I had no idea what "for" loops where, but looking back on this I realize now that for each degree in the specified range, Tina is supposed to move forward 1 and right 1.  This gradually creates the semi-circle.  I also have the code sample that I used to draw a star:

```
def draw_star(size, color):
    angle = 120
    tina.fillcolor(color)
    tina.begin_fill()

    for side in range(5):
        tina.forward(size)
        tina.right(angle)
        tina.forward(size)
        tina.right(72 - angle)
    tina.end_fill()
    return

draw_star(25, "yellow")
```

  Now that I have learned about them through our class exercises and readings, I recognize that this is a function for drawing a star with a "for" loop to draw the five points of the star at a 72 degree angle.  The "begin_fill" and "end_fill" portions of the code are what instructs the program to fill in the star with the color specified when the function is called.  Looking back at my first assignment shows me how far I have truly come in being able to not just research the code that I want but being able to also understand what it means and how it is being implemented.  This is incredibly important, since I realized that sometimes if you do not understand the code you are working with, it can cause problems.  I realized this perhaps most poignantly in the Chapter 5 exercises.

Here are my fixed Chapter 5 exercises. The first is 5.1:
<iframe src="https://trinket.io/embed/python/8a5383a746" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This is the code for 5.2:
<iframe src="https://trinket.io/embed/python/09b3da08e4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  In hindsight, I wish that I had saved the code that I had originally turned in that was definitely incorrect to show what I had fixed. However, this is the final fixed portion of the code from 5.1 that I struggled the most with:

```
while still_going:
  try:
      line = input('Enter a number:')
      line_1 = float(line)
      total = line_1 + total
      count = count + 1
      average = total / count
  except:
    if line == 'done':
      print("Done!")
      break
    else:
      print("Did we forget what a number is, or did our fingers slip? Please enter a number.")
      count = 0
      total = 0
      average = 0
```

  For some reason, I just could not wrap my mind around loops! This concept completely baffled me, and it did not help that I had copied the code from the book to use in my program.  As I alluded to above, I had not fully understand the code from the book (although I thought that I had), and this got me off to a bad start in creating the above code.  I am particularly proud of the above code because this is what I was able to create in less than 10 minutes when I started from scratch.  This lesson taught me that I need to understand what the code I'm writing means and how to best implement it into what I am working with even if it is just a step at a time.

Here is the portion of code from 5.2 that I struggled the most with:

```
while still_going:
  try:
    line = input("Enter a number:")
    if line == "done":
      print("Done!")
      break
    else: 
      line_1 = float(line)
      sum = sum + line_1
      count = count + 1
      if smallest == None:
        smallest = line_1
      else:
        if line_1 < smallest:
          smallest = line_1
      if largest == None:
        largest = line_1
      else:
        if line_1 > largest:
          largest = line_1
  except:
      print("Did we forget what a number is, or did our fingers slip? Please enter a number.")
      sum = 0
      count = 0
      largest = None
      smallest = None
```

  Again, I had been confused by the readings because they advised using max() and min(), which I did not realize required lists to use. I had also copied over some code from the book that led me in the opposite direction of where I needed to be going.  This was a pretty difficult exercise for me, since I do not think that I was ever able to completely get it correct in the end, but I found that starting from scratch was one of the best decisions I had made. I believe that this also taught me how to write this code the "hard" way so that I could appreciate the use of max() and min() later on.  I also now have a much better understanding of loops.

  It was after completing these exercises that I realized I needed to learn how to develop some problem solving strategies for when I did get frustrated and stuck with my assignments as I had with the Chapter 5 exercises.  One of the biggest problem solving strategies that I have implemented with time (other than showering or taking a break for a cup of tea) is printing the variable type.  This came in handy for exercise 6.1 in particular.

Here is the Trinket for exercise 6.1:
<iframe src="https://trinket.io/embed/python/6bcb8c5c8b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

  I remember that this problem took a while for me to figure out, but I was able to do so with persistence, patience, and printing the variable type, which was important for this exercise.  This portion of the code was where I used my problem solving strategy:

```
length = len(user_input)
last = length - 1

index = last

while index < length:
  letter = user_input[index]
  print letter
  index = index - 1
  if index < 0:
    break
```

  What I had to figure out in this code was how to get the index to start at the last letter in the word and register that as a number rather than a string (which it was).  This exercise challenged me to think about the different ways that I would be able to do so with the code that I had learned from the readings.  Using my lesson I had learned from before about starting from scratch and working with the code bit by bit, I was able create the variable "last" which served as the number for the last letter in the word.  Since my experience with printing the variable type and ruling out the possible problems presented throughout creating this code, I have used this as a strategy for working with the other programs that I have created for this class; I will continue to do so into the future.

  Looking back on these major milestones throughout my time in this course, I see that I have overcome some major obstacles and learning curves: being able to interpret and read code that I did not orginally create and understand at the time, starting with small steps to create my own code and understand new concepts, and developing problem solving strategies so that I can remain rational when I might be frustrated or inclined to give up.  Thinking about these milestones made me consider the goals that I would like to put into place for the second half of this semester.

  First of all, I have been highly concerned about how much time I have been spending on my programs.  I feel like I am definitely learning, but there are times when I feel like I am spending an excessive amount of time on assignments. I have started the strategy of beginning sooner rather than later on my exercises, and I am usually able to produce something. I want to develop strategies for what to do if I have no idea at all what to do. Ways that I could get around this might be reaching out to others for help be it classmates or finding online resources that seem plausible; the one problem I have with online resources is that I do not necessarily know who to trust or who to turn to, which might be good to know- is there such a list available?  I wonder if there is also guidance on about how long we should be spending on these assignments-how much is enough?

  One thing that I really have enjoyed and would like to continue throughout the rest of the semester is pair programming.  While I have an idea of what is expected from completing the homework exercises, I find it immensely helpful to work with another person to accomplish assignments based off what we have learned in more difficult exercises. I like bouncing ideas and strategies off another person to see what we can create, which is usually better than what I would build on my own.  We all think in different ways, and I am always curious to see how someone else approached a problem and how they applied the knowledge that we learned in class.  I look forward to doing more assignments such as these throughout the semester, but I wonder if there is a way that we can keep the exercises we work on as pairs to what we complete in class?  Working around each other's schedules before midnight on that same day can be difficult to work out sometimes, but I do want to keep up the pair programming, since I find that it is a really fruitful, positive experience.

  Thinking about my experience so far in this class, I am going to focus on building my confidence with programming, learning more problem strategies other than printing type, rearranging my code, and working the errors that the code produces, and trying not to feel so frustrated when I encounter problems with my code. Even though I aim to improve these things, I believe that some of my strengths in this class are my persistence and ability to try to reach out and understand code that we have not gone over yet.  I also have become better at working with the strategies we are taught throughout the textbook and working to iron out exactly what more technical explanations of certain methods mean.  With these goals and thoughts in mind, I look forward to learning more and becoming a better programmer throughout the rest of the semester.
