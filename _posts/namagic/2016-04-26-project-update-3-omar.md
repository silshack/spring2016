---
author: namagic
layout: post
title: "Omar's Revised Project Plan 4/21"
---

<iframe src="https://trinket.io/embed/python3/946209e5a5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Still my largest roadblock here has been my inability to subtract from different csv files, while I was able to make formulas for the equations needed to be calculated, I'm not sure how to type the code properly. I definitely didn't complete my desired milestones; however, I did read through documentation on pulling in census API information. I attempted to not use the csv module but I ended up spending more time attempting to recreate my program than achieve anything in additon. My visualizations have been stalled because I haven't been able to incorporate information that I need, namely subtracting from two different files.


<h3>Already Completed</h3>
- [x] Create main menu with 5 options: main menu, using module data, add data, help, and exit
- [x] Create functions for each of the 5 options
- [x] Create while loop for cycling through options
- [x] Handle bad file name input
- [x] Allow user to select county

<h3>For Tuesday</h3>
- [x] Handle bad input for selected county
- [x] Find a method to print just inflow categories (US & Foreign; US; Same State; Different State; Foreign; Non-Migrants)
- [x] Find a method to print just outflow categories (US & Foreign; US; Same State; Different State; Foreign; Non-Migrants)

<h3>For Thursday</h3>
- [x] Create working function to calculate AGI for net migration
- [x] Create working function to calculate household size: Exemptions/Returns
- [x] Create working function to calculate AGI per Return: (AGI * 1000)/Returns

<h3>For Tuesday (4/25)</h3>
- [x] Devise method to find top three counties flowing into selected county that have a matching outflow counties


<h3>Until 4/29</h3>
- [ ] Print out inflow, outflow, and net migration numbers for top three inflow counties with matching outflow counties
- [ ] Calculate net migration information by subtracting inflow and outflow returns and exemption numbers
- [ ] Print out numbers neatly for inflow, outflow, and net for selected county
- [x] Visualization for top county inflow
- [ ] Visualization for county net migration
- [ ] Add Census API to bring in basic info about county (population, households, median income)
- [ ] Make sure code is clean, commented
