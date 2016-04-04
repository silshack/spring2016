---
author: yiyangshi
layout: post
title: "Yiyang's Poetry Slam Exercise"
---

Here is the program:
<iframe src="https://trinket.io/embed/python/15feb10b2d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

My gut feeling is that there are some easier way to realize poetry slam. My current program has two main steps. The first step is to append all the lines the user typed in into one list while counting how many lines the user typed in. A line typed in is stored as an item in the list. The second step is to print each line, i.e. each item in the list, in separate lines. I realize this by implementing another counting variable. As long as the item number is smaller than the item number of "done", tina will keep writing. 

I think my program is somewhat redundant because we can just store each line input as a separate list. Then tina will only need to print all the lists. However, this idea will need a loop where the variable name changes within each iteration. It will look like this:

```
input_line = []
while input_line != "done":
  input_line = input("")
  poetry_line_[i]= input_line
  i = i + 1
while j < i:
  print poetry_line[j]
```

I don't know if it is possible to be realized.
