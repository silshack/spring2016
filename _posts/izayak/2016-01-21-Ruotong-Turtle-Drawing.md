---
author: izayak
title: "Ruotong's Turtle Drawing"
layout: post
---

Here is the embedded link from Trinket:  
<iframe src="https://trinket.io/embed/python/b8066c8fd0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>  

I'm kind of sad of the result.  
What I was trying to draw is like this picture:     https://www.google.com/search?q=%E6%AE%BA%E3%81%9B%E3%82%93%E3%81%9B%E3%83%BC&espv=2&biw=1548&bih=738&site=webhp&source=lnms&tbm=isch&sa=X&sqi=2&ved=0ahUKEwiJ9IzgtrzKAhUM6yYKHcA3AwoQ_AUIBigB&dpr=0.9#imgrc=utzBgU1ek9Wk1M%3A  
But the result...umm...more like a emoji face...  

What I did:  
1. Searched online and find this for drawing a circle and used this for drawing radius:
https://www.youtube.com/watch?v=zCstXk-46nE  
2. As I used this method, it's hard to do math with it. So I just try different value to draw sensei's mouth, hours...
because the speed of drawing a circle is quite slow... then I found that I can figure out the place later which at first I thought
could be hard. Actually that's way better as drawing radius is fast.  

The problems that I was facing:
1. I need to make sensei's teeth white, instead of yellow as his face... I tried using fill, but the result is weird.  
2. To indicate that's his teeth, I need lines with different length. But comparing to the first one, this can be solved, but can be
quite tedious.  
3. For the face, either square or circle would be fine. But if I use square, the radius cannot be on the top of the square.   
I guess that should be my problem. I am sure this can be achieved by Turtle.  
4. Did not figure out why the turtle.write() did not work. The place is not where I wanted the message to show up. Confused about that.

All in all, although it takes time, it's interesting!   


Feedback from insturctor:  
in your program, you send your turtle to 200,-30. The canvas goes from -200 to 200 in either direction, so this puts the turtle way off the the right of the screen. When you write(), the text is then not visible. Also, your pen is still down, so the turtle draws a line.  
Try sending the turtle to 0,-150 or something and then writing. Also, remember that your turtle will write in his current color, so you will probably need to change it for the writing to show up.    
