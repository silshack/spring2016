---
layout: post
author: jamesma560
title: "James Moore Project Update and Standup Report 3"
---
So this weekend I managed to get a lot done. 

Currently, the user is able to pick two options: search a candidate, or list the candidates by state. If they choose the ‘search a 
candidate’ option (by pressing 1) then an input string emerges where the user can type in a candidate whose campaign finance data that 
they want to see. The most difficult problem I had when coding this part of my program was how to handle input that didn’t precisely 
match the candidate names in my .csv file. Lucklily an advantage I had with my .csv files was that every single name was uniformly 
formatted (LAST_NAME, FIRST_NAME MIDDLE_NAME). So I knew that capitalization could be easily instilled on the user’s string 
using .upper(), but what about the order? What if a user only knows a candidate’s last name? Or only their first name? Or what if the 
name that the candidate is popularly addressed by isn’t the name that the candidate used to register with the FEC (for example, Bernie 
Sanders is recorded as Bernard Sanders in the .csv files). 

So this was a riddle I struggled with before going to a PyHack meetup at Francesca’s Café in Durham. At the meetup, I met an experience 
Python developer who helped me think through the problem. I don’t want to go into too much detail and spoil my report for this meetup, 
but he basically gave me the idea of splitting the user’s input on any spaces or commas they made include, and then applying .upper() 
to each element in the list of strings that are returned. So for example “sanders, Bernie” or “sanders bernie” would be [‘SANDERS’, 
BERNIE]. From there, I looped through this list of words and used the regex .findall() method to see if that single string matched 
anything in the candidate name row, and if it did, I would add that row into a new dictionary with an assigned numeric key.
Bottom line, if a user types in “Sanders, Bernie”, “BeRnIe, SaNDeRs” or whatever, it will stuff each row that matches the upper case 
version of each name element into a new dictionary. From there, the user will have another chance to pick a specific candidate from the
list of all the candidate names that matched their query. From their all they have to do is input the dictionary key associated with 
the candidate name that is displayed to show their information. 

Moving on to the second option, list candidate by state, I wanted to make an option that allowed a user to find all the candidate’s 
associated with a state. For someone like me, who is always mystified by the ambiguity of local politics, something like this would
really help out someone who’s just trying to find out what candidates are running in their state. The coding for this went by pretty
fast due to the pains I went through with my first option. The main (and recurring) challenge with this code was to ensure that the 
user knows that they need to input a valid two-letter state abbreviation. To solve this, I basically made a list of valid state 
abbreviations, and ensured that the user’s input (which I automatically capitalize) matched an item in that list. If it doesn’t, I 
print the list and give the user a chance to pick another valid state abbreviation.

From here, I want to be able to go back to the beginning, but I’m having some trouble. I can get back to the input prompt, but when the
user gets back to the beginning and tries to choose a second option, it doesn’t work. I suspect the problem involves not being able to 
iterate through the same dictionaries twice (a problem that vexed me earlier in code for this project), but that’s the next big hurtle.
From there, I just want to add a help option, refactor some code, and figure out what I’m going to do for a data visualization. 

Old Plan:

For Tuesday: 

- [ ] Figure out how to manipulate data in individual columns in the csv file.
- [ ] Figure out how to assign manipulations to each option. To be Scheduled: 
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
For Thursday: 
-	[ ] Figure out how to loop through my options as many times as my user wants (figure out how to loop through a dictionary multiple times).
-	[ ] Come up with a help option.
-	[ ] Add .csv files for different years.
-	[ ] Add more comments
-	[ ] Refactor code. 
-	[ ] Add data visualization to the state option (visualize their total contribution). 

