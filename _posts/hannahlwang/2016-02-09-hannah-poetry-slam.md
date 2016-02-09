---
layout: post
author: hannahlwang
title: "Hannah's Poetry Slam"
---

<iframe src="https://trinket.io/embed/python/85354e940b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I started with the empty list "poem", adding each "line" from the user input to the list (line 16). The only big problem I encountered in writing this was getting Tina to write each line on different lines, rather than writing the whole "poem" list in one line. At first, my code looked like this:

```
poem = poem + [line]
tina.write(poem)
```

I realized that I had to use a for loop to get her to write each line individually, moving down after each one (lines 18-20).
