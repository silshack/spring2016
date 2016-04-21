---
author: namagic
layout: post
title: "Omar's Revised Project Plan 4/21"
---

I was finally able to add two new columns to my data by using various try and for loops. Some of the data, rather than numbers, lists just a "d", so I had to catch those and pass them in the except piece of a try and except. Figuring out the CSV module has taken a lot of my time, but I have learned a lot. I still haven't finished up everything I planned to do for Tuesday, but I started thinking through what I had planned for Thursday. After providing numbers for five major categories for each county, the next set of rows provides specific county inflow or outflow information to that county. I'll use the county destination code to use a startswith to find the needed rows. Luckily, what I had planned the last week is less busy than this week.

<iframe src="https://trinket.io/embed/python3/cd7a9bf6bf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
<h2>Milestones</h2>

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
- [ ] Devise method to find top three counties flowing into selected county that have a matching outflow counties
- [ ] Print out inflow, outflow, and net migration numbers for top three inflow counties with matching outflow counties
- [ ] Calculate net migration information by subtracting inflow and outflow returns and exemption numbers
- [ ] Print out numbers neatly for inflow, outflow, and net for selected county
- [ ] Visualization for county net migration
- [ ] Visualization for top county inflow

<h3>Until 4/29</h3>
- [ ] Add Census API to bring in basic info about county (population, households, median income)
- [ ] Make sure code is clean, commented
