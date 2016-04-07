---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's MOAR Dictionary Exercises"
---

Here is my trinket for Exercise 1:
<iframe src="https://trinket.io/embed/python3/cb1d5f1d5e" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is my trinket for Exercise 2:
<iframe src="https://trinket.io/embed/python3/dbe922337d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

These were some difficult exercises for me to complete.  I used a lot of printing at certain parts of my code so that I could better understand where I was having an issue or calling on an incorrect value.  

This strategy was particularly useful for Exercise 1, since I needed to break down the entire text file into lines and then into words.  Once the list was broken down into words, I discovered that I was easily able to add this to my dictionary and count the number of times each word appeared.  I made this exercise a lot harder than it should have been, since solving the rest of it was very similar to the exercises that we had done previously.  Here is the way that I went through the list I'd created to break down the lines into words:

```
words_table = []
for line in words_lines:
    parts = line.split()
    for part in parts:
      words_table.append(part)
```

Looking back at this code now, it seems so simple, and I wonder why I struggled so much before.

The second exercises were challenging for some and not as challenging for others.  For the first part of Exercise 2, I could not figure out for the longest time why I kept getting an error in my code when it should have been working.  Going back through the text file, I discovered that not all lines that started with "From" had a weekday associated with it.  Because of this, I needed to adapt my "if" statement appropriately.  In the end, it looked like this:

```
if len(day_table) > 3 and line.startswith('From'):
```

Once I'd figured out that, things went a lot smoother.  I didn't encounter any difficulties with the second part of Exercise 2; I just went through it like we had for previous exercises.  For the third part of Exercise 2, I tried a couple things, but wasn't sure what to do.  I consulted this <a href="http://www.pythonlearn.com/html-008/cfbook006.html#maximumloop"> website </a>.  Once I understood the general idea of what this code was supposed to be doing, I went through and applied it to this specific situation.  I discovered that I needed to count the actual value of the item within the dictionary, so I created a count variable to do so.  After this, I was able to adapt the code to fit my needs.  Here is where I created the count variable:

```
count = email_sender[email]
```

The final portion of Exercise 2 was pretty tough too, but it was a good exercise for me to learn how to split a string down further and further using dictionaries alongside it. For these exercises, I consulted <a href="http://stackoverflow.com/questions/1633932/slice-a-string-after-a-certain-phrase"> this </a> and <a href="http://stackoverflow.com/questions/4945548/remove-the-first-character-of-a-string"> this </a> website.  These websites were particularly helpful because they helped me understand how to break down the different parts of a string bit by bit.  There's probably an easier way to do it than I did, but this is what I have for now.  Here is the bulk of my code that extracted the domain of the email address and then added it to the dictionary:

```
    if len(domain_table) > 3 and line.startswith('From'):
      #This is where we go in and slice out the specific section from the email address
      email_address = domain_table[1]
      #Finding the point at @ and beyond
      section_1 = (email_address[email_address.find("@"):])
      #Creating a string that removes @
      section_2 = section_1[1:]
      #Now we evaluate our created string
      if section_2 not in domain_name:
        domain_name[section_2] = 1
      else:
        domain_name[section_2] += 1
```

I still think that I need to continue practicing with dictionaries in order to fully understand them, but these exercises made me somewhat more confident.
