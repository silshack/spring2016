---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Chapter 6 Exercises"
---

Here is my 6.1 exercise:
<iframe src="https://trinket.io/embed/python/6bcb8c5c8b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This one was a bit puzzling to me, since I was able to easily get the string to list each individual letter going forward, but was struggling to get them to go backwards.  I discovered that the trick here was checking for the type of each variable after I called it and making sure that I could get the variables I needed to float to do so.  

Once I figured out how to get all my types just so, I was able to rework the code that I'd originally had for listing each letter individually forwards and make it go backwards.  Here is a sample of what it looked like:

```
while index < length:
  letter = user_input[index]
  print letter
  index = index - 1
  if index < 0:
    break
```

I discovered that I needed to set the index beforehand to a variable I'd named last, which was the length-1.  Once I was there, I kept counting down.  I had to remember that [0] references the first letter in my string, so I had to adjust the index to be less than 0 in order to account for this last letter to print.  After that, the loop breaks!  I was moderately puzzled as to why I could still enter numbers and they would print back to me, but I had to remember that unless I change them to float, they are interpreted as strings.

Here is my 6.3 exercise:
<iframe src="https://trinket.io/embed/python/15d23c014e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This one was not so bad for me, and I liked how I was able to combine my new string knowledge with my prior knowledge of functions.  Functions and learning how to write them are a skill that I'm still working to improve on, so this was a good exercise for me to play around with prior and new knowledge.  Here's my function that I wrote:

```
def counter(letter, word):
  count = 0
  for place in word:
    if place == letter:
      count = count + 1
  return count
```

Here is my 6.4 exercise: 
<iframe src="https://trinket.io/embed/python/c64d4841d4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This was also a pretty exciting exercise, as I got to learn how to do a new string method for a specific word. The code explanation for the website that we were referenced to better understand the method didn't make a lot of sense, but I found some examples online and  applied those to the definition that was in the reference.  After this, things clicked quickly.  I can see this being useful as for the previous exercise to shorten things up.  This will be good to keep in mind for the future.

Here is my 6.5 exercise:
<iframe src="https://trinket.io/embed/python/70c4946d0c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This was a trickier exercise that made me think about how to do this.  I really had to think about where I wanted to slice the string, since I discovered that if I set word.find to find the :, then I was a little further back than I'd intended to be.  I needed to change things up so that I was setting word.find to the space after the colon.  Once I'd found that, I guided my code to the 5 that marked the end of the string slice that I ultimately wanted to print.    After this, I created a section that allowed me to print the piece that I wanted to.  It took a little trial and error to make it appear exactly as I'd wanted, but once I understood that where you set word.find matters, things improved.

