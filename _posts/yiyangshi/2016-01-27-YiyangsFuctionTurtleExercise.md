---
author: yiyangshi
layout: post
title: "Yiyang's Function Turtle Exercise"
---

Here is the refactor:
<iframe src="https://trinket.io/embed/python/f517596f4a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here is the original program:
<iframe src="https://trinket.io/embed/python/5292f2db95" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:

I used the logical turtle exercise as my original program and added three functions into the program. One to define the background color, one to draw star, and one to swith color between white and yellow.
When I first created the function for star drawing, I realized that one does not have to use the variables defined in the function in the main body of the function for that function to work. 
A simple example would be: 

```
length = 10
def tina_forward(x1, x2)
  tina.forward(length)
```

This may be an extreme case but I realized that I was making some functions with no actual function that was just a complicated version of the above example. It makes me think of the purpose of the function. I think functions should be independent and it need not use outside variables to realize the calculation. If not, it could probably be simplified as something else.
