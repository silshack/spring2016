---
layout: post
author: payalpn
title: "Payal's Drawing App" 
---

**Ice-Cream Drawing App**


<iframe src="https://trinket.io/embed/python/9f3ff11dc1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


**Revised Milestones:**

- [x] determine layout of game

- [x] create instructions function to display instructions of game 

- [x] determine toppings

- [x] create turtles for each topping

- [x] create ice-cream cone functions 

- [x] create function for each of the toppings

	- [x] cherry
	
	- [x] chocolate chips
	
	- [x] sprinkles
	
	- [x] whipped cream
	
	- [x] caramel
	
	- [x] fudge
	
	- [x] gummies 
	
		- [x] use for loop 
		
- [x] create restart turtle

	- [x] create restart function
	
- [x] create Option functions to change state of topping turtles 

- [x] create clicky function 

- [ ] troubleshoot problems --there is a small problem (not with the functionality) that I mentioned in detail in my reflection

- [x] add comments to program 


**Reflection:**

My plan for this program changed throughout the entire time I worked on it, as did my milestones.  Initially, I created buttons for the topping options available.  I was able to make it so the user could click on the button and then the topping would be drawn depending on the button selected, however, I wasn’t able to get it to draw the topping when the user clicked elsewhere on the screen.  I knew I needed to include multiple onclick functions by nesting them into a larger function, but I wasn’t getting my buttons to work the way I intended them to.  Initially I was able to get the clicky functions for the toppings inside of the larger clicky function for the screen, however, I noticed that I needed another function to make my program work the way I intended for it to.  Before meeting with my partner I had already created several functions for drawing different toppings and for drawing the ice-cream cone.  

Below is an embedded version of my trinket that I showed my partner during the Drawing App check-in (this version is different than the one embedded into the blog post due before this date because I ended up working on it more after I created the blog post).  

<iframe src="https://trinket.io/embed/python/a389767418" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

When discussing this post with my partner I explained the problem I was having with my program.  She suggested that I try using clicky turtles instead of boxes like in the example from class (“Tommy’s Clicky Turtle”).  I tried using turtles and turtle.onclick and I was closer to getting what I wanted to do.  Using the turtles instead of boxes/buttons made it so that my criteria was easier to select.  This also enabled me to call a function outside of my clicky function and use the result of that function as a criteria for the if/elif statements in my clicky function that I used when for screen.onclick.  By doing this I was able to reduce the amount of errors I had than my previous method.  In my previous method I used the coordinates of the boxes I created as the conditions for the if/elif statements in my clicky function.  This allowed me to call the functions when those boxes were selected, however, I became limited in the actions I could allow the user to perform by doing this.  

Currently, I have a problem with my program where after selecting a topping and then switching to another turtle topping, the previous topping will print on or near the second turtle I select.  I am able to draw a different topping afterward, but I have yet to figure out a way to solve the issue.  


