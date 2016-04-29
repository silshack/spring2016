---
author: clairewlj
layout: post
title: "Lingjie's Final Project"
---

Github link: https://github.com/clairewlj/clairewlj

**About the program plan:**

1. Datasets searching: 

When I realized that we needed to apply our programs on our own data files, I began to think about using data sets from kaggle.com, whose data sets were very suitable for practicing data analysis skills. However, it was difficult for me to find two or more datasets with same or similar variables and structure. Then I tried to search from several universities’ libraries’ archives, such as UCI Machine Learning Repository. I finally found a dataset with medals data of several Winter Olympic Games from another course and successfully found another dataset with data of Summer Olympic Games.

2.Project Plan & Changes: 

a. Original idea: 

At first, I was thinking about displaying some descriptive statistics as summary of the two sample files and also files uploaded by users, such as the size of the file, types of variables (column names) and the relationships between variable. Specially for these data sets, different year/ hosting city/ sports type/ NOC(National Olympic Committee)/gender/medal type, etc. Also, the relationships between sports, disciplines and events were one containing the next, which would be quite important for users to know before they could apply the program to their own data files. As for the main functions of my program, I planned to give users two options. Users could choose to view rankings of countries based on sums of different types of medals, or to view visualizations such as scatter plots, line graphs or bar charts.

I was planning to make user select filters following fixed and ordered steps. However, I changed my plan quickly after I began to write my program, as I wanted my program to allow users choose whatever and no matter how many filters they liked, and they could also return to previous menu or directly quit search whenever they wanted.

b. Update 1: 

I then completed the option for user to choose multiple filters for selecting data. Basically I created a dictionary of lists as an index list and summary, where each key was an ordered list of all unique values of one specific variable ( year/city/sport/discipline/event/gender/medal/ NOC). Then the user could first select one variable, and then select one unique value from the related type (such as choose “Aquatics” from “Sport”). Also, with the help of multiple levels of loops, users could return to previous menu, select whatever they like and quit search at any time and did not need to follow a strict order of steps. 

However, I then realized that “Event” was actually subclass of “Discipline”, and “Discipline” was subclass of “Sport”, which meant that if I left them as independent variables, users might wrongly selected disciplines that did not exist in a specific sport. Thus, I changed my index dictionary to fix the bug as I made ‘Sport’ a dictionary, whose keys were ‘Discipline’s and the related value of those keys were lists of related ‘Event’s.

c. Update 2: 

After completing the first option, I was thinking about add one option of ranking countries according to the medals they won in one specific year. As it seemed not to make sense to rank countries at ‘Event’ level (only one gold, silver and bronze winner for one event), I decided to narrow the range of user’s filter choices down to only among year/sport/gender/medal type. The details of this part will be explained later.

d.Update 3:

After the two options were completed, I tried to achieve one of my stretch goal – adding visualizations. Firstly I planned to display visualizations I chose and that users were not able to create visualizations as they wanted, which seemed much easier – I just needed to figure out how to make use of the existing package to create plots. I used matplotlib to add one bar plot of one year showing the top 10 countries winning the most total medals. I was then wondering if I could adjust my program to enable line graph and allow more flexible plotting according to user’s choices.

e. Final update: 

Finally, the third option – for viewing visualizations included 2 types of graphs to choose from. The line graph was for comparison through history. It would allow users to choose 2 countries from the NOC list and choose to view the change of total / gold/ silver/bronze medals they won through time. The bar graph was for viewing rankings in one year. It would allow users to choose one specific year, and choose to view visualizations of top 10 NOC winning total /gold /silver / bronze medals.

**About code:** 

1. Select and view detailed data part:

At first I was thinking about creating a dictionary of dictionary of … of dictionary in the same way that the raw data was in the csv file. (For example, summary={ ‘1996’:{‘City”: “Atlanta ” , ’Sport’:{“Aquatics”:{“Swimming”:{“ Butterfly”:{“Male”:{“Gold”:  USA}}}}}}}. I did spent some time creating the large and complex dictionary, but then I realized that it was actually not suitable, since what mattered was NOC, and as I wanted to enable users to search across different levels (such as select “1996”, “Swimming” and “Bronze” only), the complex structure was actually make the search process harder to complete. Thus, I decided to keep the original words table – list of lists created by the method of f.readlines(), and create a new dictionary to store user’s filters chosen, and then use the choices dictionary to accordingly extract data rows from the original words table.

For the filters selection process, I chose to sort the list of filters alphabetically, and in each step, print out the filters and their indexes following the order, and ask user to enter the numeric index to select one specific filter, and move to another level to choose more classified filters. The program also allowed users to select multiple filters in the same level or across different levels one by one and quit using while loops and conditions. The filters would be stored as: [[1996,1992],[ ],{‘Aquatics’:{‘Swimming’:[‘200m butterfly’,’200m freestyle’],’Diving’:[‘10m platform’]}, ’ Badminton ’: {‘Badminton’: [‘single’] } }, [ ],[‘Gold’,’Silver’]].

After filters chosen, when selecting data rows accordingly, I created a loop to go through each line, and used Boolean values to determine if the elements in the line matched the filters. I felt excited that I could use the functions of all() and any() in this part, which I learned from extra reading.

After completing all these above, I began to refine this part of program. I dealt with user’s possible bad input using try and except, and fixed the bug that if users accidentally selected one filter more than once, it would be add into the filters list again even if it already existed. Then I tried to clean the module by creating custom functions for repeated simple tasks, such as printing out a menu by printing out a list of elements with its index joint by a blank space, or checking if the filter was already in a list, and adding it if not, and making all keys in a dictionary a list and sorting it alphabetically. To clean main module, I separated it into several parts and changed them into several functions, which needed particularly attention as many levels of loops, conditions and try/excepts involved. I think it’s still not efficient enough, as there are still many repeated or similar codes in the program, and these large custom functions take too many arguments, and it is difficult to apply them to other uses. 
		
After realizing the relationships between sport, discipline and event, I had to make big changes in filters structure and also the list of lists for selecting data rows.

2. ranking:

The ranking part was much alike the option of selecting and viewing data rows. I wanted to make the program to allow users to select filters, thus complex combinations of dictionaries and lists were needed just as the viewing part did. In order to simplify the program, and as it seemed not to make sense to rank countries at ‘Event’ level, I decided to narrow the range of user’s filter choices down to only among year/sport/gender/medal type. And again, I used union and intersection of Boolean values to select data rows in original words table based on user’s choices. For ranking, I wrote code to count through the whole words table based on user’s choice of medal type (total medals/gold/silver/bronze). I’m also still wondering if there’s easier and more efficient way to count these numbers can be applied and help to avoid the huge loop.

During the process, I’ve learned to use data.sort(key=lambda x: x[index],reverse=True) to sort and gain the ranking based on user’s choice. Also, I realized that error would occur if I used int(input) in conditions. And I learned to make a pause by adding an input. Another interesting thing I found was that when printing out selected information, “ “.join can not be applied when a list consists of both strings and integers. I think it’s helpful for future work.

3.visualization: 

I had to say that I nearly gave up this part when I stuck in the procedure of installing numpy & matplotlib package. This was my first experience of using outside packages. Then I first learned simple bar graph plotting through simple examples, figured out basic procedures and format needed such as tuple and lists, and applied them on my sample datasets. When I got more familiar with this package, I added one more option to create a line graph to allow user to choose two countries for comparing and one specific year.

There was something wrong when I tried to run the program on Cloud9, and with the help of professor, it finally succeeded and was able to save figures created in the current directory.

**Generally about the project:**

I truly worked hard and learned a lot through the process. I’ve spent 5 hours per day on the program, and now I feel more confident in handling more challenging tasks. I also have fully realized that I’ll need more training and practice to make my program more efficient and readable with a clearer structure. In the future I’m thinking about learn more about algorithms and data structure, and also work on more real data and conduct task oriented analysis.
