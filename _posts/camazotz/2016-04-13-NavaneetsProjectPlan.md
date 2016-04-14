---
layout: post
author: camazotz
title: "Navaneet's Project Idea and Work Plan!"
---

My project idea deals with the election results. I found a dataset on election data on Kaggle that gives all the voting information for each of the candidates by every county on every state. There is also an additional dataset that gives information on the demographic breakdown of every county.

The election data dataset consists of the number of votes cast for each candidate for each county as well as the candidate's political affiliation. My project goal is to build a user interface to obtain concise statistics on election data. There will be several modes of querying based on the fields available in the dataset (for example, query by state, query by party , query by candidate, etc.) and a way to switch between modes. If in the candidate mode, the user can type in the name of a candidate and be able to see the candidate's political affiliation, the fraction of votes they have garnered in each state, and the total fraction of votes they have gained.

I will alter the original dataset so that the user will be able to toggle between more than one data file and see how the election statistics vary (though one of the statistics will be fake). This way, the program will be generalizable to any files that contain these fields and as more election results come in, they can be fed in.

My milestones are as follows:

- [ ] Read all data into python lists
- [ ] Create a dictionary with each state as key and a candidate-party-vote tuple as value
- [ ] Create a dictionary with each candidate as key and a party-vote tuple as value
- [ ] Create a dictionary with each county as key and a state-party-candidate-vote tuple as value
- [ ] Build a user interface for the user to select three modes (state, candidate, and county)
- [ ] Have a help option to give the user directions on navigating the app
- [ ] For each mode, allow the user to enter any state, candidate, or county respectively and display the corresponding value tuple
- [ ] Allow the user to switch datasets
- [ ] For any query, display the fraction of votes as a bar graph (composed of asterisks) as a function of the votes and the mode that the user has selected (so if the user is in state mode, display the number of votes for each state as a bar graph)

If I have time left over, I would like to incorporate the additional dataset on county demographics and provide options for viewing that data as well. I also feel that handling a lot of these queries would be more effective if the data were fed into a database with candidate, state and county tables so I would like to explore Python's interface with MongoDB. However, this is a stretch goal if I have time remaining - the primary project milestones are covered by the above and should be sufficient for the achieving the purpose.
