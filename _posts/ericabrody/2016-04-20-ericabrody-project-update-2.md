---
layout: post
author: ericabrody
title: "Erica's Project Update 2"
---

A snapshot of my progress can be found in this GitHub repo: https://github.com/ericabrody/data_explore.git

Once again, I did not accomplish as much as I had hoped; however, I took this opportunity to better specify my milestones so that as I move forward, progress is (hopefully) more swift. Up until now, I have been conflicted about spending my time coding (which is what i have done) versus planning and (which I am prioritizing for submission of this update). I think without small enough chunks in my milestones, I am having trouble staying focused on my work. I am also optimistic about my progress going forward as I have become more systematic in my approach to developing the code for the data analysis program. I figure out the functionality (e.g., creating the mode of a variable) using a specific variable and then I write a function that "generalizes" that code so it can be used with any dataset, variable(s). I don't see any specific roadblocks at this time as I hope to be able to build upon the work I have done so far to finish coding the "data analysis functionality" and then work on the user interface.

Since last class, I have also come up with some ideas for my approach to the user interface. I will ask users what topic they are interested in and what year they would like to know about. Topics include: general health (2 variables), sleep (1 variable), smoking (2 variables), exercise (1 variable), alcohol (2 or 3 variables (not sure if I am going to keep one of the three)). Then I will provide the most basic information for that variable (basic info for continuous variables = mean, mode, median; basic info for categorical variables - frequency distribution by table and graph). Then I can ask users if they would like to see the data broken down by state or sex or pick a new topic. The third potential step for users will be to ask if they would like to see these variables broken down by state or sex again (so they can pick the other choice that they didn't see before - or if I get fancy, ask users if they want to see the breakdown by the other variable that they haven't seen), or to see another topic and/or year. My milestones related to user interface have been edited to reflect this flow of interaction with users.

Milestones
Finished
  - [x] Review BRFSS documentation for 2014 and 2013 to identify which columns are associated with the variables I want to include in my datasets
  
  - [x] Import the desired variables from the 2013 and 2014 data files which are in fixed width format 
  
  - [x] Convert the fixed width format into a csv format outside of my actual data analysis program (and require users who bring their own data to bring a csv)
  
  - [x] New (surpise milestone) Set up new GitHub repo and connect it to Cloud 9 to accomodate the data files that were too big and blew up my Trinket
  
  - [x] Input 2 csv data files into GitHub repo and stored them as a dictionary of a list of dictionaries using csv.DictReader after reading the python csv module documenation
  
  - [x] Created and review frequencies of each categorical variable using dictionary of response values
  
  - [x] Created dictionary of response values for categorical variables
  
  - [x] Create text visualization - horizontal bar chart of response values of any variable 

  - [x] Calculate univariate statistics - min, mean, max, mode, median, range
  

For Tuesday:  Finish creating functionality and Create user interface (which includes pretty display of results)
  
  - [ ] Delayed:Calculate bivariate statistics for two specific variables- average tobacco use by state
  
  - [ ] Generalize bivariate statistics into a function
  
  - [ ] Create nicely formatted output for the univariate statistics
  
  - [ ] Create nicely formatted table of bivariate statistics results - first for specific variables and then in generalized function
  
  - [ ] Delayed: create bar chart that shows results of one variable by another for specific variables tobacco use by state
  
  - [ ] Generalize bar char of one var vs. another into a function
  
  - [ ] Put results of twovar function that shows results of a variable by state or sex or another variable into nicely formatted table - first for specific variables and then in a generalized function
  
  - [ ] Create interface for stage 1 of user interaction - choose topic of interest from list of topics and year of data
  
  - [ ] Create interface for stage 2 of user interaction - see data by sex or state or (look at a new topic and/or new year of data - i.e back to stage 1
  
  - [ ] Create interface for stage 3 of user interaction - see data by sex or state (so they can see the breakdown that they haven't seen) or go back to stage 1 (look at new topic and/or new year of data) 

To be scheduled:

  - [ ] Create help document (do work on this as I program and set up features of the program)
  
  - [ ] Create introduction to the program
  
  - [ ] Create functionality for program to work with a "bring your own" dataset

Stretch goals:
  - [ ] stretch goal - Functionality to look at categorical variables by state and sex, first with a specific variable
  
  - [ ] stretch goal - Functionality to print out nicely formatted output for categorical variable by state and sex
  
  - [ ] stretch goal - generalize the categorical variable by state and sex and the corresponding nicely formatted output into functions

  - [ ] Stretch Goal - create vertical bar charts

  
