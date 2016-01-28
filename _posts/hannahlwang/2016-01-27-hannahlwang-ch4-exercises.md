---
layout: post
author: hannahlwang
title: "Hannah's Chapter 4 Exercises"
---

Exercise 6:

<iframe src="https://trinket.io/embed/python/7ec310b208" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For this exercise, I defined two separate computepay functions (for 40 hours or less and for more than 40 hours). I'm still not positive if this is the simplest way to do it, but because you have to perform an additional operation for overtime, it seemed like the only way to do it. It made sense to do this with functions, because regardless of the input, you want the program to perform the same computepay function, so you only have to write this once. I kept my try/except statements from the last time to deal with bad input.

Exercise 7:

<iframe src="https://trinket.io/embed/python/375e02ce6f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Defining this function was mostly accomplished by replacing my "float(score)" instances with "a". It was interesting that when I had the if/else statement nested inside my function definition, the program could not deal with bad inputs. Moving it outside the if/else and using "float(score)" as the variable instead of "a" worked.
