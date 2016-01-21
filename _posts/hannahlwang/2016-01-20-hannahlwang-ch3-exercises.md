---
layout: post
author: hannahlwang
title: "Hannah's Chapter 3 Exercises"
---

I definitely had some frustrating moments with this first exercise! It turns out that they mostly stemmed from the same kind of variable mistakes I was making in the last assignment, not from the new concept of conditionals. At first, I had:
```
if hours <= 40 :
  pay = int(hours) * float(rate)
```
Which obviously is missing a variable type assignment for hours. I was also a little slow to realize that I could use a statement like "pay = int(hours) * float(rate)" inside a conditional, since the chapter only used "print" statements. I also had to remember good ol' PEMDAS to get the second calculation working.

Exercise 1:
<iframe src="https://trinket.io/embed/python/61c4af4016" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The second exercise required the use of nested conditionals. In this case, you needed to use a nested pair of "try/except." At first, I had this:
```
hours = input('Enter Hours:')
int(hours)
rate = input('Enter Rate:')
try:
  if int(hours) <= 40 :
    pay = int(hours) * float(rate)
  elif int(hours) > 40 :
    pay = 40 * float(rate) + (int(hours) - 40) * float(rate) * 1.5
  print('Pay: ' + str(pay))
except:
  print('Error, please enter numeric input')
```
This worked ok if you entered an invalid input for rate, but you just got one of those ugly errors if you entered an invalid input for hours. Then I realized that I somehow had to first check if the input for "hours" was an integer. 

Exercise 2:
<iframe src="https://trinket.io/embed/python/2b8c91119b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 3 was more tedious than challenging. I realized pretty quickly that I would have to use the logical operator "and". After that, it was just a matter of entering all of the different conditions for each grade range.

Exercise 3:
<iframe src="https://trinket.io/embed/python/360a863dcf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
