---
layout: post
author: camazotz
title: "Navaneet's Final Project!"
---

Overall, this project made me a lot more comfortable with using and manipulating dictionaries in Python. I completed the functionality I had set originally as a goal, although my methodology for achieving it had to be slightly altered. In particular, my original structure for the dictionaries had to be changed to avoid iterating through dictionary key tuples. I ended up creating more dictionaries to allow efficient access to data.

My milestones:

- [x] Read all data into python lists
- [x] Create a dictionary with each state as key and as value another dictionary with candidate as key and vote as value
- [x] Create a dictionary with each candidate as key and as value another dictionary with state as key and vote as value
- [x] Create a dictionary with each county as key and as value another dictionary with candidate as key and vote as value
- [x] Create a dictionary with each county as key and as value another dictionary with party as key and vote as value
- [x] Create a dictionary with each state as key and as value another dictionary with party as key and vote as value
- [x] Build a user interface for the user to select three modes (state, candidate, and county)
- [x] Have a help option to give the user directions on navigating the app
- [x] Create actual help instructions
- [x] For each mode, allow the user to enter any state, candidate, or county respectively and display the corresponding value(s)
- [x] Allow the user to switch datasets
- [x] Allow the user to enter different column addresses for the fields of data
- [x] Modularize code
- [x] Comment code
- [x] For any query, display the fraction of votes as a bar graph (composed of asterisks) as a function of the votes and the mode that the user has selected (so if the user is in state mode, display the number of votes for each state as a bar graph)

The most time-consuming part was building all of the error checking parts at every step. It also took a little bit of time to modularize the code afterwards because some of my methods had were built in a way that assumed global variables so I had to make sure to look out for while creating separate modules. At one point I ran into an issue with two-way import statements causing an error (meaning two classes importing from one another) so I had to create a separate class that contained the dependencies they needed and had both of them import from it.

Process:

I began working on the project the week it was assigned and started working on the dictionaries because I needed them for all of the other tasks. I had to alter my dictionary design halfway through the project because I realized that the current plan for creating dictionaries would have made it necessary to iterate through the dictionaries for some user queries (which kind of defeats their purpose and doesn't make effective use of them). So I ended up recreating all of the dictionaries. As a result, I had to recreate part of the user interface because it was partway through creating the UI that I realized that my dictionary design was not efficient.

Most of the challenges I ran into were during this initial set-up portion of the project. Creating the dictionaries and making the bar chart for each mode were the most difficult conceptually. The user interface and mode-checking were time-consuming because there were so many parts but it was just a matter of testing to make sure I've covered all of the cases. But the it was not particularly difficult from a coding perspective.

I documented the challenges I ran into and how I resolved them as I went along and I've listed them below:

I tried to use the pandas library to read in data from the election dataset but after reading it into a pandas DataFrame, I could only access data via the columns so it wasn't very useful for forming the dictionaries that I wanted. I ended up reading the data as we did in class through the readLine() method.

While creating the countyDict, I found that some states had the same county names. So for example, Arkansas and Montana may both have a county named 'Autuaga'. As a result, using the county name by itself as a key wasn't sufficient so I made a key consisting of a tuple of the county and state.

After I created the countyDict dictionary, I built the remaining dictionaries by traversing through the already existing dictionaries. I found the method to traverse a dictionary [here](http://stackoverflow.com/questions/4992739/how-to-traverse-through-dict).

My app has three modes so when I was taking user input to enter a number corresponding to a given mode, as part of error checking, I had to check whether the user input was a number before checking which number it was. For this, I used the isinstance(<var>, int) method that I found [here](http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not).

The user can enter a candidate name, a state name, or county name as a query. But if the user does not capitalize the first letter of each word (as in 'Donald Trump' as opposed to 'donald trump'), their query won't be found in the dictionary. To allow more flexibility, I plan to read everything into the dictionaries in lowercase and convert the user's input to lowercase. When printing out statistics, however, I want the first letter of the names to be capitalized. I found a Python method title() to do this [here](http://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python).

When printing out the bar graph of asterisks for the number of votes each candidate has, I didn't want to print out the actual number of votes (since that would mean hundreds of thousands of asterisks). So I decided to scale all the votes between 0 and 10. After doing the multiplication and division necessary for implementing this scaling factor, I had to round the number to an integer. I found the method to do that [here](http://stackoverflow.com/questions/31818050/python-2-7-round-number-to-nearest-integer).

When printing out the asterisks in a loop, I noticed that the print function was automatically inserting a newline at the end. I found a way to disable that by putting end='' on stackoverflow [here](http://stackoverflow.com/questions/12032214/python-3-print-new-output-on-same-line).

In order to get the asterisks to line up when printing in the loop, I used format(string, '<30') to align the string to the left and extend space out for 30 characters. I found that method [here](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch02s13.html).

The input does not take keyword arguments error when trying to have variable name in input call so I added ‘+’ to add string instead of comma and got rid of the ‘sep’ parameter.

To exit the program, I use sys.exit() after importing sys module.

To create fake data, I had to find a way to randomize excel data so I used the method outlined [here](http://answers.microsoft.com/en-us/office/forum/office_2007-excel/how-to-randomize-data-in-excelspreadsheets/399ec67b-a443-e011-9bac-78e7d160ad4e?auth=1).

Retrospective/Looking ahead:

Next time I work on something like this I think I would think a bit more critically about the requirements for the functionality before beginning to code. This would have saved me the time that I spent on redesigning the dictionaries. I would have also begun modularizing the design from the beginning because waiting until the end to modularize would require some tweaking of all of the methods (which assume global variables in a non-modularized design), which would be a pain as the project scales up.

Unfortunately I didn't get a chance to look into using Cloud 9 (I used PyCharm instead) because I got overwhelmed by other project deadlines this week but I think it would be helpful to get comfortable using it so I'll look into it over summer. Now that I'm pretty comfortable using dictionaries and reading from datasets, I think I might tackle some of the challenges on Kaggle and start building my data analysis skills.

As I stated in my project proposal, I feel that a lot of the functions that I had to enable using dictionaries could have probably been acheived a lot more efficiently if I had used a database, so that is the next thing I will look into. My plan is to look into using the MongoDB Python user interface and perhaps trying to replicate the same functionality in this app using the dictionary.

My github repository can be found [here](https://github.com/camazotz/ElectionStats2016.git). The file electionResults.csv is the original file I got from Kaggle. I have included three other fake datasets named fakeData1.csv, fakeData2.csv, and fakeData3.csv respectively.
