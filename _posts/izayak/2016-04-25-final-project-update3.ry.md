---
layout: post
author: izayak
title: "Ruotong's Final Project Update 3"
---

https://github.com/izayak/INLS560_FinalProject   

I've done most of the data analysis part, now the program can be used to analyze sentiment frequency, negative reasons frequency, distribution of comments on days of week, distribution of comments of airlines, and analyze some of them at the same time. The remaining part is the tweets part (formatting the tweets column data, analyze different words' frequency), generalizing the program to work with user's own file, adding help documentation.  
with open() as f:  
  readfile = csv.DictReader(f)  
I've cleaned tweets data one line by one line. As it will pomp a error "not a valid function", I can only delete the material in the cell with more than one lines instead of making the materials into one single line. Also, sometimes after deleting the materials it still has more than one lines, then if that happens I delete the whole row. I am not sure now if there still has "broken" rows as it can be tricky to clean the files as most of the "bad" materials are in two lines (hard work... as the total number of "broken" lines are big...). And I've tested the program with the new file, now it works for all the functions except the time part which works with the concise version file. After saving the files into a tab-deliminated text file, it works now! I have mentioned one way in update 2, which is replacing all the ',' with ';', which cannot be used on the csv file as there are restrictions on the original file.  


*Milestones*  

- [x] (new1,fin1) Set up cloud 9  
- [x] (new1,fin1) Load data file (part: loaded concised version of one data file)  
- [x] (new1,fin1,fin2,fin3) Data cleaning (tried data cleaning, tweets and time zone variables problem solved)  
- [x] (new1,fin1,fin2) Build lists and dictionaries to get information from the data (part: built nested dictionaries, also need dictionaries of negative reason and airlines etc. separately; the remaining part finished in update2)  
- [x] (new1,fin2) Make readable tables based on dictionaries, thinking of alignment  
- [x] (fin2) Try one simple descriptive statistics calculation and do visualization on a particular data file (In my mind the first try would be calculation the total number of complaints towards different airlines in data file airline.csv, and make a histogram.)    
- [x] (new1) Before using regex with tweets, find a way to make tweets' materials loaded successfully  
- [x] (fin3) Use regex to deal with texts (i.e. tweets in airline.csv and gopdebate.csv, 'time created' variable)   
- [x] (new2, fin3) Before studying time and time zones, find a way to load them i.e. figure out how to deal with this error: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 5427: invalid start byte    
- [x] (new2, fin3) Study the pattern of time, for example, according to days of week (Thanks for Erica's suggestion on Tuesday!)  
- [x] (update2, fin3) Use a function to implement the analysis of airlines and sentiment and negative reasons since they are similar, this one is for separate  
- [x] (new2, fin3) Use a function to implement analysis of airlines and sentiment, airlines and negative reasons' relationship  
- [ ] Generalize the program to make it work for different data files: make some variables flexible; add conditionals; let the user input which columns map to what kind of data etc.  
- [ ] Make a text-based interface   
- [ ] Add help text (think of in what way to achieve that)   
- [ ] The user should be able to perform any number of supported actions and then exit the program   
- [ ] Check if the program is well-formatted (comments, organized, readable), error and bug free   


* Stretch/Optional Milestones*      

- [ ] Think more ways to do data visualization through text printouts (scatter plot, density line)     
- [ ] matplotlib (start a pachy? server), 3rd party modules  
- [ ] Do more descriptive statistics analysis such as summary statistics (max, min, mean, etc.)  
