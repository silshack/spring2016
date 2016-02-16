---
layout: post
author: hannahlwang
title: "Hannah's Midsemester Reflection"
---

I think the greatest challenge for me this semester has been assessing what I don’t know, and figuring out how I can fill or improve those knowledge gaps. The book exercises have provided great hands-on examples of the topics covered, but I have learned to take the more freeform assignments as chances to improve my skill set and try something that I might not know how to do. 

<h3>Clicky Turtle</h3>

<iframe src="https://trinket.io/embed/python/a89c1fca50" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My clicky turtle was one of the exercises where I felt like I did this successfully. Prior to this assignment, I had done a lot of work with circles in my other programs. I had made Tina the Turtle draw a modernist clock, a cake with different colors, and differently sized balloons, all of which mostly consisted of circles. Although these drawings all looked nice, I knew that I would have to try some other shapes in order to expand my skill set. For this clicky turtle assignment, I had Sally the Turtle set up a lily pond with lily pads - these were circles with slices taken out of them, which required me to do more thinking about angles. The real challenge here was getting Tina the Turtle to draw the star polygons I had seen in my classmates’ work. The problem-solving technique I used here was Wikipedia.

In retrospect, I really wish I had gone with my original idea for this assignment - creating ripples in the water where the user clicked. This would have been incredibly challenging, but I would have learned how to use clear, and it would have required more difficult loops. Maybe I can use this as a challenge for a future assignment. 

This has been a slightly frustrating theme of this semester — I come up with an idea for a program, then I think that it’s too difficult to execute, so I scale it back or completely change the direction. But I’ve realized that if I don’t challenge myself with these big ideas, I won’t get as much out of the class as I can. 

The best way for me to realize my knowledge gaps and expand my skill set has been partner programming. At first, I was <em>extremely</em> skeptical of partner programming — SILS involves a lot of group work, and I have thoroughly enjoyed the solitary nature of these programming assignments. And at the beginning, pair programming was a very difficult concept to adjust to. It’s hard to explain your code to someone else, much less the half-formed ideas about code in your mind. I found that it was difficult for myself and all my partners not to grab the laptop out of each other’s hands to just explain by showing, rather than through talking it out.

<h3>Romeo List</h3>

<iframe src="https://trinket.io/embed/python/06042bfcab" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My first pair programming exercise was with Will. We had a lot of trouble with the first exercise, a program that was supposed to read four lines of text from Romeo and Juliet, split the text into words, and compile an alphabetical list of all the words in the poem, with no repeats. The concept seemed fairly straightforward: we would apply our new knowledge of lists to create an empty list and add items to it, and we would use our new knowledge of strings to “create” these items, by splitting the line into its different parts. However, we hit a roadblock involving our “for” loop in line 7. Our original code was some version of this:

```
for words in wordlist:
  if words not in wordlist:
    wordlist.append(item.lower())
```

This was essentially checking the entire list against our “wordlist,” resulting in words repeatedly being added to the list.

More interesting that figuring out this stumbling block was observing Will’s thought process when he codes. Things like creating loops seemed to be a little more intuitive for him, but he was also willing to keep trying new things and running the code. I realized that I’m more apt to try to piece it together in my head before writing it down, which really slows down the process. When you just try things and run them, you get more immediate feedback about what is and isn’t working.

<h3>Pair Poetry Slam</h3>

<iframe src="https://trinket.io/embed/python/be8514f0ef" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My second pair programming exercise was done with Jasmine. This was a really effective exercise for pair programming. I think at this point we were both more accustomed to explaining our ideas about code, and we had also done similar things in the starter, which was a simplified poetry slam program.

We started with my starter code, mostly because I had included font sizes to make it look a little nicer. I already had a list using “poem” that added each line as a separate list item, ensuring that they would each be printed on separate lines. 

In order to limit the number of lines printed on the screen, we used a “count” function. After a couple runs of trial and error, we were able to have Tina wait after writing 12 lines, clear the screen, and go back to the top. It was much more difficult to limit the length of the lines, and to have Tina start a new line as a continuation of the first. It was really great to have a partner to talk through the limitations of our code, because we were able to quickly realize that you would not only need Tina to start a new line after 38 characters, but you would also need her to move down AND start the count over at 0. I realized that it’s super helpful to have a partner when you’re just talking about logic: you can use “if… then…” statements to puzzle through really tricky parts of your code. It is also really helpful to have someone else there to point out flaws and gaps that you might not even see by yourself. 

I have several goals for the remainder of the semester, mostly related to this challenge of assessing knowledge gaps, and filling them. I have realized that I should ALWAYS do the optional reading — even if it covers similar material, it does it in a slightly different way that might make more sense, or it at least gives a different perspective that rounds out my understanding. I have also resolved to try to do my challenging ideas for programs, even if I’m not totally successful. I think it is ultimately more instructive to fail at something than do something safe and not expand my skill set. I will also try to seek out more opportunities for collaboration — I might start using the chat function more, or work together with classmates on assignments, when possible. Learning how to talk about code has been perhaps the most difficult part of this class, and it would be great for me to get more practice.
