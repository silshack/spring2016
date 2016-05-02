---
layout: post
author: jamesma560
title: "James Moore Final Project"
---

Snapshot of final project: https://github.com/jamesma560/INLS560FinalProject

Reflection:


For my data analysis final project, I wanted to analyze data that was both socially relevant and interesting to me. So since the project
was assigned in the midst of political primary season, I opted to create a data analysis tool that worked with CandidateSummary files 
from the FEC’s official website (www.fec.gov). As you can see from the files in my repo, my program takes CampaignSummary files from 
election years 2008, 2010, 2012, 2014, and 2016. Each .csv file contains campaign finance information on each and every candidate that
registered with the FEC for that election year. Essentially for my program, I created a utility which allowed the user to do basically 
search for a specific candidate, or create a data visualization that allows the user to pick a state, and then display a data 
visualization for the total contributions that went to each candidate for that selected state. With these two functionalities, I 
tailored my program to fulfill one central goal: allow users to find campaign finance statistics for any candidate that registered with 
the FEC for the last five elections cycles (since 2008).

So when a user runs the program, the first choice that the user has is which campaign cycle’s candidates they want to learn about: 2008,
2010, 2012, 2014, or this year’s election, 2016. Each election cycle is associated with the numbers 1 through 5 respectively, so to 
select an election cycle to work with, all the user has to do is type in a number from 1 to 5. Early on in conceptualizing the logic 
for this program, I quickly realized that the more I can do with the least amount of valid inputs the better, because it will make 
capturing bad user input much, much easier. To put it another way, if I were to have let the user type in the name of the csv file, or 
if I were to allowed them to type in the name of the year, there’s a lot that could go wrong. The more I allowed the user to input 
strings, the more I would have to account for spelling, capitalization, and punctuation errors.  Sure it’d be possible to catch and 
account for all those efforts, but I felt like limiting the user’s options to numbers 1 through 5 would make it way easier to catch 
errors (since I only had to check for the numbers 1 through 5) with much less code. So I tried to use this train of thought every time 
I had to code a user interaction.

Once the user selects an election cycle to work with, a second tier of numbered options is presented to the screen: 1. Search a 
Candidate 2. General Candidate Data by State 3. Help 4. Choose Another Year. Again, I minimized the pressure put on the user by
limiting the domain of valid input to the numbers 1 through 4.  

If the user presses 1, they are presented with a prompt to search for a candidate name. This part of the program was tricky to code. 
With all of the candidate names that existed throughout the csv files that I was using, it was obviously impractical to restrict the 
user’s domain of choices to a set of integers. I had one thing going my way however. Throughout all of the spreadsheets, all of the 
names were formatted the same way:DOE, JOHN ADAM.

So as far as capitalization errors go, a simple .upper() on the user’s input would eliminate those. But what about the name order? 
What if in the search of candidate ‘DOE, JOHN ADAM’ a person typed in ‘John Adam Doe’ or just ‘John Doe’.  What if they didn’t know the 
candidate’s full name and just queried ‘John’. I talked about this in past reflections already, but this was definitely a big roadblock
in my program. In retrospect though, I was fortunate to have this problem because it ultimately led me to see the value in the meetups
we had to attend for class. I won’t rehash my second meetup report, but basically the guy who organized the meetup, Aaron Knight, 
helped steer me away from the much, much more complicated solution I was going for (I don’t quite recall what it was exactly, but I 
remember it involved a horrific amount of regex) to a much simpler one. Basically, after I capitalized all of the user’s input, he 
basically suggested splitting the user’s input on any space or comma that the user might include in their query, effectively creating a 
list of name elements. From there, I could loop through each split name element while I looped through each row in my csv file, and if 
the capitalized version of the element appeared in the ‘Candidate Name’ column, then I would add that row to a new dictionary if that 
row hadn’t already been added. Extending off of the above example, if a user types in ‘john adam doe’, by program will split that 
string on the space and capitalize each name element (‘JOHN ADAM DOE’). The program then checks through each row in the csv file, and 
see if any of those three elements appear.

Using this technique, the program will then output a list of all the candidate names that matched the query. From the beginning I 
didn’t want to return just one candidate on the user’s first query. Since there are so many John Doe candidates I wanted to give the 
user the opportunity to see all the John Doe’s that they could possibly be looking for. From there, the program displays each match and 
associates that match with a number. To see the campaign finance statistics for a given candidate, all the user has to do is input the 
number that corresponds to the candidate. Below is an example of the record that pops up when a user selects ‘TRUMP, DONALD J.’:

Candidate name: TRUMP, DONALD J
Type of office: P
Candidate Office State: US
Incumbent/Challenger/Open: OPEN
Candidate Address: 725 FIFTH AVENUE,NEW YORK,NY
Individual Contributions: $9,527,020.19
 Other Committee Contributions: 
 Total Contributions: $9,809,453.45
 
Aside from the ‘search a candidate’ option, I also wanted to provide an option for users who aren’t coming to the program for a 
particular candidate name in mind. This is where the second option ‘General Candidate Data by State’ comes into play. This option allows 
the user to type a two-letter state abbreviation. Then, based off of the two-letter state abbreviation that the user selects, a data 
visualization of the total contributions for each individual candidate in that user-selected state will be generated. Once again, the 
constant formatting of the FEC csv files really helped me out in this task. Since all of the states in the csv files two-letter, 
capitalized state abbreviations, for user validation I simply created a list with every single two-letter state abbreviation that 
appeared in the csv files (one for each state), and checking the user’s input against that list. 

What wasn’t so easy was getting the data visualization to work. My original idea seemed easy enough. For each candidate, print out a
number of asterisks that is proportional to their total contribution dollar amount. Many candidates had hundreds of thousands of dollars’
worth of total contributions, so printing an asterisk for each dollar was an impractical avenue: essentially I would have to divide the 
number I used to multiply the asterisk to make the data visualization readable (ultimately I chose 1,000). Ironically though, the FEC’s 
constant formatting ended up coming back to bite me in respect to this task. Throughout the csv files the values in the ‘Total 
Contributions’ field were presented as strings like this “$100,000”. So in order to get a number to perform any type of mathematical 
calculation I had to change “$100,000” to 100000. This ended up being a problem that actually had a simple solution, but ended up taking
me a long time to code. I knew how to use the .split() method to remove any dollar signs, commas, or decimal points (for cent values), 
but for some reason every time I tried to apply that number to the calculations of my data visualization, nothing would happen. Completely
stuck, I ended up having to take several ‘breaks’ in order to wrap my head around this problem. 

But of course, as has been the case many times throughout this class, the solution I was looking for was laughably simple: essentially 
the reason why it was working was because I was attempting to multiply asterisks (string objects) by floating point numbers (since many 
of the dollar amounts I converted to numbers still retained their cent decimal values) which of course is impossible (you can’t really 
print a third of an asterisk). All I was missing was a simple int() to truncate the decimal places.

From there the last two options (the help screen and the choose another csv file options) were pretty easy to code. 

All in all I am very happy with this project.  Although I didn’t accomplish every single thing I milestoned during the very first 
planning period for this project, I was happy with the way I was able to modify my scope and tailor my program to what I thought would
be most useful to the user as time went on. All in all, I wanted to create a program that I thought was both interesting and useful, 
which is why this is by a country mile the most proud I’ve ever been of any program I’ve done. Despite all the work and frustration, 
coding this project was a great experience, and definitely gives me confidence to tackle any coding project I may face in the future. 
