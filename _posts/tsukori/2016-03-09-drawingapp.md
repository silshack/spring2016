---
layout: post
author: tsukori
title: "Drawing Project: Hangman"
---

<iframe src="https://trinket.io/embed/python/02cefbfd83" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Project Standards:

- [x] Key and click events
- [x] Animated congratulation screen
- [x] Keep track of game state i.e. if you collect coins, how many coins were collected
- [x] Intuitive HUD

Base Goals:

- [x] Draw Hangman 
- [x] Layout letters
- [x] 5 word "dictionary"
- [x] Functional key presses
- [x] Lay out spaces based on word length
- [x] Updates hangman correctly

Optional Goals:

- [x] Reset game ability
- [ ] Have multiple word-size dictionary
- [ ] Mode selection: easy, normal, hard

Reflection: 

I was glad that Elliot gave us suggestions for games to make because the hardest part of starting projects, at least for me, is thinking of the idea. I like to have one vision and then make it happen, rather than a flexible idea that can change as I work through the program. 

I started off by drawing all of the components for the screen that would stay constant and laying it out, then I stepped away from the program to actually think about how all of the parts would be working together. I knew I wanted to use the key presses and update the hangman; I thought about the assignment for bits at a time over a couple of days, putting in the majority of the work on Tuesday night when it somehow just clicked for me. I did not want to type out each of the key presses so I tried to think of creating an algorithm for creating each of the functions relating to the key presses but I ended up scrapping it since I could just implement it the brute force way and it would run just as well.    

I was able to meet all of my goals and even one of the optional goals, which I am pretty proud of. When implementing the restart feature I ran into an issue with correctly updating the wrong and correct counters since my restart function sits in the main module, then I realized I could create a reset counter function in the correct module that housed the variables in the first place and call it in my restart. I am not all too sure if my "animation" counts as an animation since nothing actually moves but I thought the static display fit more with the hangman game. As far as I know the only bugs occur if you try to press multple keys at once or if you enter them too quickly. I was considering using the ontimer function to remedy this problem but I was not completely sure how to use it/if it actually would fix the problem. 

Compared to the drawing project, I had a lot more fun doing the game app since I had a much clearer goal and the implementations were a lot smoother than for the drawing app. I think I could possibly modularize it a little more, towards the end I was just kind of throwing functions into modules for the sake of cleaning the main one. 
