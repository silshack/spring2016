---
author: yiyangshi
layout: post
title: "Yiyang's Treasure Hunt Turtles Exercise"
---

Here is my treasure hunt turtle Tina:
<iframe src="https://trinket.io/embed/python/f61ded18e0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
I think the difficult part of the exercise is to figure out the layers of the "try and except" commands and the conditional commands within the while loop. When thinking natural, people would do "try-except" and then "if...else...". However, not only will the "if..else" be executed regardless of the result of the "try-except", those commands will keep being executed until specific conditions being satisfied. Thus, we need to use "try...if...else...except". In this exercise, there are more layers within the "try and except" commands.

There is still room for improvement for my exercise. When I put a valid number for the x coordinate and then an invalid number for the y coordinate, the system gives an error message and goes back to the beginning to ask for a x coordinate again. In the future, I want the system to accept the x coordinate and only ask for a y coordinate. I think more loops may be needed to accomplish that. 
