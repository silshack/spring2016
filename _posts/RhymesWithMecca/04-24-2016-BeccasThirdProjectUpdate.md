---
layout: post
author: RhymesWithMecca
title: "Becca's Third Project Update"
---

**Trinket:**

<iframe src="https://trinket.io/embed/python3/b418d38033" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Reflection:**

I accomplished all of my milestones again!  The capitalization was quick - I just converted the cDNA to upper case and the gDNA to lower case in one line each.  The difference is so the user doesn't get confused.  

I then started moving blocks of code around to add functions and ran into an issue.  It seemed for a while that Trinket wanted me to define each function before calling it, so the order of my code is, essentially, flipped from what I'd like it to be (chronological/what happens when).  I sketched this out on paper to make sure I wasn't messing it up (I'll bring this to class on Tuesday).  I then realized that the order is not the problem because I can call gDNA_options or cDNA_options in each capability before I define it - this is the iterative aspect of the program where the menu prints again so the user can do more things.  I'm thus not sure what the problem is.  I looked back at my Game App and I definitely called functions before defining them there.  This is also why I have two help functions rather than one - the calling order didn't work if the function was on the main menu and on the two sub-menus.  The error message is "NameError name 'cDNA_options' is not defined" when I move the "Main Menu" section from the bottom of the code to just after the initial user input section.

I also had a problem (this might be part of the same larger problem) with moving functions into separate modules to pare main.py down a little.  Hopefully I can fix these two problems (Milestone #2 for Friday).  I **think** that every functional problem has been solved and these are just style points.  Thus, I'd like to fix them, but won't go crazy if I can't.

The visualization part was fun.  My plan in my original set of milestones was to visualize the % AT/CG content, but I ended up visualizing the 20 types of codons.  This was not very hard to code and is a lot more readable than the long sentence with the number of each amino acid.  At first, I had zero tabs after each codon name and before the asterisks.  Then I added tabs to all of them so it was clearer.  Then I deleted tabs from the codons whose names are longer than a single tab.  Then I declared myself done with that portion of the assignment.

**Tuesday's Milestones:**

- [x] fix capitalization
- [x] program has help function, accessible by user input
- [x] program is iterable
- [x] program has visual component

**For Friday:**

- [ ] debug
- [ ] fix calling and moving function problem(s), if possible
- [ ] make code pretty (conciseness, comments, consistency).  I'm giving myself style points for alliteration here.
