---
layout: post
author: wagerpascal
title: "Jason's Exercise 2 Problems"
---

Take a look:
<iframe src="https://trinket.io/embed/python/2c801f4cf8" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

And here's the code:
```
#Exercise Two Problems
# Jason Wang

#I believe exercises 1 and 4 were more experimental than actual problems, so I have not included it.

#Exercise 2

username= raw_input("Enter your name:")
print("Hello " + username)

#Exercise 3

employhours= float(raw_input("Enter your hours:"))
payrate = float(raw_input("Enter your rate:"))
employpay= employhours*payrate
employpayfinal= round(employpay, 2)
print("Pay: " + str(employpayfinal))

#Exercise 5

celsiustemp = float(raw_input("What's the temperature in Celsius?:"))
fahrentemp_1 = (celsiustemp*(9/5)) + 32
fahrentemp = round(fahrentemp_1, 3)
print("It is " + str(fahrentemp) + " degrees Fahrenheit.")

```

Thoughts:

Overall, I learned some interesting stuff about the properties of int and float types, and concatenation behavior. 

I had a bit of a mixup with integers (int) and floating points (float) initially. This led to some errors when I was trying to round the values due to disagreements between the datatypes, i.e. float() doesn't work with integers, and integers and floats don't work together. Mildly frustrating when I figured that out.
Also, I forgot that you need to convert the numbers into strings before you can concatenate them into the print functions. Nothing serious, but just for readability.
Guess the lightbulbs are slowly warming up. Unfortunately, I believe that most of the variable properties and procedure were learned during the turtle hacking project- but there were still things to learn here.

Finally, for the reading- exercise 4 has an operator for exponents called "\*". Does that still apply to python? I could only find documentation for "**" instead.
