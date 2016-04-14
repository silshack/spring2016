---
layout: post
author: ericabrody
title: "Final project idea & work plan"
---

My final project will allow users to explore a dataset called, the Behavioral Risk Factor Surveillance Survey (BRFSS). This is an annual survey of individuals throughout the US, reported by state, that measures various behavioral risk factors for health problems. The public use data files are provided for each year of the survey in fixed width format and SAS format. I plan to include the files for the most recent two years of data available, 2013 and 2014. Users who would like to examine older data, can "bring their own data." 

Each data set is quite large, so I plan to include a subset of variables in the data files I provide. Specifically, I plan to include variables that allow users to look at tobacco use, exercise, health status, healthy days health-related quality of life, inadequate sleep, alcohol consumption, oral health, and screening for breast cancers. Gender and age will also be in the data for analysis. To decrease the number of observations in the dataset, I will restrict the data to individuals from 3 states - California, North Carolina, and Connecticut. 

Milestones:
  - [ ] Review BRFSS documentation for 2014 and 2013 to identify which columns are associated with the variables I want to include in my datasets
  - [ ] Import the desired variables from the 2013 and 2014 data files which are in fixed width format 
  - [ ] Possibly convert the fixed width format into a csv format outside of my actual data analysis program (and require users who bring their own data to bring a csv)
  - [ ] Possible stretch goal - set program up to accomodate new data files in fixed width format
  - [ ] stretch goal - import an entire dataset that the user brings and let them select the states of interest
  - [ ] Allow users to print a frequency table of each variable so they can find unexpected or bad data
  - [ ] The BRFSS documentation indicates that 9, 99, and 999 are used as missing values/bad data, so I need to figure out a way to handle them in my program 
  - [ ] Create help document (do work on this as I program and set up features of the program)
  - [ ] Create introduction to the program
  - [ ] Calculate univariate statistics - min, mean, max, mode, median, range
  - [ ] Calculate bivariate statistics - average tobacco use by state, average health status by state
  - [ ] stretch goal - Allow users to create tables of desired variables - e.g. average or median or mode of tobacco use by state by year
  - [ ] stretch goal - Allow users to select which of the three states they would like to include in any analysis
  - [ ] Allow users to create text visualization - horizontal bar chart of any variable by any other variable (e.g., tobacco use by state, health status by year)
  - [ ] Stretch Goal - create vertical bar charts

- Note: Visualizations may need to represent percents or 100s or 1000s of cases since sample size may be large

Order of programming: First get all features working on my two datasets, then to work on the “bring your own”

Questions:

1. The BRFSS data is available in fixed width format and as a SAS dataset. I googled and found a SAS package for Python. Importing a SAS dataset into Python sounds like a potentially realistic scenario. Would you recommend dealing with the fixed width format or the SAS? Would I be able to import the SAS module into Trinket or would this require me to use C9?

2. If I use one module to import data and assign variable names to each element, will those variables be available in other modules? or will these need to be defined as global variables?

Here is a little bit of starter code:
<iframe src="https://trinket.io/embed/python/af11c255cc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I am still having a little trouble envisioning exactly what data analysis features to offer and how the user interface will work. Hopefully, this will become clearer once I have my analysis datasets in my Trinket and talk to other students in class
