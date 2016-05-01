---
layout: post
title: "Ruotong's Final Project"
author: izayak
---

https://github.com/izayak/INLS560_FinalProject     


**Strategies Used (also included work done in this project)**    
1. A clear map in head    
I prepare more carefully this time, comparing to those projects in the first half term. Before starting the project, I considered thoroughly about the order of my programming (which is shown the project idea's first  version milestone). So form the first version to the last one, my milestones do not change much, only some small steps are added.    
Each step is based on the previous step, that is to say, adding codes the previous codes (new arguments in functions, new conditionals, etc.). Working in this is good for keep tracking and not getting lost, although when the program gets bigger and bigger it is harder and harder to think it clearly. Anyway, it is a good practice for thinking in clear logic.                
In my plan, the order is like this:     
1) Work on a simple variable's analysis i.e. airline.txt file's sentiment varaible. Only a dictionary is required. airlien.txt's airline varaible is similar. In this part, we can see how many tweets are distributed in each airline companies and in each sentiment (positive/negative/neutral).        
2) Try this with a more complicated varaible i.e. airline.txt file's negative reason varaible. This one requires only a dictionary, but I have to deal with some of the reasons: capitalizing 'longlines' and replace ' ' with 'Not Stated'. In this part, we can see how many tweets are distributed in each negative reason (longlines/luggage/late/etc.).        
3) Try to make tables and visualizaiton. I first calculated the lenth of the longest string then use that one as a criteria to make the table. In some later codes, I used '\t'.join(). '\t'.join() is more convenient in coding, but when the string is very long, it does not work well. Basically this part is working with how to show the table and stars in a good format.       
4) Work with more than one variables. As not only the tweets number of differnt airlines, different sentiments are interesting, I am also interested in when two or more factors are considered what the pattern of number of tweets will be. In this part, I built a dictionary of dictionary of dictionaries. Airline is the first layer, sentiment and negative reason are the second layer, the third layer are the counts of tweets. After forming the big dictionary, I made contingency table and visualized the table.     
5) Work with time varaible. The time variable of airlines.txt contains days from 2/16/15 to 2/24/15, 2/16/15 is Monday and 2/22/15 is Sunday. So I use regex to get the day of the date and translate it to Monday through Sunday. I did not include 2/23/15 and 2/24/15, I only included one week. In this part we can see that Mondays and Sundays have most of the tweets, which is an interesting finding.   
6) Work with tweets variable. This part is the most difficult, and till now I cannot say that I worked well with tweets variable. I am not proficient in either regex or data cleaning with other tools. It is hard to accurately subtract the content I want from the tweets. So with what I wrote in this program, I haven't found interesting findings (maybe 'cancelled' occurs more frequently in negative sentiment can count one), which should be the most insightful part in my plan.   
7) With 1-6 steps, after tested the analysis part worked, I put it into a function. So when I was at step 7, I had all the functions.   
8) Cleaned the data file gop.csv and formed gop.txt. This is similar with what I did with airlines.csv, except there are more lines needed to be fixed in gop.csv's tweets variable.   
9) Studied the variables of gop.txt and considered how to analyze them using the existing functions. The sentiment variable is exactly the same with airlines.txt. The candidate variable is similar to airline variable of airlines.txt. The subject matter variable is similar to negative reason variable of airlines.txt. The interaction analysis between these 3 variables are similar with the interaction analysis of airline, sentiment, negative reason of airlines.txt. The only thing need to be noticed is change some contingency column names printed. The tweets variable need changing with the regex part. The time variable is not good for analysis since there are only two days. The retweet variable is worth analyzing in gop.txt as it is not always 0 (which is always 0 in airlines.txt). So I added a new function for retweet varaible since the analysis of this variable is unique to the previous ones since in this case the count is not one by one, but adding the retweets numbers together.  
10) Made the main function to let the user choose between files and variables the user wanted to analyze. Then assign index numbers, variables to keep records with the user's choices. Test and refine the program to work smoothly. So in this step the program is generalized. This part is really exciting, as I can see how the previously functions work on a new data file and some interesting new findings. The gop.txt data file is based on tweets about the first gop debate, it is more interesing for me than the tweets of airlines. We can see that more tweets are about Donald Trump and Ted Cruz obviously, the gap of number of tweets between candidates is really big.  That's why data analysis is attractive :)    
11) Made a helper function. At first I planned to use turtle to let the user press one key then the helper function will pomp out. But I did not work out as the turtle does not work. Have no idea. If it works, I planned to count the total number the helper function is called and total number that the helper function is useful evaluated by the user.    
2. Work perservarantly    
Work some hours each day, then continue the next day. It seems easy, but people have to defeat laziness. But one can work step by step, he or she will feel more flexible and more efficient.    
3. Debug     
Basically use the print function, simple and useful.    


**Possible Improvements**     
1. tweets    
I really hope that I could know how to deal with those unrecognizable chracters in tweets; With tweets analysis, separately print the 10 most frequently used words in tweets in these 3 categories: words counts >5000, 1000-5000 and 500-1000; regex.   
2. tools that can be used with files      
Cleaning files in excel can be time consumind and at the same time the result is not good. I deleted tweets with more than one lines as cannot put them into one line, which waste lots of valuable materials.     


**Overall Reflection**    
I am very glad that we are assigned this final project instead of a final exam since we can learn more from a project like this. I gained quite a lot coding experience during the process of building this data analysis program. Although it is relatively small comparing to what are made by programmers in industry, I haven't imagined one day I can write a program that is more than a thousand lines, which is quite encouraging, isn't it? Also, I like the way that the project is updated. In order to turn in the three updates and effectively discuss in pair and in group, I have to write programs step by step and think carefully in advance. It forces me to break up the big goal into small tasks and keep working on it. After the last day of class, I realized that I have finished most of the work, and it is 3 days from the submission deadline. If you work in advance, you will feel relaxed and think in a more thorough way. Moreover, I am very happy with my pair Erica and my group members Omar and Javairia. I got helpful suggestions from them and felt supported in the group. All in all, thank you very much for this experience. I will be more comfortable when coding is needed in the future, and will have more option when trying to do data analysis. (In previous projects, I found other students' work quite inspiring, will there be a show for students' program this time for the final project?)       




**Milestones**     

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
- [x] (fin4) Generalize the program to make it work for different data files: make some variables flexible; add conditionals; let the user input which columns map to what kind of data etc.  
- [x] (fin4) Make a text-based interface   
- [x] (fin4) Add help text (think of in what way to achieve that)   
- [x] (fin4) The user should be able to perform any number of supported actions and then exit the program   
- [x] (fin4) Check if the program is well-formatted (comments, organized, readable), error and bug free   


**Stretch/Optional Milestones**          

- [ ] Think more ways to do data visualization through text printouts (scatter plot, density line)     
- [ ] matplotlib, 3rd party modules   
- [x] (fin4) Do more descriptive statistics analysis such as summary statistics (max, min, mean, etc.)    
- [ ] (new4) Use other tools deal with data cleaning and tweets 
- 

