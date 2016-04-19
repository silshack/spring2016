---
layout: post
author: gao14g
title: "Ga Kay's Project Idea & Work Plan"
--- 

## General Idea:
For the final project, I plan on making a text-based data analysis utility using Cloud 9. If I am unable to get Cloud 9 to work, I will use Python 3 Trinket, but I think it'll be a fun experience trying to figure out Cloud 9. The data set that I plan on using comes from a game called Eve Online. Firstly, there are four different data sets, one for each major trade station located in the game. Each data set contains a list of all (or at least most) of the potential items that you can trade in the game. The data is split between buy and sell which refers to buy orders and sell orders. In Eve Online, a buy order is an order users can put out when they want an item. They can get it at a cheaper price with a buy order, but they have to wait for the item. A buy order is very similar to a retailer buying from a wholesaler. A sell order is another type of order users can put out when they want an item. With a sell order, they will typically buy it at a higher price, but they receive the items instantly. A sell order is similar to a customer buying from a retailer. The data contains the volume, average, max, min, standard deviation, median, and percentile for both types of orders. I will analyze the data and allow users to search for specific items and see certain statistics about those items. To do this, I might create a dictionary of dictionaries for each item where I can easily access all the values of each item. I want to allow users to input a name and certain column and have the outputs for the query show up on the screen. I could also compute margin percentages between buy and sell if the user wants to know that information. There is another data set that I might use if I have the time. It shows all items and where they can be purchased for the cheapest price. 

## Required Milestones:

- [ ] include at at least two of the four data sets
- [ ] allow users to search through any type of data set
- [ ] have a text-based interface
- [ ] have a "help" function that the user can access by typing "/help" (or something similar to that)
- [ ] allow the user to keep searching for information until they want to exit the program
- [ ] visualize at least two to three of the text printouts
- [ ] include an introduction message for the user
- [ ] include at least three to four options for the user to choose from
- [ ] use try and except to handle bad input
- [ ] allow users to search for specific items and specific statistics about each item
- [ ] include at least one custom module, one dictionary, and one function
  - [ ] create a dictionary of dictionaries for each item in the file
  - [ ] create a function that allows the user to exit the program

## Stretch Goals:

- [ ] include all four data sets
- [ ] include additional data set about cheapest item locations
- [ ] integrate Eve Online's Crest API to pull more data
- [ ] allow visualization for all text printouts

## Revised Project Plan

### For Tuesday:

- [ ] import the csv files
- [ ] read through each data file
- [ ] include a welcome message for the user
- [ ] have the layout of my options menu 
  - [ ] include at least three to four options all with descriptive titles
  - [ ] create functions for at least one to two of the options

### To Be Scheduled:

- [ ] include functionality for all the options
- [ ] allow the printouts to be visualized 
- [ ] use try and except to handle bad user inputs
- [ ] implement help function that will print more instructions and tips for user when the user types "help"
