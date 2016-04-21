---
layout: post
author: jamesma560
title: "James Moore Project Update and Standup Report 2"
---

To be honest I didn’t realy have a chance to work on my project that much since Tuesday do to an excess of projects in other classes. But despite that I still feel like I did something meaningful.
As a milestone for Thursday’s class, I mainly wanted to explore the .csv module, to see if it would process my data in a cleaner way. Fortunately I was able to utilize the csv.reader() function, which really  formatted my data better than the way I was doing it before (just using .readlines()). So I basically made this my main.py as opposed to campaign.py (although I kept campaign.py because there is some useful stuff in there).
In addition to this csv module epiphany I was also able to create a dictionary where each ‘Candidate_ID’ is a key to another dictionary which lists the column value for each corresponding ‘Candidate_ID’. I was inspired to do this by suggestions from the last group meetup we had last Tuesday. Another thing  I did was I deleted the first column from my .csv file, since all it contained were URLs that weren’t really that interesting and I wanted the CandiateID to be the first column (as the primary key). 

Old Plan: 

For Thursday:
- [x] Make dictionary of dictionaries.
- [x] set campaign_name as key, type in column row name as key and column value as the value.
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
- [ ] Figure out how to visualize each column value
- [ ] Figure out how to deal with incomplete names.

New Plan: 
For Tuesday: 
- [ ] Figure out how to manipulate data in individual columns in the csv file.
- [ ] Figure out how to assign manipulations to each option.
To be Scheduled: 
- [ ] Figure out how a user’s .csv file would work with a program made on Cloud9.
- [ ] Display 3rd tier of user input. Whether they want to pick another column (1), sort the column they picked (2), (3) filter, (4) or find a candidate (for campaignsummaryaction.csv only).
- [ ] If they pick filter, allow the user to enter a string, and only display the records displaying the column value the user selected.Match the user selection with records with the matching column values and display
- [ ] After sorting and filtering, allow the user to choose whether they want to sort their results (if they picked filter) or filter their results further (if they picked sort) or start all over and go back to the place where they pick a .csv file.
- [ ] Going back to the first tier, if they pick find a candidate, prompt the user for a string describing the name of candidate they want to look up, match that string with the corresponding value in candidate_name, and data visualize the corresponding column values for that record, using the model given in the assignment description (instead of asterisks use dollar signs).
- [ ] Create list of candidate names
- [ ] Match user’s input with correct name
- [ ] Figure out how to visualize each column value
- [ ] Figure out how to deal with incomplete names.




