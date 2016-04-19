---
layout: post
author: ericabrody
title: "Erica's Project Update 1"
---

My biggest roadblock is still envisioning the user interface - do they pick variable(s) of interest first and then table of results or histogram/barchart? How to convey which variables are available, etc. I am curious to see how others in my group plan to handle this. I have moved my milestone of creating a user interface for data cleaning to a stretch goal since I think this is more complicated than I first envisioned - at a minimum, it will require a lot of back and forth with the user, so I am not sure I will get to the point where the user interface is that robust. I want to focus on more basic functionality first.

I think my milestones are sufficiently ambitious, especially given the (large amount of) time devoted to the project thus far. As I move forward, I think it will be helpful if I can break down my milestones a little bit more into what the code actually needs to do. However, I think the biggest reason for not meeting all of my goals for this "deadline" is that I didn't expect my data files to be too big for trinket and thus, to be motivated to move into Cloud 9. There was definitely a learning curve for this. 

Also, I had originally thought to import my data as a list of lists, but I altered this plan after finding the csv module and the dictreader function that produces a dataset that is a set of dictionaries, i.e., each row in the dataset is a dictionary, where the keys are the variable names and the values are the value for that variable for that case/row. I liked this approach to dealing with the variable names and the data. So I spent a some more time reviewing the dictionary exercises we did in class and dictionary information in the book, Getting Started with Python, being used by the other section of 560 - which introduced the get function of dictionaries which is very helpful. In addition, when I produced frequencies of my variables, I hadn't realized that they would be ordered alphabetically by key (i.e., variable name) - so I spent time reviewing Python documentation on sorting (https://docs.python.org/3/howto/sorting.html) to get the output to be in order of values, starting with highest going to lowest. 


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

For Thursday: More Functionality

  - [ ] Delayed:Calculate univariate statistics - min, mean, max, mode, median, range
  
  - [ ] Delayed:Calculate bivariate statistics - average tobacco use by state, average health status by state, tobacco use by sex, etc.
  
  - [ ] Delayed: create bar chart that shows results of one variable by another (e.g., tobacco use by state)

To be Scheduled:  Create user interface    
  
   - [ ] Allow users to select which of the two states (or both) they would like to include in any analysis
  
  - [ ] Allow users to select which of the data sets (or both) they would like to include 
  
  - [ ] Allow users to select which statistics, visualization they would like to see

  - [ ] create interface so folks can select years and states and do multiple analyses without having to select years and states again and let them have the option of starting again with different states/years.

  - [ ] Create help document (do work on this as I program and set up features of the program)
  
  - [ ] Create introduction to the program
  
  - [ ] Create functionality for program to work with a "bring your own" dataset

Stretch goals:
  - [ ] stretch goal - Allow users to create tables of desired variables - e.g. average or median or mode of tobacco use by state by year

  - [ ] Stretch Goal - create vertical bar charts

  - [ ] stretch goal - import an entire dataset that the user brings and let them select the states of interest - the file is so big, this would require that I move development from trinket to C9.
  
  - [ ] create functionality and user interface for data cleaning features - frequencies, univariate statistics, provide user choices for dealing with missing data
