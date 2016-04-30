---
layout: post
author: jwarrich
title: "Javairia's Final Project"
---

**Final Project Reflection**

Here is my final product: <iframe src="https://trinket.io/embed/python3/3a5ba4a20b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


The journey of completing my final project has been challenging but overall very rewarding. At times I have been overwhelmed, confused, annoyed but through it all I have gained confidence in my skills and used the knowledge that I have gained throughout the whole semester to complete something that I am proud of. For my final project I chose to analyze Male and female NBA salaries. Originally I wanted to look at UNC Basketball stats but realized that the process of extracting the data would take too long. This was one of the first major decisions I made about my project. I happened to run into a data file with NBA Salaries and thought it would be interesting to compare it to Women NBA Salaries. Because I couldn’t find a data file with WNBA salaries, I had to look for them. One interesting thing I found when going through this was the fact that major sports websites listed Male NBA salaries and not WNBA salaries. This peeked my interest even more. Once I started extracting female salaries from different sites, I realized there was a HUGE difference. I understand that Men’s Basketball is more advertised and marketable but still the difference was truly astonishing. Once I got over how interesting my findings were, I wanted to find a way to best show all aspects of both datasets and a way for the user to see the results when compared to one another. 

**Program Overview**

On the main screen, the user is allowed to choose from five options: 1- Male NBA Players, 2- Female NBA Players, 3- Comparison, 4-Help, and 5-Exit. Option one and two have the same functionality but use different data sets. Option 3 uses information found in both data sets. The help function gives the basic instructions on how the program works, and the Exit option closes the program.
The first two options have the same suboptions. The user can look at the entire datasets, look for a specific player, position, or team. The results are then printed. For example, if you want to look at Male NBA players, and then a specific player (LeBron James) the user has to type in either the first name or last name. The player information along with the amount of results found is printed. 
```
  ['RANK', 'PLAYER', 'POSITION', 'TEAM', 'SALARY($M)']
  ['3', 'LeBron', 'James', 'SF', 'Cleveland', 'Cavaliers', '22.9705']
  Results found: 1
```

If the user wants to see a specific team they can also do that as well. For example if the user types in Hornets, they will get the following results:
```
['RANK', 'PLAYER', 'POSITION', 'TEAM', 'SALARY($M)']
['40', 'Al', 'Jefferson', 'C', 'Charlotte', 'Hornets', '13.5']
 Results found: 1
['44', 'Nicolas', 'Batum', 'SG', 'Charlotte', 'Hornets', '13.125306']
 Results found: 2
['53', 'Kemba', 'Walker', 'PG', 'Charlotte', 'Hornets', '12']
 Results found: 3
['102', 'Marvin', 'Williams', 'PF', 'Charlotte', 'Hornets', '7']
 Results found: 4
['113', 'Michael', 'Kidd-Gilchrist', 'SF', 'Charlotte', 'Hornets', '6.331404']
 Results found: 5
['117', 'Spencer', 'Hawes', 'PF', 'Charlotte', 'Hornets', '6.110034']
 Results found: 6
['124', 'Courtney', 'Lee', 'SG', 'Charlotte', 'Hornets', '5.675']
 Results found: 7
['165', 'Cody', 'Zeller', 'C', 'Charlotte', 'Hornets', '4.2042']
 Results found: 8
['208', 'Jeremy', 'Lamb', 'SG', 'Charlotte', 'Hornets', '3.034356']
 Results found: 9
['219', 'Brian', 'Roberts', 'PG', 'Charlotte', 'Hornets', '2.85494']
 Results found: 10
['232', 'Frank', 'Kaminsky', 'C', 'Charlotte', 'Hornets', '2.61252']
 Results found: 11
['258', 'Jeremy', 'Lin', 'PG', 'Charlotte', 'Hornets', '2.139']
 Results found: 12
['319', 'P.J.', 'Hairston', 'SF', 'Charlotte', 'Hornets', '1.20144']
 Results found: 13
['360', 'Damien', 'Wilkins', 'SG', 'Charlotte', 'Hornets', '0.947276']
 Results found: 14
['361', 'Jorge', 'Gutierrez', 'PG', 'Charlotte', 'Hornets', '0.947276']
 Results found: 15
['362', 'Tyler', 'Hansbrough', 'PF', 'Charlotte', 'Hornets', '0.947276']
 Results found: 16
['363', 'Troy', 'Daniels', 'SG', 'Charlotte', 'Hornets', '0.947276']
 Results found: 17
['392', 'Aaron', 'Harrison', 'SG', 'Charlotte', 'Hornets', '0.525093']
 Results found: 18
```
The main option that I think has the most value is the Comparison option. This has two sub-options, comparing the average and minimum salary for both and counting the players per position.  For the first sub-option, I used average functions to calculate the average salary of both men and women and then I created a percentage to see how much of a difference there really is between them. The following is the output of that function:
```
What dataset do you want to see  3
1 - Compare average and min salary
2 - Players per position
Pick a category 
 1
Average NBA Salary($M): 5.074814482014392
Minimum NBA Salary($M): 0.030888

Average Women NBA Salary($M): 0.1453103448275863
Minimum WNBA Salary($M): 0.025

Average Men NBA salary is 3492.3972467588337% more than Women NBA Salary
```
These results are the most important one that this program produces. With this the user can see the wage gap. On average, Male NBA players make 5.07 million compared to .145 million made by female players. Although I did not include this statistic in the program, out of the 412 players in the NBA only twelve make below the female average. 
For the second sub-option, I created two dictionaries that count how many players play each position. I then created a visual for the results. Each asterisk represents a count of 5
```
NBA Position count: 
{'PF': 85, 'PG': 85, 'SG': 96, 'SF': 82, 'C': 69}

SG: *******************
C:  **************
SF: ****************
PG: *****************
PF: *****************

WNBA Position count: 
{'F': 51, 'G': 71, 'C': 23}

F: **************
G: **********
C: *****
```
**Overcoming the struggles**

While I was making my program, I had a few roadblocks. I was able to overcome these roadblocks with the help of my classmates and thinking through the problems myself. One problem that I had close to the end was the average functions for the salaries. I was able to store the last item of each row in a table and then find the average of all the values. This worked for the NBA file but not for the WNBA file. I kept getting the error: index out of range. I ran into this problem during the night and decided to continue working on other aspects of my program and return to the problem in the morning. When I woke up, I began working on it again. Through the use of print statements, I realized that one of my rows had empty spaces. This occurred when I was cleaning out my data in the initial stages of the project. When I realized my small mistake, it was aha moment. I was eager to eliminate the white spaces and see if my function worked and IT DID! 

Cleaning up the actual dataset was a crucial step in my project. I didn’t realize how much of a problem it would cause. It was by far what cost me the most time. Once I cleaned out the empty spaces, I went back and checked other columns and rows to see if I was missing anything. Through this I realized that my position column which I thought was the same for every row had some values other than player positions. I then cleaned those out too. 

Another thing that posed to be a problem for me was narrowing down what options I wanted the user to have. I didn’t want to overwhelm myself or the user with a bunch of options. I was able to put myself in the place of a user and decided which options were the best to have. 

**Milestones**

Creating, updating, and adding milestones throughout the past two weeks has been useful to my overall project journey. I started with vague milestones such as project requirements and ended up having specific milestones such as those for specific function. The more I got into my project, the more specific my milestones became because I knew what I wanted my program to do. I had to replace some of my options with other ones once I realized that they were not as useful as others. Looking back at my update 3 I realize that I listed more options than I have in my final project. Although this is the case, I still think my final project has useful information even though it doesn’t have everything that I originally planned. 

Completed:

 - [x] make men and women salaries into txt files 
 - [x] Check dataset for error
 - [x] create main menu
 - [x] create numbered options for men, women, compare 
 - [x] read through each data set
 - [x] create specific options for users under each data set
 - [x] create user option to see salary based on specific team
 - [x] create specific options for users under each data set
 - [x] change option to only search last name
 - [x] make table with all last names
 - [x] make table for position
 - [x] make dictionary of player positions
 - [x] create function to find mean
 - [x] print out male to female salary ratio
 - [x] create visualization
 - [x] allow user to see salary based on position

Not used/decided on other options:

 - [ ] allow user to see salary based on position
 - [ ] add random facts about the data
 - [ ] create dictionary with players and salaries
 - [ ] include regex

**Summary**

This class has allowed me to grow upon my programming skills and be confident in myself as a programmer. One of the goals that I had for myself was writing code without looking at examples. This project allowed me to do that. I was able to recall a lot of what I learned about opening files, creating dictionaries and list, and taking in user input. I did look back at class examples, but was not dependent on them like I was in the first half of this course. I hope to continue programming in python and use what I’ve learned in this class for other programming languages. 
