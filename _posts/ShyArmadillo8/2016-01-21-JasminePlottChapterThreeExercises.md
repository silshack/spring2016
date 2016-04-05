---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Chapter Three Exercises"
---

I knew a little bit about conditional executing before I read this chapter and did the exercises, but for the most part, writing the code for my trinkets for these assignments was pretty exciting.  Many of the mistakes that I made while working through these exercises were due to silly mistakes on my part or not realizing that I should have been more specific in a certain instance.

Starting with the first exercise, I thought that things went pretty smoothly.  The most difficult part for me was figuring out how to make the equations that I was using with the operators as specific as they needed to be.  For instance, I didn't include the float in front of the hour variable I had created for my "if else" statement, so because of this, only the "if" portion of my conditional statement was executing. I also didn't separate the 40 hours from the extra hours that were being multiplied by 1.5, so the  result was that I was getting much higher numbers than I expected. So what I was doing was this:

```
if hour > 40:
    overtime = float(hour) - float(40)
    pay = (float(hour) * float(rate)) + ((float(overtime)*float(rate))*1.5)
    print("Good for you for working overtime! Your gross pay is" + " " + str(pay) + ".\n")
else:
    pay= float(hour) * float(rate)
    print("Looks like it was a typical work week for you.  Your gross pay is" + " " + str(pay)
```
When what I should have been doing was this:

```
if float(hour) > 40:
    overtime = float(hour) - float(40)
    pay = (40 * float(rate)) + ((float(overtime)*float(rate))*1.5)
    print("Good for you for working overtime! Your gross pay is" + " " + str(pay) + ".\n")
else:
    pay= float(hour) * float(rate)
    print("Looks like it was a typical work week for you.  Your gross pay is" + " " + str(pay)
```

Here is my Trinket for the first exercise:
<iframe src="https://trinket.io/embed/python/175155762e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The second exercise went pretty smoothly as well, and I didn't encounter many problems when I was doing this one.  Perhaps I'd learned my lesson from the previous exercise about making sure to append variables with the specific value that I wanted them to have rather than just letting them be variables.  

Here is my Trinket for the second exercise:
<iframe src="https://trinket.io/embed/python/0a2eafe501" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This last exercise was something of a nightmare for me.  I spent a ridiculous amount of time trying to figure it out, but after coming back from a break, I just started my program from scratch and was able to have it done in less than 10 minutes.  I still can't quite believe that it works, since I spent so much time on it, it feels strange that it was able to come together so easily afterwards.  While I'm not 100% certain what I was doing wrong, here are some ideas that I have. My first mistake was using raw_input instead of input.  So it looked like this:

```
scores = raw_input("Please enter a score between 0.0 and 1.0")
```
Instead of this:
```
scores = input("Please enter a score between 0.0 and 1.0")
```

Another problem that I couldn't wrap my mind around was the placement of the try and except statements with the if and else statements. I believe that I made some bad nesting choices, but this is what I found out works the best:

```
try:
  if float(scores) >= 0.9 and float(scores) <= 1.0:
    print("A")
  elif float(scores) >= 0.8 and float(scores) < 0.9:
    print("B")
  elif float(scores) >= 0.7 and float(scores) < 0.8:
    print("C")
  elif float(scores) >= 0.6 and float(scores) < 0.7:
    print("D")
  elif float(scores) <0.6 and float(scores) >= 0.0:
    print ("F")
  elif float(scores) > 1.0 or float(scores) < 0.0:
    print ("Bad Score")
except:
  print("Please start from the beginning, and enter a score between 0.0 and 1.0")
```
  
The other tactics that I'd used would give me results that were definitely not right, even if I had specified exactly what I thought was correct.  Lastly, I also hadn't considered that the scores a letter grade could fall into would be ranges rather than just one number. Ranges are a much more precise way of ensuring that the value you want ends up where you want it to. This example of what I was doing wrong below helps show my well meant, but wrong, idea:

```
 if float(scores) >= 0.9:
    print("A")
  elif float(scores) >= 0.8:
    print("B")
  elif float(scores) >= 0.7:
    print("C")
  elif float(scores) >= 0.6:
    print("D")
  elif float(scores) <0.6:
    print ("F")
  elif float(scores) > 1.0 :
    print ("Bad Score")
  elif float(scores) < 0.0
    print("Bad Score")
```
Here is my Trinket for the final exercise in Chapter 3:
<iframe src="https://trinket.io/embed/python/dd24516461" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

These exercises helped me wrap my mind around conditional statements, and hopefully, I'll continue to improve and get a little fancier with these conditions in time.
