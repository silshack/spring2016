---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Final Project Milestones"
---

For my final project, I am going to create a data analysis tool for analyzing the frequency of U.S. baby names throughout the years.  The data that I found was through Kaggle.com.  I went ahead and downloaded the file to make sure that it would be applicable to this project.  The file has both National and State data attached to it, which will be useful, since I can use that to allow the user to choose which they'd like to see for either option.  

The data that is contained within each of these files is ID#, Name, Year, Gender, and Count.  From this data, I see a good number of statistical operations that could be useful.  The way that I envision this program working is that if users search for a specific name, or parts of a name (ex: A*), then I want to produce a graph that shows the output of these results.  This might be tricky, since some of the names are used thousands of times in one year; for instance, the name Mary was given to 7,065 lucky indivduals in the year 1880.  I'll have to think about a creative way to express certain values without breaking my program completely.  I might just remove the data in my set for names that occur over 50 times in a year, to help make this program more usable.

In addition to returning a graph that depicts the results of the frequency of the user's inputted name per year, I'll want to show some general statistics, such as the mean, median, maximum, and minimum for that name or set of names in general.  Having these statistics also makes my tool generalizable to different types of data sets, since if a person were to type in the name or certain criteria parts, then they would be able to pull statistics out for a specific criteria.

Here are some of the milestones that I'll need to make sure I am able to properly conquer this project:

- [ ] Have the program ask for user input (so they select from either National or State data)
- [ ] Have users type "Help" to be directed to a page that gives them more detail about the program
- [ ] Have users type "Finished" (or other appropriate command) to allow them to exit from the program
- [ ] Figure out how to have the user upload their data that they might want analyzed by my program *be sure to clarify with Elliott that he doesn't mean to just have the user copy and paste their own data into a file in my program*
- [ ] Produce a graph that visualizes the input the user entered. Baby milestones are below to grow to this:
- [ ] Create a dictionary to hold each name and the value associated with that name
- [ ] Create a for loop that goes through the data
- [ ] For each matching entry in the for loop, add this to the dictionary with the value
- [ ] Have the output print the name(s) with either * or some sort of visual symbol equal to the number of counts for each entry
- [ ] Determine if I want to place limits on the number of data outputs printed or can figure out a way to be more creative
- [ ] After the initial data is printed for the user, allow them to have the opportunity to enter more input
- [ ] Produce some statistics from the data that the user has asked for. Baby milestones are below to grow to this:
- [ ] Print the mean.  To do this, I'll need to get the sum and total count of values to figure this out
- [ ] Print the median.  To do this, I'll need to use the total count of values and put it in the median formula
- [ ] Print the maximum. To do this, I could use the maximum function 
- [ ] Print the minimum.  To do this, I could use the minimum function
- [ ] See if I can create functions for these actions
      
      
