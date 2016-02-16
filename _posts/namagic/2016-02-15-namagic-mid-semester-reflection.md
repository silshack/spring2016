---
author: namagic
layout: post
title: "Omar's Mid-Semester Reflection"
---

<h1>Introduction</h1>
I came into this course with a limited understanding of Python. Last semester I was in a Python course which I eventually dropped to lessen my heavy course-load. That course had fewer assignments and did not employ the use of flipped-classroom model. I believe that led to my greater frustration with Python in that course because I was not working in it regularly. Generally, debugging has been the consistent theme of my Python journey so far.

Before I get into my frustrations though, I must say I feel like I have learned an extraordinary amount of Python very quickly. From loops to lists, I am beginning to see how what I am learning are the building blocks towards creating more substantial programs. My housemate and I, neither of us great at programming, want to build an app together in the near future. We are not sure yet what it will be, but understanding the logic behind Python has spurred additional ideas about what we could or cannot do.

<h2>Debugging</h2>
My largest frustrations and joy have to do with debugging. When coding, I’d make several changes at a time not fully understanding their impact and then running the code. I realized that this was a relatively poor approach to coding for me because I do not get an opportunity to see smaller pieces of code in action. However, throughout this course thus far I have become much more comfortable coding via Python. I still spend a good bit of time looking things up; however, I believe this is more habit than it is necessary. Even when I know the code, I still double-check. 

Also within frustrations with debugging, attempting to figure out why certain lines of code of work make a visible change while others do not. For example, in the following trinket I was trying to find the min and max of user input. However, I was using min and max built-in functions that require items to be in a list. This I did not know and did not carefully read through Python’s Library to realize that those functions require a list.

<h3>Ch 5 Loops Exercise 2</h3>

<iframe src="https://trinket.io/embed/python/1ec3c4048e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In another example of frustration, sometimes my programs run the way they should but then I still end up with an error. To debug this, I inserted a print statement prior to line 24 but still ended up with the same error: “IndexErrror: string index out of range on line 23.” 

<h3>Strings! Ex 1</h3>

<iframe src="https://trinket.io/embed/python/108e380cff" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Looking back at this code however, I realized I erred in my own logic. Initially, I set a variable “index” equal to 0. I set another variable “backwards” equal to fruit[index – 1]. So the index was always starting at the wrong place. I made a few changes to fix this activity. I set the index to equal len(fruit) – 1 and the while loop ends when index is below 0. It took about 20 seconds to see the error this time around.

<h3>Fixed Strings! Ex 1</h3>
<iframe src="https://trinket.io/embed/python/883271f4f6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<h2>Collaborative Experience</h2>
One thing I have enjoyed about this course is the opportunity to see how other people are coding and problem-solving. There are so many cool, creative ways I have seen people approach problem-solving. What I have heard and seen people do is turn a program into 3 or 4 smaller programs and think through addressing each of the sub-problems before tackling the larger program. Moving forward, I definitely want to implement this strategy. However, I don’t think I’ve fully appreciated the idea of pair programming yet. I can see why it would be successful; however, the two experiences I had with pair programming, the way in which we both worked and thought about coding did not mesh quick enough and we never actually attempted pair programming as described.

<h2>Moving Forward</h2>
Not an excuse, but with my MPA Portfolio and MSIS proposal due on 2/23 and increased work hours, my time on Python has generally been restricted to the weekend. Moving forward, I’m excited to spend more time developing and improving upon my Python skills. 

Adopting different strategies for debugging will be central to my approach moving forward in this course. From simply running my code more often, avoiding the usual doubt in my code, and breaking down the goal’s program into manageable parts and determining the flow of control. Rather than just diving into the code, breaking down the program into more manageable pieces I believe will smoothen my coding experience.

I do believe though that I have gotten much better at googling for python code and examples to help me think about what I am attempting to implement. While sometimes I spend too much time reading through code that is irrelevant to the program I am implementing because something caught my eye, I understand how to use Python’s dictionary and search for code via Stack Overflow.

<h2>Next Steps</h2>
Although a very easy exercise, I was so excited to complete the following trinket because this is the kind of python code that I could actually imagine implementing in the near future to speed up the process of cleaning data. I spend a lot of time at work cleaning Excel data and being able to add on to Excel’s already powerful features be more customizable through Python is something I am looking forward to.
	
<h3>Strings! Ex 5</h3>
<iframe src="https://trinket.io/embed/python/4e9bebf46e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In the latter half of this course, I want to start using Python in ArcGIS and in Excel; however, I have been having trouble installing openpyxl, a module for the use of Python in Excel. By the end of this course I plan to have read through and practice Python through the text Automate the Boring Stuff.

Moreover, I want to get to a place with Python where I am comfortable coding and running my code without constantly double-checking my code. I also feel like I end up spending a lot of time googling how to do something rather than actually attempting to figure out and think through what I am attempting to program. I will be able to do this as I trust myself more which will require more time coding.


