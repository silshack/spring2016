---
layout: post
author: EternalFootman
title: "Kit's Mid-semester Reflection"
---

I got my first taste for any kind of programming in 161 last semester; we spent a few weeks on HTML. The option was given to build a website by using a template or by designing everything from scratch. I suspect that the first choice was easier, but I wanted to understand how it all worked. My result was a plain, rather pathetic thing, but I had made it and was terribly proud. I discovered that it sucks you in; the actual assignment goals matter less than the need to make it as good as possible. I’m fond of creating things, and this is apparently no different.
I catch myself having the same tendency in this class. The assignments don’t always catch my interest, but when they do, something like this happens.
	
<iframe src="https://trinket.io/embed/python/c53d8852b3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This started as one of the early assignments – I don’t even remember which now. I remember thinking then that there must be easier ways to do what I wanted, and I’ve been adding them in as I learned them (functions, modules, and multiple turtles were not part of the original program. The newest and most exciting addition is the .tracer/.update bit, which makes the opening much less tedious). I’ve probably spent more time on it than I have on most of the graded projects.
The chessboard says a lot about how I learn, though I forget it sometimes. I don’t do well if I don’t understand the purpose of an assignment.
	
```
print '\n', '8.2:'
weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
fhand = open('text.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    if words [2] in weekdays[:]:
      print(words[2])
```

I wrestled with this program for longer than made any sense. Eventually I realized that part of the problem was that I didn’t know what it was for (the goal had not been transferred from the chapter to the assignment page, and I had forgotten it since doing the reading). Doing something with no purpose made it completely pointless, as far as I was concerned. I suspect that that’s why I get frustrated with some of the homework but can cheerfully spend hours on my chess program. The solution is probably to identify the goal of each program, even the small ones, before starting on them. In related news, I just noticed the ‘Why?’ section at the end of this assignment; it’s a very apt example.
	I’ve only just begun to develop a problem solving strategy, but I’m excited about it as long as I can remember to apply it. The Tetris program from this weekend was intensely frustrating for many hours. Like Python as a whole, it was alarming because of the size and complexity; there were a great many things that I did not understand all crammed together. I only began to make progress when I started to pick out the bits that I did recognize and use them to make sense of everything else. Going line by line and looking up the unfamiliar terms was a slog, but it worked (for the most part). One of my long-term goals is to be more efficient in improving my understanding, which may just take practice. A problem solving attitude is not something I’ve thought about much, but patience wouldn’t be a bad one to cultivate. The solution mentioned above, to retain a clear idea of the purpose of each project, would be helpful as well. Something that you talked about several weeks ago was taking a step back from a frustrating problem and rethinking what question needed to be answered is related to that.
	The partner exercises are helpful sometimes (because so much of this subject is self-taught, we’ve all developed slightly different methods of doing things), but it often feels similar to what we do for homework. We’re still experimenting and brainstorming until we figure out how something works. This is an effective strategy, but I don’t like it being the only one. There have been a few class days when we all looked at each other’s’ work on the projector and you talked through the code; that gave us a chance to see the many different ideas and really understand them. I’d like to see more of that approach, as it pairs well with the flailing and experimentation that we did over the homework. Practically speaking, the pair workshops become problematic if we don’t finish; coordinating schedules to meet (even virtually) outside of class can be very difficult in the twelve hours before the work is due.
	As far as long-term (well, for the next ten weeks) plans go, that again goes back to having a purpose. The turtle programs are fun, but I don’t know how they relate to anything else. Having come into the class with only the vaguest idea of what Python even was, I now want to know where it is used apart from in games. Apart from that, I suppose my clear plan is to learn enough about the context, use, and options available in Python to develop a clear plan. How’s that for meta-cognition? To make it more concrete, I would like to see more real-world examples in class that apply the concepts we read about and practice as homework, along with explanation about why they work (and why they’re the best way of doing something).
Another goal is the completion of my Alice In Wonderland program. 

<iframe src="https://trinket.io/embed/python/ecb44ac508?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It would be pretty excellent to get through the whole book, using different bits of code for the different chapters (word games with the caterpillar, an animated croquet set, size changes from the Drink Me bottles, etc). Thus far, I’ve gotten down the rabbit hole but no further (the Garden of Live Flowers is technically in a different book; the chess theme is related but separate). The Caucus Race might make an appropriate segment. I’ve found that having a theme makes the creative assignments easier. Using the established narrative of a book that I love does two things that I wrote about above. For one thing, it gives me a goal to work towards that is vague enough that I can apply whatever skillset I’m cultivating at the moment. For another, the narrative keeps the work interesting; I’m no longer wasting time trying to think of a brilliant concept, so I can spend it writing a more complicated program.
