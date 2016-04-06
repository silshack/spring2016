---
layout: post
author: wagerpascal
title: "Jason's MOAR Dictionary Exercises"
---

Exercise 1:
<iframe src="https://trinket.io/embed/python3/614d07666b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 2:
<iframe src="https://trinket.io/embed/python3/8d7205e1b0" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
The first exercise was pretty straightforward, as splitting the words into a list will allow for easy allocation as keys through a loop.

For the rest of the exercises, I managed to extract the correct values using regex. It was pretty simple to isolate the desired lines through searching for lines starting with "From" and have "somecharacters"@"domainname", and isolating the desired pieces of data from there. For days, it was simply describing the position in terms to the email address.
After taking out the data, I could make a list of lists, and do a similar analysis to what occurred in the last exercise for counting number of instances.

Exercise 4 required two outside variables to hold the currently largest value. It was tricky to get my bearings regarding comparing the numbers, but once that was cleared up, it was easy to set up. Exercise 5 was much like Exercise 2/3, only that I used regex to specifically pull out the email domains.
