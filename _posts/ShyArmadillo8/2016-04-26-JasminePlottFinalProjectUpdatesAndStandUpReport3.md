---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Final Project Updates and Stand-Up Report 3"
---

Here is the most recent version of my Final Project:

<iframe src="https://trinket.io/embed/python3/3d1a254753" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here are the milestones that I set out to complete for this class:

- [x] Create a command for users to exit the project (i.e. something like finished)
- [x] After the initial data is printed for the user, allow them to have the opportunity to enter more input
- [x] Produce some statistics from the data that the user has asked for. Baby milestones are below to grow to this:
- [x] Print the mean. To do this, I’ll need to get the sum and total count of values to figure this out
- [x] Print the median. To do this, I’ll need to use the total count of values and put it in the median formula
- [x] Print the maximum. To do this, I could use the maximum function
- [x] Print the minimum. To do this, I could use the minimum function
- [x] Create functions for the above statistical functions

I was able to complete all my intended milestones this time around.  I owe a lot of this to my good time management, taking breaks, and using effective troubleshooting tactics.

The first step that I tackled was actually getting a real visual to print.  After checking in from last class, it was confirmed that my image of a baby saying "Here's your results!" was indeed cool, but it did not do anything for actually visualizing my data.  We were introduced to matplotlib during last class though, so I decided that I would take this route for showing my data.  By referring to this site http://matplotlib.org/ and looking at the example of matplotlib that was demonstrated for Python 3, I used a lot of troubleshooting tactics to get my graph of frequencies to print out.  Initially, I just had my graph print out the data, but after I got some of the more advanced pieces of my program, I came back to this and made it more visually appealling by adding x and y axis labels, a title, and formatting the labels so that they were not overlapping with each other.  There are still a few parts (i.e. spacing for the x axis labels) that I would like to edit, but I decided to leave these as stretch milestones to be accomplished before I turn the final product in.

The next step that I focused on was integrating the quality assurance portion of my code, allowing the user input to relate to regexes, allowing the user to exit the program, and creating the while loop that allowed the code to continue and allow the user to perform as many functions as they wanted.  This part also required a bit of debugging, as I had to remember which variable names were associated with which and assigning the appropriate .lower() and .title() functions when necessary.  During this part of the code, I tried to think about all the ways that the user could potentially break my program, and I tried to incorporate as many ways to keep this from happening.  Developing this part of the program renforced that I wasn't making a program just to complete a final project, but I needed to think about how to make the program as usable and functional as possible.

The final task that I focused on this time around for the project was integrating my functions for statistics in addition to my frequency graph.  I'd already laid out what to do in my milestones, so I got to it.  I first tackled the maximum and minimum functions; these were okay to incorporate, but I realized that there were sometimes multiple instances of a minimum or maximum value for the results dictionary that I had created.  I thus had to modify my code to accomodate this.  I solved this by extracting the minimum or maximum value of the results dictionary and then went through the dictionary to see which keys matched to this value.  Using this tactic helped ensure consistency and preciseness in my program.  I next tackled the average which went smoothly, but the median was a struggle.  I had to figure out how to get the median from the list if there was both an odd and even set of numbers in the list; I did reference Stack Overflow for guidance on this and need to remember to add the link to give credit in my code.

Working on my project like this helped me build confidence in my own programming skills and allowed me to become more comfortable with dictionaries and using functions involving them.  What I really like about having a long term project like this is that it helps me familiarize and experiment with certain types of coding in Python, which has been really useful.

Here are my milestones to be completed before submission:

- [ ] Replace the placeholder text with actual text in the "help.txt" file
- [ ] Add documentation to the code
- [ ] Organize the code and make it more legible for someone who's not myself to read
- [ ] See if it's possible to compress anything else into functions-this might not be possible, so it's okay if this milestone isn't checked.  It's a reminder to myself to check more than anything else
- [ ] Make the graph more visually appealing by adding spaces between labels
