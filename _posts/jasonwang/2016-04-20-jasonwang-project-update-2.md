---
layout: post
author: wagerpascal
title: "Jason's Second Project Update"
---

## Milestones
- [x] Multiple Data Files.
- [ ] Generalizable to a class of data files. (Sort of have?)
- [x] Text-based.
- [ ] Method of calling a "help" function.
- [ ] Iterative Interface. (While loop)
- [x] Include code in public github repo (Cloud 9)
- [x] Text printouts of data
- [ ] Function that opens user's imported file upon request.
- [ ] Function that creates horizontal histogram for comparing rating with number of comments, video rate and viewcount.
- [ ] Function that creates a line graph for modeling how the video viewcount changes over time.
- [ ] Function to allow the user to exit the program if desired.
- [ ] Create a function to determine the overall growth of view count (beginning crawl vs. ending crawl) and rank appropriately.
- [ ] Use video ID's from determining top 10 and bottom 10 view count growth rates and graph selected videos.
- [x] Make dictionary of video ID's as keys, and view count as the data.
- [x] Make dictionary of video ID's as keys, and average rating as the data.
- [x] Make dictionary of video ID's as keys, and comment count as the data. 

## Stretch Milestones
- [ ] Integrate youtube API
- [ ] Collect current view count rates of popular videos and compare to data set.
- [ ] Regression analysis for determining type of growth.

https://github.com/wagerpascal/INLS560final/commit/9147193532854f1e94c6f6211cdbcd2e3d025f04

Unfortunately I couldn’t get as much as I would have liked for these last couple of days. I ended up fixing an issue with my data where entries that were blank resulted in a list of [0], which interfered with my percent increase calculations that I also added. As you can see from my commit, I located the problem by planting messages in my commit to mark what activated, while which cases weren’t being met (that should have).  While it isn’t milestone-worthy per say, it’s still important that I ensure that the data I use is what I want it to be, as it’ll get a lot harder to pinpoint the same problem down the line.

The percent calculations were created by looping through the keys, taking each list indice, and using first and last values to calculate the percent increase. I am still working on it tonight, and hope to find out a way to save the key’s name for the least and greatest percent increases. Since I eventually want to loop, however, I may also have to make a new dictionary.

I do believe I am on track in what I am thinking, however. Just a little slow in the implementation part.

## Tuesday
- [ ] Store relevant percent increases and rank them appropriately.
- [ ] Figure out graphing/graphs.
- [ ] Begin user input and iteration
- [ ] Add more data files. (~5?)
