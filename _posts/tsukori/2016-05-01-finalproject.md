---
layout: post
author: tsukori
title: "Final Game Project: Hangman Recoded"
---

The original hangman game: 

<iframe src="https://trinket.io/embed/python/02cefbfd83" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The final product:

<iframe src="https://trinket.io/embed/python/cebc13bd85" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I had a really hard time picking a final project; I was not sure if I wanted to do a game or data analysis. It sorta got into the last minute so I just ended up choosing a game project since the game group was a lot smaller and honestly data analysis sounded really boring. The game project group helped me decide to remodel my hangman game to be more interesting and have more replay value rather than just hitting restart every time you wanted a new word. I am actually really happy with how it turned out, there's bits of my humor in it and it's just a lot more satisfying all together. Of course there's a few regrets that I have with deploying my kid into the world, but that's just what a parent has to deal with. 

I was able to complete all of my milestones, which I thought were ambitious enough to make my new game more fun and interesting. I hit little snags all throughout the process, the largest one being how I handled variables, which became extremely taxing and forcing me to need to refactor my code twice. Elliot really helped me when he answered my 4th game update pull request, using a dictionary for all of my variables and then calling that globally into functions made everything cleaner and solved that issue entirely. Importing images was a lot easier than I expected, I always had that in the back of my mind thinking that it would be a big hassle but it was simple and they helped make my game funnier/more interesting. 

I started off with just writing out and drawing a big picture of what I thought was happening. I spent a few days doing this, the thought process behind this was to mimic what I did for the original project since that proved to be really successful. This time around though, I guess I did not plan as extensively as I thought (well I also added stuff that I was not originally intending to add so I think that's a bit of the issue). In my planning stage I definitely should have refactored my code and reworked where I thought modules and functions were going since this set me back a lot in the long run. I pretty much had a chain of inheritance happening from one module till the last and this caused me a lot of headaches when I was moving forward; what seemed like a clever idea to reduce the amount of importing I had to do, was actually a foolish attempt and a mess waiting to happen. In my new code, I imported important modules very specifically and it made the tops of the modules actually look better in my opinion. In the future, I think a cool/useful trinket ability is to drag the modules around to reorder them (just in case you were looking for functionality input).

When I got into the actual coding portion of the assignment, I thought things were going well, everything I wrote was working as I wanted to, but then again I tackled the really simple stuff first. I would make each individual part of the program in a separate trinket first so I could make sure it was working, and then I would integrate it into my main program and connect it that way. I think it is important when doing projects to set goals of differing difficulty so you get that feeling of accomplishment and you can use that to motivate yourself to get more done in the future. This part of the process was really long and frustrating so I do not remember all of it clearly, just different parts of making everything work and then it breaking and working again and it was just a roller coaster of coding that I am all too familiar with.

The last home stretch that I completed today and part of yesterday was 100% the most difficult part of the entire project. Having the bulk of code there as well as so many workings parts but still broken parts only made me more frustrated. Eventually I just created a new trinket and rearranged my modules, rereading everything and re-familiarizing myself with the code I had written previously. This process helped me to better import my code into the modules and link up only what is absolutely necessary instead of linking everything. The last thing I did was work on the end game screens, which turned out to be a lot more fun than I expected. I am happy with the result and I hope whoever plays my game makes it far enough to see all of them. 

My attitude for this program was a lot "calmer" than before, if that makes sense at all. I thought about it more and did not try to force things to happen. I took my time working on the code and gave myself a relatively relaxed schedule but I still had quotas of what I needed to be done with. I am not sure exactly what to say about my skills though, I feel like I still have the same skills I had before, just more refined/efficient. 

I feel like I gained a lot from this class, I thought I was already a pretty decent programmer, but now I feel more confident, especially with knowing python now. I did a lot of cool stuff in this class thanks to turtle and it was definitely an enjoyable experience. I learned about in person coding meet ups, which I will definitely be keeping an eye out for in the future; they really opened up my eyes to the scope of people that are programmers as well as the things that can be done with coding. Also just the people in the class showed me a lot as well, they had differing levels of experience with python and programming in general but they were able to make such amazing projects, it was very humbling. I came in to the class with intermediate coding skills in Java and now I feel like I have learned enough python to where I can teach myself more going forward and make python a language I am proficient in. That was my main goal for the class so it is pretty great to feel like I accomplished it. 

At this point I just feel like I am rambling about the class and the project because I have not hit the word limit but I really have nothing else I can say about the class. It was a great way to learn how to program in python and it exposed the students to a lot of things that can be done with code. 

Functionality Milestones: 

 - [x] Allow user to click on keys on the screen
 - [x] Give points to user for guessing words correctly
 - [x] Allow user to enter their own word list
 - [x] Create 3 different difficulty levels 
 - [x] Improve on screen text to be more descriptive and helpful to the user
 - [x] Increase difficulty based on score 
 
 Visual Milestones: 
 
 - [x] Change the color of keys when they are pressed
 - [x] Make completion screen more exciting by importing outside images
 
Completed plan completely crossed off purely for self satisfaction reasons. 
 
~~1. Think out changes, start planning them with pseudo code and concepts~~

~~2. On screen click keys that change color~~

~~3. Implement score system~~

~~4. Implement level system, with ramping difficulty~~

~~5. Update on screen text to include more information~~
 
~~6. Unique screens for levels and end score~~
 
~~7. End game animations for 4 different score ranges~~
 
~~8. Allow user to import words~~
