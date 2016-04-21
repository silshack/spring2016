---
author: izayak
layout: post
title: "Ruotong's Final Project Update 2"
---

From Tuesday, I have finished the setup of basic dictionaries, including one for airlines, one for negative reasons, and one for the overall data. I have made frequency counts and printing histograms on airlines and negative reasons dictionaries. And from the overall dictionary, I made a contingency table of airlines, negative reasons and sentiments. 
I found out that I can make analysis of airlines and negative reasons by the overall dictionary as well, so I plan to do that before next update. Also, I will make functions to achieve the table and histogram making and showing. And I will make some changes before that: to change all blank in negative reasons into "Not Stated", then I do not need to do that in the data analysis and visualizaion part then it will be more convenient for me to put the analysis of all the variables in one single function. Before this Tuesday, I found that I cannot use either xxx != " " or xxx != None or xxx is not None to deal with the blank, and I figured out that I can use len() with it. Although I do not need to do this since after discussed with Erica on Tuesday I think that blank (i.e. not stated reason) is also worth attention. 
Also, before next update, I plan to finish the tweets and time variables' analysis and generalize the program to work with both the airlines and the gop debate files.  
The files in github repository has been updated. https://github.com/izayak/INLS560_FinalProject     


In today's class, I figured out how to deal with tweets and time zone variables. For tweets variable, 1) export to a tab-deliminated text file or 2) replace , with ;. For time zone variable, replace characters that cannot be recognized by blank. These helped me a lot, which allow me do the data file importing smoothly.   
I also learnt the csv module of Python from Erica, especially, the DictReader(), which would be a great help when deal with more than one data file:     
with open() as f:  
  readfile = csv.DictReader(f)  
We also discussed the order of programming and how to make plans.    
What I want to try: matplotlib (start a pachy? server), 3rd party modules.  



*Milestones*  

- [x] (new1,fin1) Set up cloud 9  
- [x] (new1,fin1) Load data file (part: loaded concised version of one data file)  
- [ ] (new1,fin1,fin2) Data cleaning (part: tried data cleaning, tweets and time zone variables)  
- [x] (new1,fin1,fin2) Build lists and dictionaries to get information from the data (part: built nested dictionaries, also need dictionaries of negative reason and airlines etc. separately; the remaining part finished in update2)  
- [x] (new1,fin2) Make readable tables based on dictionaries, thinking of alignment  
- [x] (fin2) Try one simple descriptive statistics calculation and do visualization on a particular data file (In my mind the first try would be calculation the total number of complaints towards different airlines in data file airline.csv, and make a histogram.)  
- [ ] Do more descriptive statistics analysis such as summary statistics (max, min, mean, etc.)   
- [ ] Think more ways to do data visualization through text printouts  
- [ ] (new1) Before using regex with tweets, find a way to make tweets' materials loaded successfully  
- [ ] Use regex to deal with texts (i.e. tweets in airline.csv and gopdebate.csv)  
- [ ] (new2) Before studying time and time zones, find a way to load them i.e. figure out how to deal with this error: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbe in position 5427: invalid start byte    
- [ ] (new2) Study the pattern of time, for example, according to days of week (Thanks for Erica's suggestion on Tuesday!)  
- [ ] (update2) Use a function to implement the analysis of airlines and sentiment and negative reasons since they are similar, this one is for separate  
- [ ] (new2) Use a function to implement analysis of airlines and sentiment, airlines and negative reasons' relationship  
- [ ] Generalize the program to make it work for different data files: make some variables flexible; add conditionals; let the user input which columns map to what kind of data etc.  
- [ ] Make a text-based interface   
- [ ] Add help text (think of in what way to achieve that)   
- [ ] The user should be able to perform any number of supported actions and then exit the program   
- [ ] Check if the program is well-formatted (comments, organized, readable), error and bug free   



