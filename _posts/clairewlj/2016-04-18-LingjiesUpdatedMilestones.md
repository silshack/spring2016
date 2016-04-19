---
author: clairewlj
layout: post
title: "Lingjie's Project Updates & Stand-up 1"
---

Reflection: I basically complete the tasks stated in the milestones for Tuesday. I figured out how to use both Cloud9 and PyCharm to write the program, and uploaded two csv data files. One problem I met was about the version of python when using Cloud9. It seems that .readlines() could not work in python 2, and that I still need to choose the version of python 3 even with the line #!/usr/bin/python. I'm not sure if there's something wrong about it.

For the data management part, I first created a list for the file, each element is a list gained by line.split(';'). Then I cleaned data by removing the first and last 3 lines, and created a dictionary, whose keys are the variable names such as 'Year', 'City', 'Sports', etc, and the value of each key is a list of unique value of each variable, such as different years, etc. That was for displaying basic information, like 'how many hosts cities were in the file', 'what's the range of years of the dataset'. I'm planning to create dictionary of dictionaries for different sports types and sports events. I choose to delay dealing with the bad input problem to the last procedure as I think it's more suitable to be done with the more interactive parts.

Updated Milestones:
For Tuesday:

- [x] Import two csv files into Cloud9 and PyCharm
- [x] Read files correctly
- [x] Create combinations of lists and dictionaries for extracting data from the dataset and storing it in a well-structured format
- [x] Clean Data and make sure the elements of lines_table is orgnized
- [x] Write function to ask user for filename and open/read it

For Thursday:

- [ ] Create dictionary of dictionary for different sports types
- [ ] Write code to handle user's bad input
- [ ] Set up basic display of data file opened 
- [ ] Display explanatory features(data type, format, value) of the dataset selected by the user, such as the range of years included, the total numbers of countries, sports, disciplines and events involved, etc.
- [ ] Display original instructions for users, including types of data/visualizations can be selected to view

To be scheduled:

- [ ] Write help instructions
- [ ] Write code to allow users select one or more specific filters
- [ ] Use loops to allow users re-start selecting filters
- [ ] Use screen.onkey to allow users exit the program

Strech Goals:

- [ ] Create class to simplify program
- [ ] Create functions to create different types of visualizations (bar/line charts, scatter plots, etc)
- [ ] Possible Create functions to allow users change some of the filters chosen

------------------------------------------------
Previous Milestones:
For Next Tuesday:

- [ ] Import two csv files into Cloud9 and PyCharm
- [ ] Read files correctly
- [ ] Create combinations of lists and dictionaries for extracting data from the dataset and storing it in a well-structured format
- [ ] Clean Data and make sure the elements of lines_table is orgnized
- [ ] Write function to ask user for filename and open/read it
- [ ] Write code to handle user's bad input
- [ ] Set up basic display of data file opened 
