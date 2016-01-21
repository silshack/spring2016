---
format: post
author: ericabrody
title: "Erica's Chapter 3 Exercises"
---
Here is the first program that increases the pay to 1.5 times the pay rate:
<iframe src="https://trinket.io/embed/python/5df8837e8e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is the second program that provides an error message if the user enters a non-numeric string:
<iframe src="https://trinket.io/embed/python/ee9d1b1517" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is the third program that generates grades based on scores entered or an error message if the user 
enters a number outside the range of 0 to 1.0 or enters a string:
<iframe src="https://trinket.io/embed/python/fbce5a9c7b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
The first two programs went very smoothly based on my reading of the text. The last program seemed to work quickly, but then I realized
that it did not meet all the conditions. I foolishly troubleshooted this for about an hour straight, googling the syntax for 
how to determine if an input is a string or a number. I tried nesting all conditional statements, but that didn't work because 
input comes in as a string. so i knew that i needed a try -- except to deal with string inputs and then tried nesting the if's and 
elif's under the try - but I think, ultimately, the errors were caused by misaligned indentations, though some of the errors said 
different problems, which I can't remember now. I changed the error messages to be specific to the different errors (i.e., score must be under
1.0 and error, please enter a number) to help me trouble shoot the errors.
