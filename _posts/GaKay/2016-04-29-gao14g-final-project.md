---
layout: post
author: gao14g
title: "Ga Kay's Final Project"
---

## My GitHub Repository: 

https://github.com/gao14g/INLS560DataAnalysisProject

## My Milestones:

- [x] include at at least two of the four data sets
- [x] have a text-based interface
- [x] have a "help" function that the user can access by typing "/help" (or something similar to that)
- [x] allow the user to keep searching for information until they want to exit the program
- [x] visualize at least two to three of the text printouts
- [x] include an introduction message for the user
- [x] use try and except to handle bad input
- [x] allow users to search for specific items and specific statistics about each item
- [x] include at least one custom module, one dictionary, and one function
  - [x] create a dictionary of dictionaries for each item in the file
  - [x] create a function that allows the user to exit the program
- [x] import the tsv files
- [x] read through each data file
- [x] have the layout of my options menu 
  - [x] include at least three to four options all with descriptive titles
  - [x] create functions for at least one to two of the options
- [x] have the help function print tips and more instructions for the user
- [x] format the printouts so that it doesn't just print the dictionary
- [x] fully complete at least one of the functionalities for the options
- [x] fully finish all options within option 2
- [x] start adding functionality for option 1
- [x] start visualizing certain printouts
- [x] fully account of user error
- [x] make sure my program runs smoothly
- [x] finish option 1
- [x] allow users to search through any type of data set
- [x] reorganize code within the modules (potentially make another module instead of having all my code in one module)

## Stretch Goals:

- [x] include all four data sets
- [ ] include additional data set about cheapest item locations
- [ ] integrate Eve Online's Crest API to pull more data
- [ ] allow visualization for all text printouts
- [ ] order the data within the dictionary of dictionaries

## Project Reflection

For my final project, I decided to tackle the data analysis project. At first, I did not know whether or not I should use Cloud9 or Trinket. Since we had used Trinket so much in our class before, I decided to try to figure out how to use Cloud9. At first, I was a little lost in how to navigate/use Cloud9, but the interface made it very simple and easy to learn. By using Cloud9, I feel like my Git skills have improved. There are still a lot of Git commands that I did not have to use for this project, but I have a good foundation on how it works and how to use it with GitHub. 

After I determined that I was going to use Cloud9, I had to think about what data sets I was going to use. I looked up different csv files online but nothing really popped out to me. I later remembered that one of my friends sent me an excel file of game data from Eve Online. I decided to use this data. At first, I was going to import this file as a csv file, but I realized that the numbers in the data had commas in it so I decided to import it as a tsv file so I would not have to worry about removing the commas throughout the data. I initially had a stretch goal be to use all four data sets. I was originally going to only use two of the data sets, but then I realized that the structure of all four data sets were very similar so it was very simple for me to use all four data sets. When I first tested my data in Cloud9, I noticed that there were multiple random blank spaces at the end of every row. I decided to clean up my data by deleting these random blank spaces from the data set before building my dictionary of dictionaries for my data. I initially thought that building the dictionary for my project would be difficult because dictionaries were such a new concept to me. Surprisingly, I did not have as hard of a time as I thought I would. I took Elliott’s advice he said in class and built the dictionary prior to any other functionalities of my project. All my functions had to do was to just pull from the initially-built dictionary, which I believe made my project a lot easier to manage.

After I had my dictionaries built, I had to tackle the hard part: All the functionalities of my project. I started with an initial list of options I wanted the user to be able to choose from. From this main list of options, I added more options within the first set. Many of these options allowed the user to do the same thing, so I utilized functions to avoid having to repeat a lot of code in my project. When I look back on my project, I had a lot of functions. I realized how useful functions are and how much easier writing code can be with functions. Most of my options were not too hard to figure out, but I did have issues with an option that allowed users to input their own column names. The problem was trying to account for user error. Because the keys are made in a very specific way in the dictionary, it looks for the correct spelling and capitalization when extracting the data. I could not figure out a good way to make this part account for more user variability, so I instead gave more instructions to the user on how they should input the column names. Another option I had a lot of trouble with was the option to allow users to import their own data file. I had no problems building a dictionary from a user input. The problem I had was allowing all my functions to work with a new data set since my functions were catered specifically to the four data sets I used. The error I kept on running into was that my dictionary was never defined, meaning that the variable was not being passed into a certain module I created. I tried to figure out how to fix this error with the help of Elliott. I ended finding a solution to the problem, but it did involve a lot of repeat code. I ended up creating a huge function called option5. Within this function, I basically have all of the code from the options module but for each function, I added code to make it work with the new user imported file. This was a very roundabout way to fix it, but I am glad I was able to get this problem fixed. Another smaller problem I ran into was accounting for user error. I use a combination of try and excepts and additional if statements in my code. I decided to use an additional if statement to capture user error because I ran into problems where the try and except was not working how I wanted it to. In order to capture user error, I first had an else statement that would print an error statement if the user did not put anything that matched the options. With the else statement, I ran into an issue where it would work sometimes and other times it would not work (or it would print an error statement even if the user inputted the correct thing). To fix this, I defined a list containing all the options that were okay for the user to input. Then, I had an additional if statement that said if the user input was not in the list to print an error message. From the testing I did on my code, this seemed to work in capturing user error. I also ran into a small problem with my visual printouts. For my printouts, I print out the number of items based on where they fit within a range of numbers. At first, I had each * represent one item, but a lot of times, hundreds of items would fit in the range and the *s would print onto a new line which looked very messy. I originally tried to divide the number using /, but I would keep getting random errors. I knew the issue was most likely coming from the fact that some of the numbers had decimals but I could not figure out how to fix it. With the help of a classmate, I was able to figure it out. Instead of using /, I had to use //. Talking with my groupmates each class period really helped smooth out any small bugs I could not figure out how to fix myself.

Overall, I was surprised at how much I was able to get done in just two weeks. I feel like I had a good process for working on this data analysis project. When this project was first assigned, I felt overloaded with things I would have to do with this project. The in-class milestones exercises really helped ease the stress of the project. It helped me know what I needed to specifically work on before next class. My overall process for working on this project was to spend a little time each day working on it. The entire time this project was assigned, I do not think I worked on this project more than an hour each day. Every day, I would spend a little bit of time and try to complete one or two milestones. Breaking down the time spent working on a project into smaller time periods really helped relieve some of the stress for me. A lot of times, it can be really frustrating when your code does not work. Whenever I hit major roadblocks, I would step away from my project for a couple of hours. It really helped to clear my mind and eventually, I was able to figure out how to get around the roadblock. I did not have enough time to really tackle my stretch goals, but I might continue working on this project after this class to see if I can achieve some of those stretch goals.

After finished this data analysis project, I can truly see how much I have learned throughout this class. When looking back at some of my first trinkets, it is amazing to see that I have come from a few lines of simple code to a full data analysis project. It amazes me that I started this project with an entirely blank canvas and ended up with multiple modules, some with hundreds of lines of code. I definitely plan on continuing to use programs such as Trinket, Cloud9, and GitHub. I have touched on GitHub before in a previous class, but I feel much more comfortable using GitHub after this class. I know that programming takes a lot of constant practice, and I definitely do not want to lose all of the skills I have learned in this class. Over the summer, I think I might try to build another game through Trinket. When deciding on what our final project should be, I was torn between a game and a data analysis project. Since I chose the data analysis project, I plan on messing around with Trinket and seeing what game I can build now that I have had a full semester of programming. Overall, I have thoroughly enjoyed this class, and I am glad to see how far I have come over the semester.
