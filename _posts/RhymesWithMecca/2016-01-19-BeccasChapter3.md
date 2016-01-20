---
layout: post
author: RhymesWithMecca
title: "Becca's Chapter 3 Exercises"
---
Exercise 1:
<iframe src="https://trinket.io/embed/python/dfd6a1276b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Exercise 2:
<iframe src="https://trinket.io/embed/python/fbe7c93635" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Exercise 3:
<iframe src="https://trinket.io/embed/python/d13feb667c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Exercise 1: At first, I had “else int(hours) > 40:” (or something similar), which gave me an error message.  I looked back at the text and realized that the “else” statement stands by itself.  In the process of writing my reflection, I realized that you could put the conditional statements in either order.  “If” could either be “less than or equal to 40 hours” or “greater than 40 hours.”  This was useful - I think the syntax error was helpful to make, since I learned from my mistake.

Exercise 2: I had the formatting a bit off here as well.  I forgot the colons after “try” and “except” and I forgot to indent.  My error messages prompted me to look back at the text and figure out what was causing the error.  I feel like this type of error is fixed only through practice (like this!).

Exercise 3: I declared “score” as an “float” but forgot to keep it as a float in the “if” and “elif” statements.  I had a similar problem in the Chapter 2 exercises - I guess it is counter-intuitive to me that Python won’t remember something you told it already.
At one point, I troubleshooted a bit and added "and float(score) <= 1.0” to the first "if" statement.  I then tested the program with 2.0, and got a grade of B.  It took me a bit to realize I needed the “and" statements for every “elif” statement.
It also took me a bit to realize that I needed (I think) both the “else” statement for a numerical entry that isn’t between 0.0 and 1.0, as well as the “except” statement for an entry that isn’t numerical.  That is, whenever I tried the program without both of those statements, I got an error message.
