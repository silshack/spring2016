---
layout: post
author: payalpn
title: "Payal's Final Project"
---

**Link to my program:**

https://github.com/payalpn/inls560finalproject 

**Reflection:**

For my final project I chose the data analysis project.  I chose the data analysis project over the turtle game app project because I wanted to challenge myself.  Originally, I wasn’t sure which project to choose; however, after some consideration I decided on the data analysis project.  Before starting the final I knew I was more comfortable and familiar with working with turtle.  I knew that my choosing the data analysis project I would get to work more with the material we covered in the second half of the semester; the material I wasn’t entirely comfortable with, especially in comparison with turtle.  

Once, I had decided on creating a data analysis program I needed to decide what data I would analyze.  I decided I wanted to create a program that could analyze membership information for any extra-curricular organization/club.  Organization and clubs such as TriPython or GirlDevelopIt.  I got this idea while collecting membership information for an organization I am currently in on campus.  I was looking at our membership information and seeing how many people were in each major and each year.  Looking at that information was interesting to me so that’s how I decided to analyze organizations’ membership information.  

I generated mock data for this program using Mockaroo.  I created and included three data files, all containing randomly generated data, with my program.  The user has the ability to choose one of the three data files given or upload a data file of their own.  My mock data for each member contains the following information: member ID, username, SSN, first name, last name, gender, race, email, company name, job title, street address, state, date joined, and salary.   While working with my data I realized that I could analyze it in several different ways and that I could create a numerous amount of options.  My program has six different options the user can select from (a total of 7 if you include the ability to go back to the main menu).  I limited it to six because I realized that if I added any more options the user could become overwhelmed if displayed with a long list of options to pick from.  

The options I created range in complexity from low to high.  Some of the options I created simply display a table of information when that option is picked by the user.  Other options I created require the user to input what they are searching for.  I thought this variation in option styles allowed the user to visualize the data from unique viewpoints.  Also, by creating different types of options I was able to challenge myself and gain practice with several concepts we learned in class.  For one of my options I decided to create additional options for the user to pick from after selecting that option.  I did this for the “Average Salary Calculator” option.  I decided to give the user three options—total average salary, average salary by gender, and average salary based on position searched by the user.  Creating this option took quite a bit of my time, but it was something I wanted to do because I realized that there were several different ways to analyze the average salaries for an organization.  

I didn’t come up with all of my options before starting work on my program.  I came up with a couple of options at a time and then would take turns working on each of them.  Whenever I got an idea for another option I wanted to create I would start on it.  Some of my ideas for options started out simple and then became more complex as I continued to work on them.  (The “Average Salary Calculator” is one such example of this.)  This experience has shown me that it is good to have some ideas planned out; however, it is also important to be flexible with your ideas and be open to changes in your initial plans.  Several of my initial plans changed after I began working more on my program.  For example, initially, I was going to try to create a vertical histogram.  I ended up not doing the vertical histogram because of the data I wanted to display using a data printout.  The categories I used for my visual data printouts either had very long category names, a high number count for several of the categories, or both.  I didn’t think this would create a nice, clean visual, so I decided not to pursue this further.  

While working on and engaging with this program I noticed that it was hard to distinguish between the output of each function, the main menu, and the options menu.  I realized that this wasn’t a good user interface design.  It was easy for users to become confused by what they were looking at.  In order to deal with this problem I decided to find a way to format the font.  I found two websites (http://www.siafoo.net/snippet/88 and https://pypi.python.org/pypi/colorama) that helped me figure out a way to format the various outputs from my program.  These websites helped me learn how to change the font color of print statements and string variables.  By changing the font color (and by using different font colors) for my program’s output, I was able to make my program easier to read and more visually appealing to look at.  I tried to be consistent with the font color I choose for certain things, so it wouldn’t be a random color for each output.  For example, I used the red color font for the help text and for whenever the user’s input yields no results.  I used green for the menu and option choices that the user should press for that action to happen. (So letters and number for the main menu and options menu were written in a dark green while their descriptions remained in black.)  I also used blue font for instructions and a dark black font for whenever the user needed to input something into the system.  Changing the font colors and deciding what font colors to use took a lot longer than I had originally anticipated it taking.  Even though changing the font color took a long time, I would go back and do it again if I had to recreate this program.  The reason for that is because I noticed a huge difference by changing the font color.  I think it helped improve the user interface and design of the program.  

Other things I did in terms of output designs was to format my results.  When I was first creating my options I didn’t think about how I would need to format my results; however, after running through my program the first couple of times I realized that I couldn’t just print out a dictionary or a list as a result of an option.  That would be very confusing to users with little programming experience and it also made my output messy and hard to read.  As I mentioned earlier, for a couple of my options I created tables to combat this issue.  Another strategy I used was creating customized print statements explaining what the value from the variable stood for.  This strategy was very important in my “Average Salary Calculator” option in which I had calculated different average salaries that needed to be clearly label in the output of the function.  

There were several times when I hit a roadblock while working on this program.  Talking with my group members helped and taking a break every once in a while helped too.  One challenge I faced was trying to move my functions to different modules.  This is something I have found challenging since the beginning of the semester and with our game apps.  With this data analysis project, I think I have efficient reduce the amount of code in my main module, only leaving the absolutely necessary code in there.  Another challenge I faced was figuring out how to take multiple inputs from a user.  In my program, with option seven, the user can enter as many domain names as they would like to compare in a horizontal histogram.  I decided to use the .split method to separate the different domains entered by the user.  I also printed out an example before the user entered anything, so they could see how they should format their information.  I’m not sure if this is the most effective way, but it does work the way I wanted it to.  Originally, I was trying to create a for loop that would create a new variable for each input the user wanted depending on the number they entered in for a different input function.  This way didn’t work out and it wasn’t very feasible. 

Each time I overcame a challenge I would feel satisfied knowing that I was able to solve the problem at hand.  I think it was good that I picked the data analysis project over the turtle project, because I was able to gain experience with data analysis tools.  I definitely think my knowledge and comfort level with this material is a lot stronger than it was before taking on the data analysis project


**Milestones from last class:**


 
 Milestones I will work on next:
 
 - [x] deal with user error 

 - [x] help text --accessible throughout program 

 - [x] comment code 

 - [x] runs without errors 

 - [x] format results from each option  --well, halfway (I did this for a couple of options, haven't finished for all.) 

 - [x] clean up code--create different modules for option functions and fileSelection function
 
 - [x] add more user-friendly text in each option function 
 

Stretch Milestones:

 - [x] format text/results for each option 
 
 - [ ] create at least one visual data text printout that is a vertical histogram --*reason for not doing this mentioned in reflection

 - [ ] compare data from two different csv files at the same time 



