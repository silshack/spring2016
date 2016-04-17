---
author: clairewlj
layout: post
title: "Lingjie's Final Project Plan & Milestones"
---

Datasets: 
two datasets, which arelist of medals at the Summer and Winter Games of the Olympiad per edition(year), sport, discipline, gender and event.

What to do:
Currently I plan to firstly create clearly structured table of medals using dictionary and lists, then display a descriptive summary (data type, format, value) of the dataset, such as the range of years included, the total numbers of countries, sports, disciplines and events involved, etc. Then based on users' queries, the program will display selected data, such as showing the number of gold/silver/bronze medals won in one/some specific year/city/sport/discipline/event by one/some specific country/gender. Also, I'll try to display bar/line graphs or scatterplots according to users' ask. The types of visualizations the program is able to display will be shown in the instructions for the users.

Milestones:

For Next Tuesday:

- [ ] Import two csv files into Cloud9 and PyCharm
- [ ] Read files correctly
- [ ] Create combinations of lists and dictionaries for extracting data from the dataset and storing it in a well-structured format
- [ ] Clean Data and make sure the elements of lines_table is orgnized
- [ ] Write function to ask user for filename and open/read it
- [ ] Write code to handle user's bad input
- [ ] Set up basic display of data file opened 

To be scheduled:

- [ ] Display explanatory features(data type, format, value) of the dataset selected by the user, such as the range of years included, the total numbers of countries, sports, disciplines and events involved, etc.
- [ ] Display original instructions for users, including types of data/visualizations can be selected to view
- [ ] Write help instructions
- [ ] Write code to allow users select one or more specific filters
- [ ] Use loops to allow users re-start selecting filters
- [ ] Use screen.onkey to allow users exit the program

Strech Goals:

- [ ] Create class to simplify program
- [ ] Create functions to create different types of visualizations (bar/line charts, scatter plots, etc)
- [ ] Possible Create functions to allow users to change some of the filters chosen
