---
author: izayak
title: "Ruotong's Final Project Idea & Milestones"
layout: post
---

*When I was considering about my final project plan, I paid attention to these aspects:*

* What dataset should I choose? I have to find one dataset that is rich of information (so that I can flexibly moderate my plan to make it include more or less tasks) but also in a clean format, good for me to use what I learned in this course (dictionaries, lists, functions, loops, regex etc.) and not too big. Also, one of the requirements is to include more than one file. This should also influence my decision.  
* What should I include in this project? I plan to do basic descriptive statistics analysis (with histogram visualization), regex and find interesting facts from data (i.e. Who win the largest number of counties support among Democratic/Republican candidates? Which airline's proportion of negative tweets is the highest? etc.)
* Use Trinket Python 3 or Cloud 9? Since the data files are not large, I would probably use Trinket 3. But I haven't decided. I will decide after tomorrow class' Cloud 9 tutorial. *I tried to paste the csv file into Trinket but it does not work. Is that because the file is too large? The csv file has more than 10000 lines.*
<iframe src="https://trinket.io/embed/python3/253614bf5b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Due to these considerations, I choose the follwing two data files: 1) Twitter US Airlines Sentiment 2) 2015 First GOP Debate Twitter
Sentiment. Both of them are from kaggle.com. I read all the descriptions and interesting scripts of all the kaggle datasets. They are all
interesting but some of them are too large (Amazon Fine Food Reviews), some of them are better analyzed by R or need more advanced tools 
of Python (such as Climate Change, and Iris is a classical R dataset which would be best for clustering analysis), some of them are good 
to be analyzed with geographical tools (Hillary Clinton's Emails, Ocean Ship Logbooks), some need more professional knowledge (History of
Baseball), some of them's information needed are in separte files which are hard for the generalization of the program (2016 US Election,
although this dataset is very attractive to me). So I finallly choose these two files with tweets as they are in similar formats which
can satisfy the requirement of generalization of program and contain enough information to be analyzed by materials we've learned so far.
The SF salaries and NIPS 2015 Papers are also fine, but the first one's occupation types' information is included in SQL file and the
latter one contains two few abstracts (maybe I'll add this one after I finished the program as the analysis of abstract would be similar
to that of tweets). 



*Milestones*

- [ ] Try one simple descriptive statistics calculation and do visualization on a particular data file (In my mind the first try would be calculation the total number of complaints towards different airlines in data file airline.csv, and make a histogram.)
- [ ] Do more descriptive statistics analysis such as summary statistics (max, min, mean, etc.) 
- [ ] Think more ways to do data visualization through text printouts
- [ ] Use regex to deal with texts (i.e. tweets in airline.csv and gopdebate.csv)
- [ ] Use functions to make some parts of the program concise
- [ ] Generalize the program to make it work for different data files: make some variables flexible; add conditionals; let the user input which columns map to what kind of data etc.
- [ ] Make a text-based interface
- [ ] Add help text (think of in what way to achieve that)
- [ ] The user should be able to perform any number of supported actions and then exit the program
- [ ] Check if the program is well-formatted (comments, organized, readable), error and bug free
