---
layout: post
author: wagerpascal
title: "Jason's Final Project- Youtube Web Crawl Analyzer"
---

Github repo: https://github.com/wagerpascal/INLS560final/commit/1732d474a03b2efd0a48170829bb3474c2c8efc5

I’d like to start off saying that this project went much better than the last two projects. This time, I took the time to analyze whether or not I had the time to finish the project, as the time crunch for me (and most likely everyone else) made time management a much more important factor. I chose this project mostly because I ran into these large sets of data on the internet, and quite frankly, I wanted to see how python could deal with large sets of data. In addition, the web crawls were taken during the 2007-2008 Youtube, which represented a much different time than what we can view today (On a side note, personally I feel the old rating system is much better), and made the results pretty interesting to look through.

I decided to tackle this project by largely first finishing the individual data analysis parts, followed by the UI and consolidation process. To start, I focused on reading and processing the files. At this point, we had not discussed creating the project in Cloud 9, so I began in PyCharm to keep a degree of consistency between both IDE’s. However, PyCharm has an interesting format of in cases where tabs/spaces divide columns in text files, the perceived space increases (doubles?) for easier reading. Unfortunately, I did not know this prior, and thought that the transfer between original text file and PyCharm broke the formatting; leading to some wasted time. However, moving to Cloud 9 removed this problem.

I then began data analysis. While I did have an idea on what I wanted to do, it was not until the beginning of data analysis where I was able to pinpoint on what results I wanted in the end. While I initially said that I wanted to compare certain values together, I thought about the meaning of such comparisons, and realized that overall, such outputs would not teach anyone much about data trends. However, general distributions, such as the average rating over time, or the average comment number over time, gives a picture of the Youtube landscape at the time. 

I still took a modular approach, although a slightly different modular approach. I first set up a test sequence- where data flows freely between demarcated sections and produces the results. Once that was completed, I split the sections into separate functions (but still without data requesting). I really did think that the UI would be pretty easy to implement- but between the differences of the while loop and minimizing the data that flows between functions, the functions still had to be restructured (and new ones made). Perhaps in this case, I should have also made a rough UI version so that the functions that I had made were also designed to work with the While loops.

Between this project and the last, I personally believe that my debugging skill had increased dramatically. While in the last project I had to keep playing around with values (and sometimes breaking it more) to try and isolate why certain functions weren’t working as intended, zeroing in on problems in this project was much easier. This may be helped by the fact that you can track the data as it flows through, but I also think that my deeper understanding of Python since the last project allowed me to stop and think, “Why?”. And from “why”, we can narrow down the possible areas of interest.

Honestly, between the structure of this project and the last project, I thoroughly appreciated the open-ended, milestone-focused aspect of keeping on track. The milestones really did help me quickly narrow down what topics I wanted to than if it was completely free, and the updates pushed me to make progress between each class. While I’m not saying that I would be planning on finishing the whole project 30 minutes before, the milestones gave me a good plan to plan my progress around, and plan what I would try to accomplish that day. The permanent groups was also pretty helpful. Being able to keep up with certain people over time gave me a better understanding and appreciation of what they were doing, and gave me some insights that I eventually used in the construction of my program.

There are a number of things that I would like to address in this program for the future. Overall, I think the program runs well (Cloud 9 does run into memory problems if the data set is too big, but I don’t think that is avoidable with large data sets), but it would be nice to give some flexibility to the number of data sets of the program- especially in cases where more data sets need to be analyzed as a whole. While I picked 5 as it was both a clean number and was enough points to see a clear trend (as well as the computation time), an actual data analyst may need to see upwards of 100 points to have a better picture of what is going on. I do have a vague idea of implementing this (perhaps through making the file-reading process into a function, and having the user expressing how many data files they want to use initially), but it will have to wait until after this project is over. Also, the histogram scaling is currently fixed- while I may be able to set it to an acceptable value for each one, the fact that it doesn’t automatically scale severely limits its scope. I would really like to implement a function or equation to calculate how the value should change, but due to limited time, testing values out over and over again would be too time-efficient for this version of the project.

While Elliot said that using Cloud 9 would be more work than Trinket, I think the time that it took for the extra setup was worth the convenience of automatically saving the files, as well as the IDE and github bash practice. In addition, being able to see the memory and CPU expenditure was helpful in some cases involving debugging (most particularly a case where I accidentally added too many things to a dictionary, which obviously was pretty memory heavy). The only real issue I had with Cloud 9 itself was trying to figure out how to use matplotlib (which I unfortunately implemented before we talked about it in class); there are a few cases of how to use it scattered between various websites, but I was extremely lucky that I ran into someone else’s github repo where they properly explained it (by the way, there really should be some kind of way to show your gratitude or appreciation to people’s repos in github, because his explanation was spot on). In addition, having a github repo after finishing the project is a good habit for future python projects, which may involve materials from this project. After all, your past work is your best friend in programming.

I do think that this project is a good representation of what’s happened since the midsemester reflection- that I’ve certainly learned a bit more about myself regarding time management, as well as the quality of my coding. I remember in the beginning of this class that I didn’t care that much about reduction or optimization of code- after all, what works, works. However, for this project, I was pretty pleased in the fact that I reduced the main code (all the functions went to the setup file) to less than 150 lines. Not like I skimped out on the coding or anything- my setup file was about 500 lines. However, working incrementally on the project versus trying to consider everything all at once was far less overwhelming; while this was the longest continuous program that I’ve written myself, it really felt like I didn’t really code that much (in that time flew by). And like I mentioned earlier, debugging overall has taken a lot faster than before (is this a byproduct of the IDE? I feel like the errors are more precise in Cloud 9 than anything I did in Trinket, but it could just be me talking).

I anticipate having to use Python soon as I want to do research in computer networking in graduate school. I discovered python’s socket library some time ago (and even made a port scanner that I tested), and hope to learn more about networking through Python. I will have to admit that at this moment in time, if someone requested that I had to program something, I will consider using Python first- the fact that Python is such a user-readable language (at least more than Java) is fantastic, and makes the programming almost seem like you’re explaining how to do all the functions and calculations to the computer. I’ll definitely never claim to be an expert in Python until I actually do become one, but I think learning how to learn to program was probably one of the best outcomes that came out of this whole experience.

## Milestones
- [x] Multiple Data Files.
- [x] Generalizable to a class of data files. (txt)
- [x] Text-based.
- [x] Method of calling a "help" function.
- [x] Iterative Interface. (While loop)
- [x] Include code in public github repo (Cloud 9)
- [x] Text printouts of data
- [x] Function that opens user's imported file upon request.
- [x] Function that creates horizontal histogram for comparing rating distribution.
- [x] Function that creates horizontal histogram for comparing Comment distribution.
- [x] Function that creates a line graph for modeling how the video viewcount changes over time.
- [x] Function to allow the user to exit the program if desired.
- [x] Create a function to determine the overall growth of view count (beginning crawl vs. ending crawl) and rank appropriately.
- [x] Use video ID's from determining top 10 and bottom 10 view count growth rates and graph selected videos.
- [x] Make dictionary of video ID's as keys, and view count as the data.
- [x] Make dictionary of video ID's as keys, and average rating as the data.
- [x] Make dictionary of video ID's as keys, and comment count as the data. 

## Stretch Milestones (Unfortunately not enough time)
- [ ] Integrate youtube API
- [ ] Collect current view count rates of popular videos and compare to data set.
- [ ] Regression analysis for determining type of growth.
