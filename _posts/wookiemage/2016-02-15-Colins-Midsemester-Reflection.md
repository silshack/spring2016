---
author: wookiemage
layout: post
title: "Mid-Semester Reflection"
---
#Reflection
I came to this class with some expectations and some previous coursework in programming. I assumed that this course would be similar to my C++ course in college. I also assumed that my previous experience would always be helpful. I wasn\'t right.

This course, with its flipped nature, is not at all like my C++ course ten years ago. That course was very traditional in nature and used a textbook originally published in the late eighties. There is something to be said for doing things the hard way, and I do remember a lot of the concepts from that class, but there is a definite advantage to the setup of this class.

My C++ course started with the history of computers, worked our way through some basic assembly language programming before we ever started messing with the command line. That\'s also the furthest we got. We never learned how to interact with any other file, or even create separate files. We supposedly learned object oriented programming, but it\'s hard to really see the benefits when the extent of your program is converting military time to standard and displaying it on an ASCII-art clock. The fact that this class has already had us using short functions that call information from another text file is great. I also really appreciate that we don\'t spend too much time talking about the benefits of one kind of programming over another or get into in depth “discussions” of whether it\'s better to call developers “software engineers,” “computer scientists” or “programmers.”

This class is much more project based. We made something go on our first day:
<iframe src="https://trinket.io/embed/python/7c81b5cc31" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
It isn\'t much, but it really shows the emphasis is on doing, not discussing and I really appreciate that.

My previous experience with programming, limited though it may be, has almost always been helpful. Here\'s one example of where it hasn\'t been.
<iframe src="https://trinket.io/embed/python/448c8c4f8a" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I had a hard time understanding that Python allows you to loop through a list as many times as there are things in the list without prior knowledge of how long the list is. And that it allows you to declare variables in the loop statement is very different from how C++ does it (or at least how I remember C++ doing it). 
```
for line in fhand:
    split_words = line.split()
    for item in split_words:
      if item not in words:
        words.append(item.lower())
```
These for loops are super confusing. 
```
for line in fhand:
```
Is simultaneously declaring a variable (line) and declaring a loop that will run as long as there is another entity in the list fhand. Or at least that\'s what I think because I\'m not really sure how python treats text files called in this way. It seems to treat each line in a text file as another entry in a list. So this statement says for each line (which is arbitrarily named line, it could just as easily be for each x) in fhand do the following. I think that if you were to do the same thing in C++ you would have to declare the existence of line somewhere else, and assign it a value (presumably the length of the array) and then start the list with that information having already been ascertained. And if that info changed, then you would no longer have functioning code. That Python allows and endorses this ambiguity is hurting my head.


I do find that the problem solving strategies I used year before are still helpful here. The biggest strategy that I employ is giving myself lots of time to work through something. I like to start a new assignment the day it\'s posted whenever possible. That way I can finish it early if it\'s easy and if I get frustrated or it just isn\'t clicking, I can take lots of time away from the problem before it\'s due. This strategy has worked very well so far, but as the semester gets busier and busier it\'s going to be hard to find the time in advance to work on it.

Another strategy that works well for me, that I first started using in my C++ class, is breaking down the program into pseudocode in English before embarking on a large section of an assignment or, as when refactoring the Tetris Turtle, when trying to understand someone else\'s code. Here\'s a good example of that.

<iframe src="https://trinket.io/embed/python/d0b14e13d2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen=""></iframe>
On line 222 of the above embedded program, we are declaring a loop. My pseudocode would read something like:

Loop through all the items in the list pieces and for each one reverse the list inside that piece. Or at least I think that\'s what this means. I looked up negative ranges on https://docs.python.org/2.3/whatsnew/section-slices.html and it seems to say it reverses the function. 

Walking through the code like this really helps me see what isn\'t working the way I think it should or sections I don\'t really understand. In this case it helped my expose a few lines of code that I don\'t understand and that I need to further investigate. This led me to looking up the way that ranges function.  This walking through line by line can be very tedious, but because it\'s so meticulous you are less likely to miss anything.

Pair programming is completely new to me. We didn\'t do anything like that in my previous programming experience and I\'m finding it a little hard to get used to. It\'s hard for me to not want my hands on the keyboard, and when my hands are on the keyboard, it\'s hard for me to “slow down” and listen to what the navigator is saying. One aspect of pair programming I do like is how quickly we can spot simple mistakes: missing colons, parenthesis etc.  When you can\'t touch the keyboard and are steering the programming you have that opportunity to spot those mistakes before they throw you off. Really, my reticence to adopt this method is just my attitude. I have a hard time not "doing" something, and I\'ll need to just convince myself of the benefits of this practice.
