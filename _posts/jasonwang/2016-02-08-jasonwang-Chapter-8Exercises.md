---
layout: post
author: wagerpascal
title: "Jason's Chapter 8 Exercises"
---

Exercise 1:
<iframe src="https://trinket.io/embed/python/fe147cea08" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I wasn't sure if it was a list of strings or numbers, so I decided to go with numbers. However, I realized that raw_input outputted a list of strings. This problem was solved by using the map() function, which applies int to every possible independent iterable argument in the function.
In order to split it up, I used a split() function. The suggestion was taken from http://stackoverflow.com/questions/4663306/how-can-i-get-a-list-as-input-from-the-user-in-python . 
From this point, it was only a matter of realizing that taking the length of the list was a good indicator of where the second-to-last indice was, and for isolating it.

Exercise 2:
<iframe src="https://trinket.io/embed/python/5b8be3ca29" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

First, I wanted to mention that it was rather confusing what the mbox-short.txt file was or where it originated, but I eventually found it out. Also, hyphens don't work as a title for text files, apparently.
In order for the file to work, only two changes were required: the inclusion of a days (with shortened names as of the email's format) list, as well as specifically including the list into the comaparison line (line 13).
From this point, all of the days that appear in the emails are displayed line-by-line. 

Exercise 3:
<iframe src="https://trinket.io/embed/python/12b6e971d5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

At first I thought that we were required to alter the original lines from exercise 2, but an error occurred that I was unable to resolve. However, I realized that since the the words[0] != 'From' line is searching for "From", it can be replaced with words[0] == "From". 
From this change, the 'and" operator error was resolved, and the code had the same results as exercise 2.
