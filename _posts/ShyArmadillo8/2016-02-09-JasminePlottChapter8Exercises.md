---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Chapter 8 Exercises"
---

Here is my 8.1 Exercise:
<iframe src="https://trinket.io/embed/python/1acf97e19a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I really liked messing around with this exercise.  There is something so soothing about creating a list and then destroying it.  Here is the function that I used to create my list chopping:

```
def chop(cheeses):
  length = len(cheeses)
  last = length-1
  if cheeses != []:
    del cheeses[0:1]
    del cheeses[last-1:last]
  if cheeses == []:
    print("None. There are no more cheeses in this list.")
```

From my experiences in the Chapter 6 exercises, I realized that I needed to make sure that the ranges I put in my indexes for cheeses needed to be integers.  This is why I created length to account for the length of the cheeses list and then last, which is based on the last item in the list of cheeses.  Once I straightened that out, things got a lot simpler and I just kept chopping until there were no longer any cheeses in the list.

Here is my 8.2 Exercise:
<iframe src="https://trinket.io/embed/python/b7d27fbe3b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This exercise took me longer than it should have I think.  I couldn't figure out how to add the text to the code, since I kept trying to
save it under the same name that we were given under the code.  However, when I changed the name of my file to mytext.txt, it suddenly worked. Why is this?

Now that my program was reading the text again, I played around with it and discovered that if the second(in human brains third) word in 
the list was not a weekday, then it printed that word anyways.  I entered snail, and it entered snail instead of Sat.  To fix this, I made a list of weekdays and set the program so that if it was not a weekday, it would not enter anything for that line.  It looked something like this:

```
weekdays = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]

fhand = open("mytext.txt")
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != "From" : continue
    if words[2] in weekdays[:]:
      print(words[2])
```

I'd ideally like to do something where I could have the program read the entire line and be able to pick out the weekday from this line,
but I wasn't able to figure out how to do that.  Since what I'd found at this point worked, I decided to leave it for now. I'm curious to
figure this out for the future.

Here is my 8.3 Exercise:
<iframe src="https://trinket.io/embed/python/adab0843e2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I was really confused by the wording of this question, since I thought that I had to build on my 8.2 code to adapt it to this situation.
Once I realized that I was supposed to adapt only the code provided in 8.2 I changed my tactics and realized that. 

```
fhand = open("mytext.txt")
count = 0
for line in fhand:
    words = line.split()
    if (len(words) > 0) and (words[0] == 'From'):
      print(words[2])
```

I switched up the code above and made it so that if the if statements were true for those things as a collective whole the code would
continue anyways and produce the expected text.  It'll be interesting for the future to try to combine the 8.2 and 8.3 into one cohesive
exercise so that it is guarded and less lengthy.
