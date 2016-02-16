---
layout: post
author: jamesma560
title: "James Mid-Semester Reflection"
---

I’ve certainly learned a lot this semester. All in all, I’d say this semester so far has been akin to the “tool belt” metaphor 
I’ve heard you employ in class. Looking back to the first day of class, I’d say I had some tools (maybe a hammer and some nails) 
but I wasn’t really confident in how to use them. I had taken some intro computer science courses throughout my undergrad (C++ as well 
as Python), and I had been messing around on Code Academy over the summer, and I had even started to pick up some Python at my job as 
well. So I was pretty familiar with the syntax and reading Python, but I hadn’t really done more than novice scripts myself, so this 
semester has really been about adding new tools to the novice foundation I had developed before coming in to this class. 
I think one of the first big revelations for me was the need for a programmer to be cognizant of what data types they want to work with 
throughout their program. During the first several assignments for this class, I noticed that most of the errors I was running into 
involved the program not knowing what to do with invalid data types. The most poignant example that comes to mind would be when I would 
convert a user’s input from a string to an integer for computation, but then when I would try and display the result of that computation,
the program would run into an error. 

So for example I would have code blocks like this:

<iframe src="https://trinket.io/embed/python/9ecba335ff" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


The "parse error" on line 4 would pop up in the print statement, since I was trying to concatenate an integer with a string. 
So the ‘tools’ I picked up from running into these errors are the str(), int(), and float() methods. Using these tools I was able 
to get my data types straight and avoid the error above:

<iframe src="https://trinket.io/embed/python/c47e841146" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I even learned how to do this within the display statement:

<iframe src="https://trinket.io/embed/python/397330ef3a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Thus taking advantage of nested functions and having one less variable to keep track of.

Speaking of functions, another lesson that has stuck with me during this first part of the semester involved the importance of refactoring. Coming into this class, “refactoring” was one of those computer programming jargon words that I had vaguely remembered hearing during the Computer Science courses I took in undergrad. I sort of knew what refactoring was, but admittedly I didn’t understand it’s importance fully. But when we went over some of your refactored code (I think it was your treasure hunt game), and at the code of other people who had refactored their programs, the difference in readability became apparent. 
For example, I think the most poignant example the importance of refactoring making itself apparent to me was your congratulations() function. 
First off, being completely new to Turtle at that point, when you ran it I was blown away. I can only hope to write a turtle 
program/game that’s half as cool as that. But anyway, when I looked for it in the main.py of your code for that program, I was shocked 
that all that animation only took up one line.

As you explained further however, the real “guts” of the function was on the animation.py file which was attached to your program. And 
these “guts” were much more intricate and complex than the call statement “congratulations()” let on:

<iframe src="https://trinket.io/embed/python/0216c31ed3" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I think that’s really when “refactoring” made sense to me. The fact that a programmer can spare the reader from reading dozens 
(or perhaps even hundreds!) of lines of code makes it clear to me why “refactoring” seems to be such a highly valued virtue in computer programming. 
But despite me learning this lesson I feel like I’ve done a poor job of incorporating refactoring into my programs. In fact, outside of the assignments which have specifically 
mandated that we refactor, I don’t really think about refactoring that much while I’m in the midst of programming. I think it has 
something to do with my coding habits up to this point. Coding is still a very time consuming process for me, so whenever I finished 
a program that works (or a program that I think works), I never stop to ask myself: “is there a way to refactor this code to make 
it more readable?”. Instead I end up just turning it in because of the risk of messing up my program during refactoring just doesn’t 
seem to be worth the effort. But I guess the glaring solution to this would be to refactor the code as I go. And I guess that’s one of 
the major improvements that I am looking to make throughout the remainder of this class. 

Speaking of improvements, I think the largest improvement I wish to make is with these Turtle programs. Walking into this class, 
the whole concept of coding to make a game or animation was completely alien to me. Before, in other intro to computer programming
classes, the code we wrote was geared to perform certain tasks: like order this list, find and parce out this string, etc. 
I had never really coded to “entertain” a user. So because of this lack of experience, I feel like all of my Turtle programs have either 
been really, really simplistic, or really, really boring. Most likely both. Another frustrating aspect of the Turtle exercises has been 
that at many points I’ve had to scale back my initial goal for the program because I just don’t have the knowledge and skill to pull it 
off. For instance, one thing I've wanted to do is print words to the screen without having to use a Turtle. I also wanted to get better
at exploiting the onclick() methods.

But I hope that as  I move forward that I’m able to add more tools to my Turtle tool belt, in order to get them to where I want 
them to be.



