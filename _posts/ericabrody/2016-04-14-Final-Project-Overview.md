---
layout: post
author: ericabrody
title: "Milestones- Revised"
---

Today's accomplishment: my 2 data files are in Trinket
Data: Health Survey (BRFSS) - Limited to 2 states: CT, NC so each file is about 15,000 observations and 11 variables
I did not include breast cancer screening, since this only applies to women and has a different denominator than the other variables in the set, and therefore could create havoc in my analyses. I also left out oral care because the question was asked in 2014, but not in 2013 - so it wasn't available for both datasets.  Age wasn't available in the file. But I did include gender. 

Removed stretch goal: set program up to accomodate new data files in fixed width format - i think it would be better to focus my energy on programming the user interface and calculations.

Milestones
Finished
  - [x] Review BRFSS documentation for 2014 and 2013 to identify which columns are associated with the variables I want to include in my datasets
  
  - [x] Import the desired variables from the 2013 and 2014 data files which are in fixed width format 
  
  - [x] Convert the fixed width format into a csv format outside of my actual data analysis program (and require users who bring their own data to bring a csv)

For Tuesday: Get functionality working
  - [ ] improve the header row of the data
  
  - [ ] create and review frequencies of each categorical variable and univariate statistics for each continuous variable

  - [ ] create functionality and user interface for data cleaning features - frequencies, univariate statistics, provide user choices for dealing with missing data
  
  - [ ] Calculate univariate statistics - min, mean, max, mode, median, range
  
  - [ ] Calculate bivariate statistics - average tobacco use by state, average health status by state, tobacco use by sex, etc.

  - [ ] Create text visualization - horizontal bar chart of any variable by any other variable (e.g., tobacco use by state, health status by year)

To be Scheduled: Create user interface
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


- Note: Visualizations may need to represent percents or 100s or 1000s of cases since sample size may be large

Order of programming: First, build the functionality of analyzing the two datasets, then build user interface, then to work on the “bring your own” dataset functionality.


Here is a little bit of starter code (which now has .txt data files in it):
<iframe src="https://trinket.io/embed/python/af11c255cc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

