---
layout: post
author: RhymesWithMecca
title: "Becca's Second Project Update"
---

**Trinket:**

<iframe src="https://trinket.io/embed/python3/c4ce5cc5fd" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Reflection:**

I accomplished all of my goals again!  The textwrap module that Elliott mentioned in class fixed my problem of trying to print variously-lengthed DNA sequences using a for loop or a while loop (or, as I was doing it, multiple if statements).  I began the evening with 291 lines of code for the cDNA section and finished with 137.  So that was exciting.  The gDNA milestones were not, as predicted, that difficult, since they were similar to the cDNA ones.  My main problem was keeping track of variable names and formatting my print statements correctly.  At one point, I was printing the complementary sequence instead of the reverse complement because I used the wrong variable name in the .join function (oops).

I discovered midway through this process that my cDNA file is all in upper case and my gDNA file is all in lower case.  I need to go back through all of my code and either convert everything to upper/lower case pre-capabilities, or change all of my if statements to be more general.

Over the weekend, I hope to add functions, user input (right now, it just prints all of the capabilities all at once), and a visual component.  Then next week will be all about debugging and optimization.

**Thursday's Milestones:**

- [x] print percent AT/GC content
- [x] print the length of the sequence
- [x] print the reverse complement
- [x] print the complementary DNA strand

**For Tuesday:**

- [ ] fix capitalization
- [ ] program has help function, accessible by user input
- [ ] program is iterable
- [ ] program has visual component
