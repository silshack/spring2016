---
layout: post
author: wagerpascal
title: "Jason's First Project Update"
---

## Milestones
- [x] Multiple Data Files.
- [ ] Generalizable to a class of data files. (Sort of have?)
- [x] Text-based.
- [ ] Method of calling a "help" function.
- [ ] Iterative Interface. (While loop)
- [ ] Include code in public github repo (Cloud 9)
- [x] Text printouts of data
- [ ] Function that opens user's imported file upon request.
- [ ] Function that creates horizontal histogram for comparing rating with number of comments, video rate and viewcount.
- [ ] Function that creates a line graph for modeling how the video viewcount changes over time.
- [ ] Function to allow the user to exit the program if desired.
- [ ] Create a function to determine the overall growth of view count (beginning crawl vs. ending crawl) and rank appropriately.
- [ ] Use video ID's from determining top 10 and bottom 10 view count growth rates and graph selected videos.

## Stretch Milestones
- [ ] Integrate youtube API
- [ ] Collect current view count rates of popular videos and compare to data set.
- [ ] Regression analysis for determining type of growth.

I’ve been largely focusing on the setup and design of how I want to approach the problems. Before I began in Cloud 9, I did some preliminary work in PyCharm, specifically focusing on the general formatting and initial organization of the document’s data. However, I didn’t know about Pycharm’s method of altering the distance taken up by a tab, so I ended up wasting some time attempting to figure out why the spacing changed between each column. While it looked like distances were doubling between each column, the distances apparently never changed. I did, however, set up the functions to read the text files.

Once I successfully moved into Cloud 9, I moved in the multiple data files. It seemed that the initial data set was only crawling videos once, so I had to switch to a different set of videos that were crawled by the same research group. Each text file was at least 16000 videos, so for testing purposes, I shortened it to 1000 videos per text file. 

Recently, I got the dictionaries working, where I can take the video viewcounts from multiple videos and compile them into one dictionary. There was some conflicts with the data types initially (where every entry turned into a “NONE” type), but I figured out it was due to the fact that I did not set added values to a list.

I think ever since I got through that dictionary point I have a lot of momentum to continue setting up the other categories’ dictionaries. After this point I will look into the math of determining fastest growing videos, and the graph part. I also need to set up functions for adding dictionaries to quicken the process. I haven’t had time to really implement them before writing this post, but I will try after. I think the plan currently is going at an okay pace, even with the regular pre-finals craze. Currently there's no process on the stretch goals.
