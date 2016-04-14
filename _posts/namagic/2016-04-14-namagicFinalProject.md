---
author: namagic
layout: post
title: "Omar's Final Project Plan"
---

<h2>Background</h2>
I am choosing to work on the data analysis project. For this project, I will be using IRS tax migration data. While working at the Development Finance Initiative, I have had to calculate net migration by looking up inflow and outflow migration numbers for the particular county I am researching. To do so, I download the year-to-year inflow and outflow numbers for NC in an excel file and use VLOOKUP to locate the particular county I am seeking out. 

The inflow and outflow data is categorized into broadly into the following categories: US, Same State, Different State, Foreign, and non-migrants. In addition to those broad categories, each county includes all the inflow and outflow numbers for each county that intersects with the county I am interested in. Thus, I can determine the top counties that have a lot of inflow and outflow into the chosen county. For both inflow and outflow datasets, I have the following information: returns, exemptions, and average gross income. With that information, I can also calculate household size and average gross income per return to get a more accurate household income. This is all done for each year I’m interested in, typically interested to see a trend line over 3 years to see who is coming into the chosen county. For example, in Iredell County, it’s interesting to note how many people are coming in from Mecklenburg County which is generally wealthier than Iredell County. 

<h2>Ideal Project</h2>
The ideal project would be to incorporate 6 datasets, inflow and outflow data for three years. If this project is idealized, this actually would be a humongous help to DFI because this research is done for each county we work with. Not only could additional years be added, but the user would be able to get results immediately rather than open haphazardly stored information. Each dataset is roughly half a megabyte. Each dataset has been saved as a TSV. The user would type out a county name and receive the following output.

<h3>INFLOW 2013-14</h3>
<p><b>County Total Migration – US and Foreign:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – US:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Same State:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Different State:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Foreign:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Non-Migrants:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>

<h3>OUTFLOW 2013-2014</h3>
<p><b>County Total Migration – US and Foreign:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – US:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Same State:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Different State:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Foreign:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Non-Migrants:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>

<h3>NET MIGRATION 2013-2014</h3>
<p><b>County Total Migration – US and Foreign:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – US:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Same State:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Different State:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Total Migration – Foreign:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>
<p><b>County Non-Migrants:</b> Returns, Exemptions, AGI, HH Size, AGI/Return</p>

<h2>Scaled Down Project</h2>
For this particular project, I will first focus on one dataset, 2013-2014 inflow data. The user should be able to type a county name and get inflow, outflow, and net migration information. Net migration is simply inflow minus outflow. I am planning one visualization to be histogram of the various categories (Same State, Different State…) and another visualization to capture the top inflow counties for the county being asked for.

Thus, total there’d be two datasets, inflow 2013-14 and outflow 2013-14. It’ll be generalizable for IRS tax migration year data, specifically county to county data. Prior to 2011, the categories are slightly different which will be something that needs to be incorporated (but smaller priority).

<h2>Optional</h2>

1.	Include Google Maps API to get information about requested county
2.	Incorporate prior categorizations of data 

Thus far,	I have downloaded my data and put them in a <a href:"https://trinket.io/python3/be39bd49ee">trinket</a>.
