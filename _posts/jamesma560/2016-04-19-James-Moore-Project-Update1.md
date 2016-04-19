---
layout: post
author: jamesma560
title: "James Moore Project Update and Stand Up Report 1"
---

So far I have gotten a python file working on Cloud9, and I feel pretty comfortable with the interface so far. I was also able to upload 
my CampaignSummary.csv file to my python program (Campaign.py) and I was able to make a list of the column headers and print them
out as options (1-23). This was a pretty big step and it went a lot easier than I thought it would (I didn't even have to mess with the
csv file!). I was also able to create a loop of simple user options and suboptions. Using that nest, I should be able to input certain
functions within each option. 

Milestones Finished: 

- [x] figure out how to make a simple .py file in Cloud9
- [x] Figure out how to get a .py file to interact with a .csv file on Cloud9.
- [x] Create and display list of column headers.
- [x] Create loop of options.

For Thursday:
- [ ] Make dictionary of dictionaries.
- [ ] set campaign_name as key, type in column row name as key and column value as the value.
- [ ] Figure out how to manipulate data in individual columns in the csv file.
- [ ] Figure out how to assign manipulations to each option.

To be Scheduled: 

- [ ] Prompt the user to pick the name of a .csv file.
- [ ] Figure out how a user’s .csv file would work with a program made on Cloud9.
- [ ] Display 3rd tier of user input. Whether they want to pick another column (1), sort the column they picked (2), (3) filter, (4) or find a candidate (for campaignsummaryaction.csv only).
- [ ] If they pick filter, allow the user to enter a string, and only display the records displaying the column value the user selected.Match the user selection with records with the matching column values and display
- [ ] After sorting and filtering, allow the user to choose whether they want to sort their results (if they picked filter) or filter their results further (if they picked sort) or start all over and go back to the place where they pick a .csv file.
- [ ] Going back to the first tier, if they pick find a candidate, prompt the user for a string describing the name of candidate they want to look up, match that string with the corresponding value in candidate_name, and data visualize the corresponding column values for that record, using the model given in the assignment description (instead of asterisks use dollar signs).
- [ ] Create list of candidate names
- [ ] Match user’s input with correct name
 - [ ]Figure out how to visualize each column value
- [ ] Figure out how to deal with incomplete names.
