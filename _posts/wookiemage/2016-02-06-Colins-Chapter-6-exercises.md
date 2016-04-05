---
author: wookiemage
layout: post
title: "Colin's Chapter Six Exercises"
---
  Here\'s the first exercise:
  
```

fruit = input("Please name a fruit")

index = len(fruit) -1

while index > -1 :

    letter = fruit[index]
    
    print(letter)
    
    index = index - 1
    
```
  
  Here\'s the second:
  
```

def counter (word, char) :
    
  count = 0
  
  for letter in word:
  
      if letter == char:
      
          count = count + 1
          
  print(count)
  
counter(\'mmmmmmmm\', \'m\')

```

These were pretty straigtforward and followed examples in the chapter pretty closely making it easy to start with some example code and adapt it.
  
Here\'s the third:

```

string = "banana"

string.count("a")

```

Here\'s the fourth:

```

str1 = \'X-DSPAM-Confidence: 0.8475\'

atpos = str1.find(\':\')

sppos = len(str1)

print(atpos, sppos)

fnum = str1[atpos+1:sppos]

float(fnum)

print (fnum)

```

