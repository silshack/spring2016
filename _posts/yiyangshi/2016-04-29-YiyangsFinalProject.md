---
author: yiyangshi
layout: post
title: "Yiyang's Final Project"
---

Here is the program:
https://github.com/yiyangshi/FinalProject

##### IMPORTANT!!! Please do not run it on Cloud9 directly. It takes forever! 

My csv files are around 50MB each. It takes around 17 seconds in PyCharm for my cleaning codes to clean up a whole file. When I ran it in Cloud9, it took 664 seconds. I did not wait for the other functions to run. So, please download all the files and run it locally.

#### Final Project Review:

##### Background
---

As a frequent flyer, I am always interested in learning about flight on-time performance. Specifically, what carriers or airports have the least delays, and what are the delay reasons. I wish there is an App that I can get those information from so that I can pick the “best” carrier or airport to fly with. So, for this data analysis project, I decided to create such tool by myself. 

Fortunately, I am able to obtain detailed flight information from U.S. department of transportation website as csv file. Within the file, each row is a unique flight. On this website, users can customize the variables they want to see. The following are the variables that I chose to form the original dataset for this project: year, month, day of week, flight date, carrier code, origin airport, origin city name, origin state name, destination airport, destination city name, destination state name, crs departure time, departure time, departure delay, crs arrival time, arrival time, arrival delay, carrier delay, weather delay, nas delay, security delay, late aircraft delay. I downloaded complete data for January 2016 and February 2016, which are the most up to date datasets. Each dataset is around 50MB.

An issue with this dataset is that it only provides carrier codes and airport codes to users. To most people, these codes are not very informative. So, I used other sources to download a reference list for carriers and a reference list for airports. I also added location search functionality to the airport codes so that users can easily obtain all the airport codes for a certain area.

When finishing the project, I noticed that I did not use all the variables that I downloaded. I think it reflects a planning issue. I was not completely sure what information I would provide and what data I need to analyze.  For future projects, I would create a complete list of information that I wanted to provide, along with the needed data to provide the information. Then I would not end up with too many un-used data.


##### How did I accomplish my project
---

According to my original plan for the project posted on Github, I vision users to be able to obtain three types of information: the basic statistics on the delay time and reasons for a specific carrier or airport, the carrier ranking based on delay probability, the day of week or airport to avoid in order to avoid uncontrollable delay. Compare to my final project, I have made all these functionalities available. To make the functionalities more clear to users, I ended up breaking these three functionalities into five: carrier ranking by delay percentage, carrier ranking by average delay minutes for a chosen delay reason, rank day of week by average delay minutes, basic statistics for a(n) chosen carrier or airport, delay reason breakdown for a(n) chosen carrier or airport. The calculation of these functionalities will be further explained later in the article. 

As you can tell, the original objectives are very vague. They are not the kind that you can immediately tell how the information is calculated. This caused me a lot of trouble during coding. I stopped several times in the middle to think about what exactly am I calculating here and how should I calculate it. Even now, I still think my wording for the five functionalities are somewhat confusing. I also spent a lot of time thinking about who are my potential users. Because if my potential users are just passengers, they may not be that interested in delay minutes breaking down to each reasons. Airplane companies, on the other hand, would be more interested in such information. As a reflection, I listed out five steps to do before coding next time:

•	Who are the users?

•	What information do they want?

•	Are these calculable with the available data?

•	List out all the functions and the related data used

•	Consider if there are common used functions

In terms of milestones, I’ve accomplished all the milestones except for the stretch goals. One of them is to use turtle to create line graph. I still think this is a cool idea and I want to try it during the summer.

##### Functionalities
---

###### File selection

In main.py, the first chunk of code is file selection. There are two available files: Jan.csv and Feb.csv. Users can also go to U.S. Department of Transportation to download their customized data and run it on the program. However, the variables must be exactly the same as the ones in the available file. I specifically created a choice “9” to print the download instructions. 

The program handles customized time period well. Users can potentially download a year of data and explore it with the program. Users can run the program on different months of a year to compare the differences between different seasons. In the future, I would wish the program to be able to take several files and discover the trends over time.

###### Table cleaning

The second chunk of the code in main.py is table cleaning. When I read the csv file into lines, I noticed that Python automatically added quotes to string values, for example, ‘ “origin airport” ’. So I wrote this piece of code to clean out all the spaces and quotes on the strings. The code reads through each cell, which makes the cleaning process time consuming. The average cleaning time is 17 seconds. To keep users engaged, I added a timer to the cleaning process so that at the end of the cleaning, the program will print out how many seconds is used to clean the file. 

###### Five main functions

1.Carrier rank by delay percentage (with pics)

This functionality prints out the 12 carriers in the rank of the delay rates. To calculate the delay rates, I created two dictionaries, one to store the carrier names as keys and the total number of flights as values, the other to store the carrier names as keys and number of delayed flights as values. While looping through the table, the program reads through each line. It first reads the carrier code, the fourth column, and adds one to the corresponding key in the first dictionary. Then, it determines if this flight is delayed by looking at the arrival delay minutes, -6 column. If delay minute is strictly positive, the program will add one to the corresponding key to the second dictionary. 

The advantage of dictionary is that I do not need to worry if any of the value is zero. So, I can do division directly. I calculated the delay rate by dividing the value in the second dictionary with the value in the first dictionary for each key. This creates another dictionary with carrier names as keys and delay rate as values.

Knowing that dictionary cannot be ordered by value directly, I found a sort function. The sort function can order the values in a dictionary and return the ordered list of keys. Then, I used the list of keys to refer back to the dictionary to find the values and print them out in order. There is also a bar graph included.

The dictionary technique is the main technique that I used through out the five functionalities. The idea is the same and the only difference is the specific values being calculated.

2.Carrier rank by average delay minutes for a chosen delay reason

In this functionality, user first chooses a delay reason to explore. The column number of the chosen delay reason is then passed into a function to calculate the average delay minutes. The average delay minute is calculated using the same dictionaries idea above. The two dictionaries here are: 

•	total_delay_minutes = dict(key  = carrier name, value = total delay minutes)

•	count_delay_minutes = dict(key = carrier name, value = number of delays)

Notice that the delay minutes and the number of delays calculated here are decided by the delay minutes of a specific delay reason. It means that the program is evaluating if a specific column (between -5 and -1) is above zero, not the -6 column.

3.Average delay minutes for different day of week

This functionality is also achieved by the dictionary idea. Here are the two dictionaries:

•	day_total_delay_minutes = dict(key = day of week, value = total delay minutes)

•	day_delay_count = dict(key = day of week, value = number of delays)

Day of week is represented by numeric number in the original dataset. So I created an extra dictionary to map the numbers to the strings so that the print out is more informative.

4.Max, avg, min delay minutes for a(n) chosen Carrier or Airport

This functionality allows users to pass in a carrier code or airport code and calculate the max, avg, min delay minutes for the carrier or airport. The calculations of max, avg, min are pretty standard so I would not elaborate here.

Most of the times, user will not know the carrier code or airport code so I created help functions for users to search for the codes. For the carrier code, since there are only 12 carriers, I just printed out the whole reference list for user. Airport codes are too much to print, so for the airport code, I created a regex search function, which is similar to the Google location search homework we did. User can type in a blurry location and the program will return all the airports with the codes that matches the location user entered. User can then use the airport codes to find out the basic statistics.

5.Explore Delay Reasons for a(n) chosen Carrier or Airport

This is the most complicated piece of code. However, the basic idea is still the dictionary idea. This functionality is more like the combination of all the functionalities above. 

For the specific input, two dictionaries are calculated:

•	input_delay_minutes_by_delay_reason = dict(key = delay reason, value = total delay minutes)

•	input_delay_count_by_delay_reason = dict(key = delay reason, value = number of delays)

Similary, the calculation here are decided by the delay minutes of the specific delay reason. I also created a counter input_total_delay_count to keep track of the total number of delays caused by this specific input. Using the two dictionaries, we can get the average delay time breakdown by delay reasons. Using the second dictionary and the counter, we can get the percentage of delay caused by each delay reasons.

Notice that, all of the calculation is based on the user input. Thus, the results are for a specific carrier or airport. This functionality also allows carrier code and airport code search.
There are several new things that I learned from this project: the timer, the sort function, and the usefulness of dictionary. Honestly, I did not feel completely comfortable with list and dictionary. However, now I feel confident.

Finally, a big thank you to you for this awesome class! I can now use Python to achieve so many things that I couldn’t before.

###### Reference:

http://matplotlib.org

http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

http://stackoverflow.com/questions/17211188/how-to-create-a-timer-on-python
