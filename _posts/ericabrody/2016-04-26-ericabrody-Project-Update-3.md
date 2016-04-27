---
layout: post
author: ericabrody
title: 'Project Update 3'
---

A snapshot of my progress can be found in this GitHub repo: https://github.com/ericabrody/data_explore.git

Between Thursday and Saturday, I made a lot of progress. I got to a major hurdle trying to fomat the output for looking at univariate statistics for a variable by another variable (state/sex). The mean is a float with 2 decimal places, while all the other numbers are integers, so they just were not going to line up with tabs. Eric suggested I look at Python format strings and I found some helpful resources -- https://pyformat.info and http://www.python-course.eu/python3_formatted_output.php. It took a lot of time to parse the documentation to figure out exactly what I needed, but I finally got there with a lot of breaks and trial and error. I am confident that I will complete all the project requirements by Friday, but not sure how the stretch goals will go. 

Milestones Finished - 
[x] Review BRFSS documentation for 2014 and 2013 to identify which columns are associated with the variables I want to include in my datasets

[x] Import the desired variables from the 2013 and 2014 data files which are in fixed width format

[x] Convert the fixed width format into a csv format outside of my actual data analysis program (and require users who bring their own data to bring a csv)

[x] New (surpise milestone) Set up new GitHub repo and connect it to Cloud 9 to accomodate the data files that were too big and blew up my Trinket

[x] Input 2 csv data files into GitHub repo and stored them as a dictionary of a list of dictionaries using csv.DictReader after reading the python csv module documenation

[x] Created and review frequencies of each categorical variable using dictionary of response values

[x] Created dictionary of response values for categorical variables

[x] Create text visualization - horizontal bar chart of response values of any variable

[x] Calculate univariate statistics - min, mean, max, mode, median, range

[x] get function working that changes variable response values to response names as defined in “dataDictionary” dictionary in helpers.py

[x] :Calculate bivariate statistics for two specific variables- average tobacco use by state

[x] Generalize bivariate statistics into a function

[x] Create nicely formatted output for the univariate statistics

[x] Create nicely formatted table of bivariate statistics results - first for specific variables and then in generalized function

[x] Put results of twovar function that shows results of a categorical variable by state or sex or another variable into nicely formatted table - first for specific variables and then in a generalized function

[x] Create interface for stage 1 of user interaction - choose topic of interest from list of topics and year of data

[x] Create functionality for program to work with a “bring your own” dataset

[x] stretch goal - Functionality to print out nicely formatted output for categorical variable by state and sex

[x] stretch goal - generalize the categorical variable by state and sex and the corresponding nicely formatted output into functions

For Thursday: Finish creating user interface and documentation, possibly work on stretch goals

[ ] Create interface for stage 2 of user interaction - see data by sex or state or (look at a new topic and/or new year of data - i.e back to stage 1

[ ] Create interface for stage 3 of user interaction 

[ ] Create help document 

[ ] Create introduction to the program

[ ] Stretch Goal - create vertical bar charts

[ ] Stretch goal: create bar chart that shows results of one variable by another for specific variables tobacco use by state

[ ] Stretch goal: Generalize bar char of one var vs. another into a function
