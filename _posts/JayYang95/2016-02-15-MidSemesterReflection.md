---
layout: post
author: JayYang95
title: "Jay's Midsemester Reflection"
---

Since most of my experience in coding has been in Java, I chose thise class hoping to expand my knowledge of coding to include Python, and 
I have not been disappointed. Although I am familiar with most of the concepts we covered over the semester, I have still learned quite a
few things about Python that differ from Java such as the transition from static typing in Java to dynamic typing in Python, something
that I highly appreciate because it requries me to type less. Additionally, it has been somewhat difficult getting used to the syntax used
in Python. Often times while coding, I find myself accidentally coding in Java syntax, mainly when it comes to for loops.

for(int i = 0; i < n; i++){...} 
vs 
for i in range(0, n) ...

Another cool thing about Python is that brackets aren't required to indicate if a chunk of code is inside a loop or function. Instead,
only indents are required. This simplified method makes it easier to read for me and again, requires less typing, which is appreciated.

I took COMP 110 some semesters ago and although it was simple enough, I felt I had learned almost nothing about coding. Whereas in this
class, I felt as if I have already learned more about Python than I learned about Java in COMP110. I believe that the approach of 
slowly moving up in concepts is an effective way to learn. For example, we first begin this class with very messy and lengthy code which
got the job done, like our first turtle exercise:

<iframe src="https://trinket.io/embed/python/8764885c49" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Then we learned new concepts such as loops and functions that helped us to shorten and clean up code.

I believe that I have done well in most of the exercises as I am already familiar with the concepts we have covered so far. However, I
am confident and that we will definitely cover things that I don't know and am excited to learn them. 

Something that frustrated me was the Clicky Turtle Exercise.

<iframe src="https://trinket.io/embed/python/ff73c1dfa7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Though my code was functioning as it was supposed to, there were a couple things that I wanted to do which I was not able to. The 
first would be to have all user actions including clicks have no effect on the program until whatever action that was going on was
completed. This pesky bug was evident in everyone's programs as the user could never spam click the mouse or the turtle would go 
haywire. The other thing I could not figure out was how to get the program to completely halt if the user clicked on a certain
quadrant. However, I recently looked back at this problem and thought of a solution that might possibly work, which was to set a boolean
variable at the top to True. If the user clicked on the 4th quadrant, the bool variable would be set to False. Then at the very bottom,
instead of this:

def clicky(x, y):
  tina.goto(x,y)
  checkquad(x, y)
  
myscreen.onclick(clicky)

we could have something like this:
def clicky(x, y):
  tina.goto(x,y)
  checkquad(x, y)
  
if boolvar == True:
  myscreen.onclick(clicky)
else:
  print("Program Ended")
  
Since I have not had the time to actually try to implement this, this is only something that theoretically works in my head.

My problem solving attitude is to keep working at the code until it works. In other classes, I often coded my assignments in one or two
long sessions that may have lasted up to 5-6 hours each. There have also been times where I was completely stuck and went to bed, only
to have an epiphany and jump straight back to coding.

My problem solving strategy is to look at each small individual problem to the larger problem. I will work on one function of one class
(or module or whatever we call it in Python) at a time and make sure that they each function correctly by testing them. When I run into
bugs, I always check my code for logical errors first, which is sometimes my downfall when it comes to large coding assignments. There
have been times where I have scaled through all of my code for hours looking for some logical error only to realize I left out a 
bracket, mistyped a variable name, or some other stupid mistake.

Going off this, I feel like that one benefit of partner pairing is that other people can sometimes see your errors better than you can.
<iframe src="https://trinket.io/embed/python/e12e65c0ce" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In this poetry slam, me and my partner had but one obstacle left, and according to the logic I used, I could not understand why the
code was not working. However, my partner was able to locate the error to be me accidentally declaring two variables inside a while 
loop instead of outside of it, so that through each run of the loop, the variables would reset to whatever value I had set it to.
