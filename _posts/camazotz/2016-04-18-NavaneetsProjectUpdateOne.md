---
layout: post
author: camazotz
title: "Navaneet's Project Update One!"
---

Progress:

I tried to use the pandas library to read in data from the election dataset but after reading it into a pandas DataFrame, I could only access data via the columns so it wasn't very useful for forming the dictionaries that I wanted. I ended up reading the data as we did in class through the readLine() method.

While creating the countyDict, I found that some states had the same county names. So for example, Arkansas and Montana may both have a county named 'Autuaga'. As a result, using the county name by itself as a key wasn't sufficient so I made a key consisting of a tuple of the county and state.

After I created the countyDict dictionary, I built the remaining dictionaries by traversing through the already existing dictionaries. I found the method to traverse a dictionary [here](http://stackoverflow.com/questions/4992739/how-to-traverse-through-dict).

My app has three modes so when I was taking user input to enter a number corresponding to a given mode, as part of error checking, I had to check whether the user input was a number before checking which number it was. For this, I used the isinstance(<var>, int) method that I found [here](http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not).

The user can enter a candidate name, a state name, or county name as a query. But if the user does not capitalize the first letter of each word (as in 'Donald Trump' as opposed to 'donald trump'), their query won't be found in the dictionary. To allow more flexibility, I plan to read everything into the dictionaries in lowercase and convert the user's input to lowercase. When printing out statistics, however, I want the first letter of the names to be capitalized. I found a Python method title() to do this [here](http://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python).

When printing out the bar graph of asterisks for the number of votes each candidate has, I didn't want to print out the actual number of votes (since that would mean hundreds of thousands of asterisks). So I decided to scale all the votes between 0 and 10. After doing the multiplication and division necessary for implementing this scaling factor, I had to round the number to an integer. I found the method to do that [here](http://stackoverflow.com/questions/31818050/python-2-7-round-number-to-nearest-integer).

When printing out the asterisks in a loop, I noticed that the print function was automatically inserting a newline at the end. I found a way to disable that by putting end='' on stackoverflow [here](http://stackoverflow.com/questions/12032214/python-3-print-new-output-on-same-line).

In order to get the asterisks to line up when printing in the loop, I used format(string, '<30') to align the string to the left and extend space out for 30 characters. I found that method [here](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch02s13.html).

My completed milestones are as follows:

- [x] Read all data into python lists
- [x] Create a dictionary with each state as key and a candidate-party-vote tuple as value
- [x] Create a dictionary with each candidate as key and a party-vote tuple as value
- [x] Create a dictionary with each county as key and a state-party-candidate-vote tuple as value
- [ ] Build a user interface for the user to select three modes (state, candidate, and county)
- [ ] Have a help option to give the user directions on navigating the app
- [ ] For each mode, allow the user to enter any state, candidate, or county respectively and display the corresponding value tuple
- [ ] Allow the user to switch datasets
- [x] For any query, display the fraction of votes as a bar graph (composed of asterisks) as a function of the votes and the mode that the user has selected (so if the user is in state mode, display the number of votes for each state as a bar graph)

I am still building the user interface for each mode along with error checking.
