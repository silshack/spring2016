---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Chapter 4 Exercises"
---

This exercise really helped me get the hang of functions!  The biggest obstacle for me was (as usual) trying to figure out where to put 
the try and except statements. and using these within the context of the function.  After I figured out that I needed to nest everything 
that I wanted to underneath the try part and then add the except at the end, the program went a lot smoother.  I also had to work through
indenting what I was using so that it didn't fall under the function and could allow the function to execute.  In the end, it looked a
little something like this:

```
try:
  #Setting up the function
  def computepay(hour, rate):
    #For overtime equation
    if hour > 40:
      overtime = float(hour) - 40
      pay = (40 * float(rate)) + ((float(overtime)*float(rate))*1.5)
      return pay
    #For not overtime equation
    else:
      pay= float(hour) * float(rate)
      return pay
  #Putting the function into effect
  calculated_pay= computepay(hour, rate)
  #The response for overtime
  if float(hour) > 40:
    print("Good for you for working overtime! Your gross pay is" + " " + str(calculated_pay) + ".\n")
  #The response for not overtime
  else:
    print("Looks like it was a typical week for you. Your gross pay is" + " " + str(calculated_pay) + ".\n")
```

Here is my completed Chapter 4 Exercise 6 Trinket:
<iframe src="https://trinket.io/embed/python/90f39e9f35" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The second exercise that we had to do for this chapter was challenging in the fact that I had to figure out how to account for both the 
float aspect of score and string aspect of score that I wanted to print out.  I discovered that this was easily fixed by creating a new
variable to account for the string aspect and I could continue to use the other variable for floating.  This resulted in score and 
score_string.  To better express this idea, here is the code I saw below:

```
score = input("Please enter a score between 0.0 and 1.0")
score_string = str(score)
```

When I put the code together in the function, it allowed both of the variables to build off of each other.  It looked a little something like
this:

```
  def computegrade(score):
    if float(score_string) >= 0.9 and float(score_string) <= 1.0:
      print("A") 
    elif float(score_string) >= 0.8 and float(score_string) < 0.9:
      print("B")
    elif float(score_string) >= 0.7 and float(score_string) < 0.8:
      print("C")
    elif float(score_string) >= 0.6 and float(score_string) < 0.7:
      print("D")
    elif float(score_string) <0.6 and float(score_string) >= 0.0:
      print ("F")
    elif float(score_string) > 1.0 and float(score_string) < 0.0:
      print ("Bad Score")
    
  your_grade = computegrade(score)
```

Here is my completed Trinket for the Chapter 4 Exercise 7 format:
<iframe src="https://trinket.io/embed/python/553c3ae3d6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
