---
author: namagic
layout: post
title: "Omar's Revised Project Plan"
---

Updated Trinket: <iframe src="https://trinket.io/embed/python3/cd7a9bf6bf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<h2>Are there any roadblocks ahead? Is there anything your group can do to help out?</h2>

<h3>Snag 1</h3>
For this first update, I wanted to be able to print out inflow and outflow numbers neatly. When a user types in a desired county, the idea was that it would only print out the needed information; however, anytime Orange was typed, it would return every row with Orange in it. I was able to fix that by using two if statements with the words I was seeking that would ensure that no unnessecary data is printed out.

<h3>Snag 2</h3>
I am not sure how to manipulate a csv file to add a column as well as creating a function to subtract or add from different csv files. I couldn't find anything in the python documentation about adding a field. I can see how to add a new row, but not a field. 

<h3>Snag 3</h3>
Since I cannot figure out how to add a new column, I cannot create functions to add newly created fields.

<h2>Are your milestones ambitious enough? Make sure to include some stretch goalst?</h2>
I don't think they're too ambitious yet, but I might have to reevaluate by Thursday. I am behind on my plan though and I haven't fully thought about how to include the top three counties. However I believe I can do that by selecting the three rows under the "County Non-migrants" item. In regards to my own planning, I underestimated the difficulty in writing over a csv file. While the easy way out would be to edit the actual csv file and then read it, but that would defeat the purpose. Had I been able to anticipate this, I might have had more time to actually work on my code.

<h2>Explicitly state what you’re working on next and what you intend to accomplish before next class.</h2>
Before class on Thursday, my goal will be to finish up unfinished milestones that I had planned for Tuesday. Particularly in attemtping to resolve the snags noted above. I might need help though either from my group or more google searching. I think I have to open a csv file in write mode, but when I tried previously, I ended up deleting the information in the csv file.

<h2>Milestones</h2>

<h3>Already Completed</h3>
- [x] Create main menu with 5 options: main menu, using module data, add data, help, and exit
- [x] Create functions for each of the 5 options
- [x] Create while loop for cycling through options
- [x] Handle bad file name input
- [x] Allow user to select county

<h3>For Tuesday</h3>
- [x] Handle bad input for selected county
- [ ] Create working function to calculate household size: Exemptions/Returns
- [ ] Create working function to calculate AGI per Return: (AGI * 1000)/Returns
- [x] Find a method to print just inflow categories (US & Foreign; US; Same State; Different State; Foreign; Non-Migrants)
- [x] Find a method to print just outflow categories (US & Foreign; US; Same State; Different State; Foreign; Non-Migrants)
- [ ] Calculate net migration information by subtracting inflow and outflow returns and exemption numbers
- [ ] Create working function to calculate AGI for net migration
- [ ] Print out numbers neatly for inflow, outflow, and net for selected county

<h3>For Thursday</h3>
- [ ] Devise method to find top three couunties flowing into selected county that have a matching outflow counties
- [ ] Print out inflow, outflow, and net migration numbers for top three inflow counties with matching outflow counties

<h3>For Tuesday (4/25)</h3>
- [ ] Visualization for county net migration
- [ ] Visualization for top county inflow

<h3>Until 4/29</h3>
- [ ] Add Census API to bring in basic info about county (population, households, median income)
- [ ] Make sure code is clean, commented


<iframe src="https://trinket.io/embed/python3/cd7a9bf6bf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
