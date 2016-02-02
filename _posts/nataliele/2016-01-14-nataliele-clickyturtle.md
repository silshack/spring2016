---
layout: post
author: nataliele
title: Natalie's clicky turtle
---

I spent WAYYY too much time trying to make the program works according to my vision but I still havent solved it. Basically the sharks are supposed to appear randomly several times and the user is supposed to click on the sharks to destroy them. (Why are there sharks in the river? They're freshwater sharks, trust me.) However, I could only make 1 shark to work...

<iframe src="https://trinket.io/embed/python/baaea0b0d7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Several things that interfere with my vision:
1. For example in this version:
![Turtle image](http://nataliele.web.unc.edu/files/2016/02/clickyturtle.png)
Python doesn’t wait for the clicky function to finish (ie the user click on screen) to execute the remaining codes. So the sharks keep appearing and not after each click like I wanted to.

2. It seems like I cant use the variables defined in a function. If I want to call it in another function, I have to define that variable outside of a function. For eg if shark_xy is defined under shark(), I wont be able to call it in clicky(). So I have to define it outside funtion, which gets in the way of looping the random location of a new shark.

3. Also clicky doesn’t take another value besides the click coordinate (?) so I cant put another parameter for the function.
After clicky is executed, I cant make the program continue to execute the codes after the clicky function.
