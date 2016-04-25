---
layout: post
author: hannahlwang
title: "Hannah's Third Project Update"
---

https://github.com/hannahlwang/inls560-finalproject

###Revised Milestones

- [x] Set up Cloud9 workspace
- [x] Import CSV files
- [x] Write starter code to read files
- [x] Set up separate Github repo
- [x] Push code to Github repo
- [x] Clean up data or figure out another way to deal with commas in file names
- [x] Write code to print out summary of file
- [x] Determine what options will be available on main menu (and secondary menu(s), if needed)

- [x] Create dictionary of dictionary to print out statistics for each PID (UUID)
- [x] Format dictionary output for PID input so that it looks nice, is alphabetized

- [x] Create dictionary of object types
- [x] Create visualization of objects
- [x] Create key for object visualization

- [x] Create dictionary of MIME types
- [x] Create visualization of objects
- [x] Create key for object visualization
- [x] Use regex to make meaningful abbreviations of MIME types (part after slash)
- [x] Use conditionals to deal with exceptions to MIME type abbreviations

- [x] Create a list of file sizes
- [x] Use list of file sizes to calculate max, min, average

- [x] Deal with bad user input by creating while loops for each menu

- [x] Use while loop to create a quit command ('break')

- [x] Allow user to choose from list of possible data files

###Reflection

I did a TON of work on this over the weekend, because I don't think I will have time to work on it this week. It ended up being really fun! I decided to go with a four-tiered menu system: 

- first menu: allows the user to select a file
- second menu: allows the user to choose type of analysis they want to do (whole file or search by PID). The user can also ask for help text or quit here.
- third menu(a): allows the user to choose to analyze the file by object type, MIME type, or file size
- third menu(b): allows the user to enter a PID
- fourth menu: allows the user to return to the second menu, or quit

I ran into some issues with regex, and dealing with bad user input, but I'm happy that right now, everything at least works ok.

