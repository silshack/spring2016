---
layout: post
author: jamesma560
title: "James Moore Chapter Four Exercises"
---

Exercise 6:

<iframe src="https://trinket.io/embed/python/702ec75765" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 7:

<iframe src="https://trinket.io/embed/python/e83c028c7c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

I felt like these exercises were pretty simple and straightforward. Basically all we had to do was add a couple lines of code to 
define and execute the functions described in the instructions. But despite the simplicity of the exercises, they actually helped me 
identify a major computation error in a prior iteration of my overtime wage program. In the first version of my overtime wage program, I had 
used this forumal to compute the overtime pay: pay = (hours * rate) + ((hours-40) * (rate * overtime_rate)). But as you can see,
and as I realized as this assignment forced me to look over the code again, this formula is wrong, because the first operand "hours * rate" 
ends up multiplying every hour by the regular rate, including the overtime ones, giving me an inflated result. So to fix this, I changed
the formula to read: pay = 40 * rate ((hours-40) * (rate * overtime_rate)) so only hours 1-40 get multiplied by the regular rate. I hope the 
exercises in the future continue to build upon prior exercises.
