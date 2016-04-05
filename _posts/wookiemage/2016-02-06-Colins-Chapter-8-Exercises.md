---
author: wookiemage
layout: post
title: "Colin\'s Chapter 8 Exercises"
---
  Here\'s my first exercise:
  
  ```
  def chop (t) :
  
    print (t)
    
    print ("Here comes the chop... \n")
    
    del t[0]
    
    del t[len(t)-1]
    
    print (t)
    
    return None
  ```
  
  This one was pretty easy once I remembered that lists start at 0 instead of one. This means the last index position isn\'t the same as the overall length, but instead the length minus one.
  
  Here\'s my second exercise:
  <iframe src="https://trinket.io/embed/python/f0d10b449e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
  I think that the last line was not properly guarded. It\'s possible that an email could contain the line "From johnny" That line would be caught by our search because it starts with From, but it has fewer than three words so when 
  ```
  print(words[2])
  ```
  is called, it produces an index out of bounds error. I created a guardian line: "if (len(words) < 3)  : continue" to ensure if the line is shorter than that, it will be skipped.
  This still isn\'t definative, because an email could contain a line that contains three words but not have a day in the third word position, but at least this stops the code from failing outright. We can run another function at the end to remove any values that aren\'t on our list of expected day names.
  
  Here\'s the last exercise:
  
  ```
  
fhand = open(\'mbox-short.txt\')

count = 0

for line in fhand:

    words = line.split()
    
    # print \'Debug:\', words
    
    if (len(words) > 0 and words[0] == \'From\') :
    
       print(words[2])
       
# Code: http://www.pythonlearn.com/code3/search5.py

    ```
    
    This one was tricky, in part because of the way it was phrased. I kept thinking that I had to use those two conditions as they were written to trigger a "continue." It was only when I realized that I should reverse the two conditions to have them actually trigger the print, and moved the print inside the condition, that it worked.
