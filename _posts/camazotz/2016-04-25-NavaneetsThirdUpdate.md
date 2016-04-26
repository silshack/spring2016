---
layout: post
author: camazotz
title: "Navaneet's Project Update 3!"
---

My revised milestones from last class are:

- [x] Read all data into python lists
- [x] Create a dictionary with each state as key and as value another dictionary with candidate as key and vote as value
- [x] Create a dictionary with each candidate as key and as value another dictionary with state as key and vote as value
- [x] Create a dictionary with each county as key and as value another dictionary with candidate as key and vote as value
- [x] Create a dictionary with each county as key and as value another dictionary with party as key and vote as value
- [x] Create a dictionary with each state as key and as value another dictionary with party as key and vote as value
- [x] Build a user interface for the user to select three modes (state, candidate, and county)
- [x] Have a help option to give the user directions on navigating the app
- [x] Create actual help instructions
- [x] For each mode, allow the user to enter any state, candidate, or county respectively and display the corresponding value(s)
- [x] Allow the user to switch datasets
- [x] Allow the user to enter different column addresses for the fields of data
- [ ] Modularize code
- [ ] Comment code
- [x] For any query, display the fraction of votes as a bar graph (composed of asterisks) as a function of the votes and the mode that the user has selected (so if the user is in state mode, display the number of votes for each state as a bar graph)

Reflection:

I've completed the majority of the tasks. All that remains is to modularize and comment the code. One challenge I ran into during this last portion of the project was randomizing the Excel data. I didn't want to use arbitrary numbers because that wouldn't be representative of actual votes cast. So searched [online](http://answers.microsoft.com/en-us/office/forum/office_2007-excel/how-to-randomize-data-in-excelspreadsheets/399ec67b-a443-e011-9bac-78e7d160ad4e?auth=1) and found a few Excel functions that allowed me to do so. I made three fake datasets using the method I found.
