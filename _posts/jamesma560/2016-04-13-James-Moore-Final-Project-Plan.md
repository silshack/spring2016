---
layout: post
author: jamesma560
title: "James Moore Project Plan"
---


For my final project, I will be taking the data analysis route using the Cloud9 environment.

I downloaded a .csv file from fec.gov entitled "CandidateSummaryAction.csv" that lists campaign donations by candidate. According 
to the FEC's website, this file "contains information for each candidate who has registered with the FEC or appears on an official
state ballot for an election to the U.S. House of Representatives, U.S. Senate or U.S. President.". At first glance, this .csv file
was intimidating due to some of the opaque column titles (ex. "cas_on_han_beg_of_per"), but thankfully the FEC provides a handy
metadata guide that helped explain the purpose of the columns. Another thing that indimidated me about the .csv file is that it contained
50 columns, and I haven't decided whether to just exclude the columns that are uninteresting or to just keep them. Either way
I do plan on changing the column titles to make the .csv file more user-freindly to work with.

For my project I want to create a command-line-like interface that can sort and filter through any csv file. Essentially I will have the 
user pick a column, and then I will let them decide whether they want to sort the column in ascending or descending order or whether they 
want to filter a column to only display those records that contain a certain column value. I also want to include a special 'find' selection
for my .csv file exclusively, that will take a user candidate name query, and print out a data visualization for that candidate's record
in CandidateSummaryAction.csv

- [] Preliminary Milestones
  - [] Figure out how to make a simple .py file in Cloud9
  - [] Figure out how to get a .py file to interact with a .csv file on Cloud9.
  - [] Create special final project repo on Github
  - [] Figure out how to commit push Cloud 9 code to Github final project repo.
- [] Figure out how I want to store the .csv file
  - [] Option 1: List of lists
    - [] .readlines() the file to make a list of lines. 
    - [] create empty table. Use for loop to .append.split(",") the lines from the .readlines() method to that empty table. Making
    a list of lists (of each record). 
  -[] Option 2: A dictionary of lists
    - [] Using the list of lists from option 1, make a dictionary where each candidate is a key, where the value is a dictionary of column 
    titles (keys) and the column values (values). 
  - [] Prompt the user to pick the name of a .csv file.
  - [] Figure out how a user's .csv file would work with a program made on Cloud9.
  - [] Display the .csv files column names (the first list in the list of lists). Ask the user to pick a column name
  - [] Cycle through the .csv file and make a list of column names if above strategy doesn't work out.
  - [] Display 3rd tier of user input. Whether they want to pick another column (1), sort the column they picked (2), (3) filter, (4) or 
  find a candidate (for campaignsummaryaction.csv only). 
    - [] If they pick sort, allow the user to choose whether to sort in ascending or descending order. Sort the column.
    - [] If they pick filter, allow the user to enter a string, and only display the records displaying the column value the user 
    selected.Match the user selection with records with the matching column values and display
    - [] After sorting and filtering, allow the user to choose whether they want to sort their results (if they picked filter) or 
    filter their results further (if they picked sort) or start all over and go back to the place where they pick a .csv file.
    - [] Going back to the first tier, if they pick find a candidate, prompt the user for a string describing the name of candidate
    they want to look up, match that string with the corresponding value in candidate_name, and data visualize the corresponding column
    values for that record, using the model given in the assignment description (instead of asterisks use dollar signs).
      -[] Create list of candidate names
      - [] Match user's input with correct name
      -[] Figure out how to visualize each column value
      -[] Figure out how to deal with incomplete names. 
  
