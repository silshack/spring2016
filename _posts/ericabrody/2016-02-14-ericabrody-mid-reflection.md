---
layout: post
author: ericabrody
title: "Erica's Mid-Semester Reflection"
---

Mid-semester reflection:

Since I am reflecting on the semester so far, I took this opportunity to review most of the readings and exercises we have done so far. Also, I hope this review helps me with the Tetris Turtles refactor exercise.  So far, I have learned a lot. 

I feel pretty confident using turtle – remembering that turtles write, rather than print. I can request user input, check if the input is numeric, and manipulate strings, numbers, and lists. I am getting more comfortable passing data into and out of functions, using lists, and dealing with issues on Github (remembering to close them by using the fixed statement). 

I was most excited by the clicky turtles assignment – that I had a vision of creating fireworks and was able to make it happen. I felt pretty spiffy deploying 12 different turtles at a time to keep the speed of the program high and was glad that I experimented with turtle.speed greater than 10, even though all the programs and documentation I had seen showed maximum speeds of 10. I think I also enjoyed using the many statements to control each turtle, holding off on using a list to loop through the turtles with more elegant code. I plan to refactor this clicky turtle before working on tetris for practice. 

There are two algorithms that I struggled learning related to 1) functions and 2) lists.
I found it very counterintuitive that when something (a value, a string, etc.)  is returned from a function that this variable is not ready to use in my main program. For example, in the trinket below, I wanted to be able to use the variable pay in my main program by writing something like print ("Your pay is " + str (pay)). I am getting used to the way it works, where I can call the function and assigning that call to a variable that can then be used.

<iframe src="https://trinket.io/embed/python/924c16f464" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Also, now I can more confidently say that this program from Chapter 8, Exercise 1 returns “None”
<iframe src="https://trinket.io/embed/python/dca753c951" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

So in going through lists in loops, I have had to get clear on how to go through the actual items in a list vs. going through the count of items in the list using the index and when you would want to use each type of list/loop. If you want to do something to items in a list, you use a program like this and a statement like "for var1 in list" - in this case, the list was a list of lines in a text.
<iframe src="https://trinket.io/embed/python3/a90e216cd8" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

in contrast with the following example, where the loop uses the index of the items to make a list into a well-formatted sentence.
```
words = ['grape', 'kiwi', 'apple', 'banana'] 
result = ''
for i in range (len(words)): # which is the length of the list of words
  if i != (len(words)-1):
    result += words[i] + ", " 
  else:
    result += "and " + words[i]
print "My shopping list is " + result
```
When reading the string chapter- where everything set to a variable, tested out built-in functions and methods with actual values – I created a teststring trinket and tested out different items, exercises in it, commenting out old parts and then running new parts, so I had most of the homework done by the time I finished reading the chapter. :Smile
<iframe src="https://trinket.io/embed/python/bcd0df56cd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Since these exercises took less time than expected, I played around with exercises 3 and 4 using the turtle to write rather than standard print commands.

My biggest frustrations come from syntax - I had trouble remembering to include an empty parentheses () after calling a function that didn't need an argument. I remember staring at a program for a long time before it would run because of this problem.

I think the pair programming has a lot of potential to support learning and developing better formed programs (and my husband, a professional programmer attests to this); however so far the pairing feels very rushed since we have limited class time and, as much as I would like to take lots of time to work together, we all have many competing demands with other classes and jobs. So far, I feel like the times I slowed down with my partner so we could understand each other's thinking is when we both get stuck on the problem, otherwise we just forge ahead. In the future, I want to try harder at slowing down and working together better as navigator and driver.

As for problem solving strategies, I most commonly use Command + / to comment out sections of programs to see what different parts are doing. I copy a lot of code and build from that either from the book chapters or my old programs. At times, when I copy from the book, I may not be fully learning the concepts as well as possible, so I want to be more thoughtful about this as we go forward. I found it very helpful to break down the requirements of the program into small bits that are psuedo code - I used this to create the firecracker program. With loops, it is helpful to take an example and consider what the program will do with a particular set of characters, etc. Also, using print statements to see what is going on the program is helpful.

It is also interesting to realize that there are several ways to approach any given problem, sort of like organizing thoughts in an 
essay. When examining text, you can look at or manipulate characters, words, or lines of text.

Going forward, I would like to get better at trying the "time box" strategy, because I frequently just want to sit at the computer until I find the right answer. I also want to take more time to look at my classmate's code (which I have started to do) to get more ideas about ways to code. I hope to reflect even more effectively going forward, but, frankly, the reality of grad school with lots of competing demands sometimes makes it hard to focus on learning rather than solving the problem at hand and moving onto the next item on my list. I think the framework of this class really encourages and supports a focus on learning, but I sometimes struggle with keeping that focus.

In one of the early class notes, there was an example of data visualization, I would like to learn how to do that, as well as use Python to manipulate datasets, if possible.


