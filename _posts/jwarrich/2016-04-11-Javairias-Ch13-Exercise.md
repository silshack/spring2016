---
layout: post
author: jwarrich
title: "Javairia's Chapter 13 Exercise"
---

<iframe src="https://trinket.io/embed/python3/84e482f0d6" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
Reflection:

So for this exercise, we were to pull out relevant information from the location given to us by the user. When looking for what information to extract, I tried to find stuff that were commonly available given different inputs. With that said, longitude, latitude, place_id, and formatted address were 4 that I wanted to extract. The code given already had the 3 of the 4 already given so most of what I did was cleaning up the code to make it user friendly. I also wanted to add something that handled inputs that had multiple results. So for example, I noticed that Chapel Hill had multiple locations so I added an if/else statement to handle input like that. I tried to find the country of each location, but it was difficult to do since the index kept changing in relation to the type of input. One question that I had was how the results are given. When I typed in Chapel Hill, the first result was of Chapel Hill, NC but there are other locations in Tennessee and Alabama with the same name. How does it decide which one to print out?
