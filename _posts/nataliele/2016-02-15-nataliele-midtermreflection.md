---
layout: post
author: nataliele
title: "Natalie's mid-term reflection"
---

* What have you learned? 
Coding is fun, and hard, and frustrating, but rewarding when you get it to work!
* What has excited you?
Making Tina do things is my favorite. Also seeing other people's Tina and the creative things they do with their turtles.
* What has frustrated you?
Being stuck trying to make the program do what I want. When I was doing the Clicky turtle exercise I was really frustrated because I spent so much time figuring out how to make the shark appears in loop. I came upon the problem of not being able to use variable in function in other functions. I thought that was a Python design and didn’t think to consult the Internet! Previously I never really searched for solutions and just tried to figure out myself unless it's something new that I wanted to do. After the Clicky turtle exercise I realized I tend to just go straight to the internet, which is also not good. For example for the loop exercise I gave up too early and looked it up on stackexchange. I saw that people were using list so I couldn’t see past that to realize I could do the exercise without lists.
I feel I definitely need to find a balance because the answers on the internet sometimes are convoluted for simple things that I'm looking for.
I do wish I have more time to look for extra things to add to my code but that's ok. I think I will focus on getting the foundation down.
* My solving strategy now:
	 - For exercises where questions and tasks are well-defined: maximum about 30' per exercise. Then I'll go to another exercise and then come back. If when I come back I still don’t have a solution I'll try stackexchange.
	 - For turtle exercise where the scope is open: I usually spend about 2 hours in one sitting to make it work. If I'm still not happy Ill come back another day and spend some more hours on it.
	 - I think I need to work on conceptualizing the problem. My first instinct is to jump in and start coding and figure it out along the way. 
	For example this exercise below. I know that we'll need to loop and I would just try having 2 loops separated. I tend to want to see what the program returns to understand how it processes my code and then go back and look. So when I see that I only have the last sentence. I'll be like, ah ok so it only returns the last sentence ie the last "words" value, how do I solve that, maybe I will put the second loop inside the first loop. Perhaps if I spend more time thinking about the problem and write out pseudo codes that I want the program to do, it will be more efficient.
	
```python
prompt="Enter file name"
userinput=input(prompt)
file=open(userinput+'.txt')
wordlist=[]

for line in file:
  words=line.split()
  # print(type(words))
  for word in words:
    if word not in wordlist:
      wordlist.append(word.lower())
      
wordlist.sort(key=str.lower)

print wordlist
```

* My solving attitude:
	 - I try not to get too frustrated and or be a perfectionist. I cant know everything otherwise I wont need to be in class. Sometimes I know that when I make certain assumptions or choices I'm choosing the easy way to do it but I feel that's what I could accomplish realistically given the time I have for the assignments.

* Paired programming:
   - It's definitely harder than doing it yourself because sometimes it's hard to convey your thought to another person. Also changing between the "driver" hat or the "navigator" hat is challenging. I think with my pairs we usually just talk it out without clear roles. It's also because sometimes we're trying out an idea and the changing role happens in the middle of that so the person with the idea might just keep talking and explaining as a navigator even though they're supposed to be the driver.
	 - For the poetry slam, we were stuck figuring out how to split the input according to the length of the string and print it on the next line. James went back and did a workaround by putting exactly 5 words on a line. I added the new screen part and asking for new poem. I think that for complicated exercise we might just end up doing our part individually. If we have a partner who works fast, he'll finish the big chunk of the exercise and I would miss out on doing that part of the exercise.

* Example of coding process:
The Tetris remix was tough. I had to spend some time reading the code to understand what it's doing. There are still so many things that I don’t know. Individually I know what they mean but for some reason when put together I have problem understanding them. I was able to separate the functions that draw the background first. I took about 2 hours because I was moving the codes over one by one to make sure they work. However, I was perplexed that the turtles still show even though I have the codes to hide them (see below).

![Tetris Turtle](http://nataliele.web.unc.edu/files/2016/02/tetristurtle.png)

So I stick to my problem solving strategy and decided to come back another day.
When I came back, I put on my debugging hat and searched for the reason why the turtles are still there. Soon I realized I have turtles defined on both the main module and the background modules and that might be why I hid the turtles in my background module but they still show in the main module.
And it worked! Now I know modules are useful but they can be troublesome too. The custom modules I create have to maintain their individuality from the main module otherwise functions and variables will conflict.
Knowing that, I was able to move the drawing screen function to the gameplay module. Every time a piece moves, the screen is redrawn. I was not able to understand the code so I'm not sure if its possible to redraw the piece without redrawing the screening and grid.
This is probably why my program is not stable. I have to click run button several times to get it display correctly. I think this is because of the random function and the fact that I store the drawing screen codes in another module. But I don’t know how to fix it. I made sure that no variables are defined more than once but that doesn’t fix it.

So I think in general I think I can understand why the codes are giving me certain results and that’s why I can do debugging well. This goes back to my coding style where I like to jump in and start coding and see what the computer gives me and then fix my code according to that.

This is why I like exercises with set rules and problems to solve. When I'm faced with open-ended exercises, I spend way too much time brainstorming about what I should do. I'm not a creative person so it's hard to me to come up with ideas. And because I'm also critical to myself, I cant just remix assignments we already did. So usually I would take inspiration from things we've done for example the turtle logical game idea is from the congratulations turtle. My clicky turtle is also kinda the same idea. I should definitely branch out more because now I’m afraid all my turtles will be the same! For example I've never done a drawing turtle except the very first one.

I also think I still take a lot of time to code. I've been timing myself and I take on average 7.5 hours I'm not sure if it's because I'm just slow or because of my approach. So I think for the second half of the semester I need to work on my approach to problems and get better at documenting my thought process.
