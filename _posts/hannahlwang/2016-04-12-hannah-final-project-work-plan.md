---
layout: post
author: hannahlwang
title: "Final Project Work Plan"
---

I am going to build an application to do data analysis on CSV exports from the Carolina Digital Repository. In the internal admin interface, we have the option to export CSV files that tell you information about different collections. I will be using only files from collections that are public, so I will not be doing any analysis on private or unpublished works. The user will be able to select a CSV file and choose the type of analysis they would like to perform. The types of actions I want to allow are: counting the number of different object types, counting the number of different MIME types, finding the max and min file sizes, finding the folders with the least and most children. I plan to visualize these with histograms. However, since some of these actions will yield numbers in the thousands, I will be printing out a simplified histogram that scales down the output. 

I would like practice using the Cloud9 IDE, so I will first have to set up a workspace.

Here are my milestones:

- [ ] Set up Cloud9 workspace
- [ ] Set up separate Github repo
- [ ] Import CSV files
- [ ] Write starter code
- [ ] Write code to read and analyze data, produce outputs
- [ ] Write code to create visualizations
- [ ] Push code to Github repo
