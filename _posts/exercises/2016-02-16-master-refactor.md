---
layout: post
author: elliott
categories:
  - exercise
title: Master Refactor Turtles Exercise
---

Submit a well-formatted pull request to our class blog with embedded Trinket programs for the below exercises.
Complete these on your own, using any materials you need. Do not
look at other students' submissions until after you've completed your work.  

**After your programs are done**, check other students' work and other resources online if you had questions.
Include a reflection about what you think you've learned and any concepts that are still fuzzy to you.
Did you encounter frustrating situations? Did you feel a lightbulb turn on?

___


Refactor the below trinket program.  You should use custom modules, functions, and any other tools neccessary to 
clean up the code, increase readability, and modularlize the logic in the program.

<iframe src="https://trinket.io/embed/python/0a04b3533d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Your finished program should look and behave like the original, but with cleaner, more readable, and more easily
hackable code.

Some concepts we haven't covered yet that you may want to read ahead on:

* **dictionaries**  Whenever you see `{` and `}` in Python, think dictionaries.  These are like lists
on steroids. They take the form `{ key1: value1, key2: value2 }` and will let you look up the keys to
get the values with a syntax similiar to lists, such as `dict[key1]`.  Check out how they're used with 
the `colors` in the tetris program.
* **files**  We haven't yet learned about opening and reading through text files (as opposed to modules, which
we have covered).  Sometimes data like the shape of pieces may be convenient to store in text files during a
refactor.

**For an extra challenge worth extra credit**, improve upon the functionality of the original by 
implementing more of the Tetris rule set. This is quite an extensive project, so it's important 
to pace yourself, and pick and work on only one new feature at a time.  It's very unlikely that you'll
be able to implement all of Tetris in a weekend, so pick your battles wisely.