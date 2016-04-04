---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Chapter 2 Exercises"
---
Overall, these exercises went smoothly, and there was only one major setback I encountered but was able to work through in the end.

The first exercise was fairly straightforward and I got that pretty quickly. I discovered that unless you indicated it in your code, you
would not have spaces between your words.  To solve this, I place a " " between the output in my print code.  My code looked like this:
```
#Ask the user for their name
name = input("What is your name?\n")

#Welcome the user
print("Welcome" + " " + name + "!")
```
Here is my completed trinket for exercise 2:
<iframe src="https://trinket.io/embed/python/172319618b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The second exercise was the one that gave me the most trouble, but I was able to work through it fairly quickly.  The biggest problem that
encountered was calculating the pay, and I couldn't understand why I kept getting an error, since my equation was correct.  I went back
through the Chapter 2 notes and discovered that it was because I had not specified a type for the values that were used in the equation.
To demonstrate things a little more clearly, my code looked something like this:

```
#Ask how many hours the user has worked
hour = input("How many hours have you worked?\n")

#Ask what their hourly rate of pay is
rate = input("What is your hourly pay rate?\n")

#The equation to calculate their gross pay is below...
pay = hour * rate
print("According to your responses, your gross pay is" + " " + pay + ".\n")
```

When it should have looked like this (this is the actual code that I used in my final trinket)

```
#Ask how many hours the user has worked
hour = input("How many hours have you worked?\n")

#Ask what  their hourly rate of pay is
rate = input("What is your hourly pay rate?\n")

#The equation to calculate their gross pay is below...
pay = float(hour) * float(rate)
print("According to your responses, your gross pay is" + " " + str(pay) + ".\n")
```

After working through this dilemma, I discovered that I need to be specific as to what I want my program to do. Here is my
completed trinket for exercise 3:
<iframe src="https://trinket.io/embed/python/9031eae42d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Lastly, the third exercise was not as bad as I expected either, especially since I figured out that I needed to indicate the type for
each of the values that I was going to use in an equation.  Below is the code that I used to come up with the conversion:

```
#Time to ask for the temperature.  Letting the user know what we're doing.
print("Let's figure out what the temperature is today.")

#Ask what the temperature is in degrees Celsius
celsius = input("What is the temperature in degrees Celsius?\n")

#This is the equation to convert the temperature from Celsius to Fahrenheit
fahrenheit = float(celsius) * 1.8 + 32

#This prints out the temperature in degrees Fahrenheit
print("According to your answer, the temperature you entered in degrees Celsius is" + " "
+ str(fahrenheit) + "°" + " " + "Fahrenheit" + ".")
```

I did compare my conversion table to Google's temperature conversion method, and I thought that it was interesting how there was a button available to click to allow the conversion to happen after entering in the temperature.  The two methods appear fairly similar, but I'm curious whether we'll learn how to create buttons and drop down menus with Python for the rest of the semester.

Here is my completed trinket for exercise 5:
<iframe src="https://trinket.io/embed/python/49b36ede91" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
