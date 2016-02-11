---
layout: post
author: jamesma560
title: "James' Loop Exercises"
---

Loop exercise 1:

<iframe src="https://trinket.io/embed/python/dd03c03880" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Loop exercise 2:

<iframe src="https://trinket.io/embed/python/57aa16c429" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Reflection:

I thought the first exercise was pretty easy. Not much to say about it. The second one gave me some trouble though. With the try/except 
stipulation, coupled with the fact that I chose to use if statements to check to see if the user's input was the max or min value, keeping
the indentation on the up and up was difficult. Another funny thing I noticed is that when I first ran my program, I kept getting 0's
for the maximum and minimum values. And this bugged me for the longest time because I was FOR SURE that it wasn't the indentation. But for 
some random reason in the midst of my frustration, I realized that I had written the max and min assignment statements backwards. The reason why
I was getting 0's was because I had 'user_choice = maximum' as the assignment instead of 'maximum = user_choice". It was a silly mistake, but
it was definitely an educational one. Finally, the biggest problem I had was figuring how to initialize the max and min values. At first, I 
set them both to None, but during my first iterations of running my program, I would always end up None as my minimum value whenever I would input
positive numbers. In hindsight, I deduced that this was because None was stil less than any positive numbers. Once I figured this out,
I realized that I had to set both numbers to the user's first inputted value, so I could have something to compare the user's subsequent
variables. That lead to the additional if statement on line 26 where I say as long as maximum = None (which it definitely would on the first
iteration since that's what I initialized it to), then just set both maximum and minimum to the user's first inputted number. Once I did that, 
I started to get correct max and min values. 
