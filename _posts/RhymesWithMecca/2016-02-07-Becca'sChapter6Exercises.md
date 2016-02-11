---
layout: post
author: RhymesWithMecca
title: "Becca's Chapter 6 Exercises"
---

Here is 6.1: <iframe src="https://trinket.io/embed/python/021954b0cd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is 6.3: <iframe src="https://trinket.io/embed/python/373e4cafbd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is 6.4: <iframe src="https://trinket.io/embed/python/9d48d3f785" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is 6.5: <iframe src="https://trinket.io/embed/python/0028eb27f3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

General Reflection:
I didn't have code for user input checking because it didn't say we needed to - hope this is okay!

6.1 Reflection:
This one took me a bit.  At one point, I wanted the program to break "if index == " ""/if I'd gotten to the end of the word.  I was getting an index error and got stuck.

Then I went on to Exercise 3 before coming back to this exercise and realizing I had to factor in word length.  I made a negative_len variable for negative length since index was starting at -1/the end of the word and I wanted to print letters until the word was done/we had reached index = negative_len - 1.  This worked.

6.3 Reflection:
Here, I needed a refresher on how functions worked.  I needed to ask the user for input outside of the function and return the function.  

I also had "if let == “let”" for a while, which was returning 0 because I needed to take out the quotation marks for it to return the user input.  I realized this was occurring, and what the program was doing, but couldn't figure out how to fix it for a bit.

Also, printing types part way through is a very helpful troubleshooting method.

6.4 Reflection:
The linked website's notation on str.count was confusing, so I consulted http://www.tutorialspoint.com/python/string_count.htm for further assistance.

I had str.count (I thought this was for a general string), not word.count for a while.  Also, I needed to print word.count, not let!

6.5 Reflection:
I based this on the Stephen Marquard example in the book chapter (commented out in my Trinket).  It wasn't as difficult as the previous ones.  I also printed more things than necessary to ensure that it worked.
