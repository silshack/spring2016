---
layout: post
author: hannahlwang
title: "Hannah's Clicky Turtle"
---

For my clicky turtle, I decided to go with the turtle theme and make a lily pond, with lilypads and flowers. Click anywhere in the box to make differently-colored lilies:

<iframe src="https://trinket.io/embed/python/a89c1fca50" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I had Sally set up the screen with differently-sized lily pad. I used a function to define the shape of the lilypads, which takes the arguments of x and y coordinates, rotation, and circle size. This part was pretty straightforward, because I've done a lot of work with circles in my other programs.

Figuring out the lilies was much more difficult for me. Since I had done a lot of circles in past assignments, I wanted to do something with angles this time. I took inspiration from Colin, and read the Wikipedia about star polygons <a href="https://en.wikipedia.org/wiki/Star_polygon">here</a>, because it's been a really long time since I took geometry. After a lot of trial and error, I was able to figure out how big to make the angles, and how many lines I wanted Tina to draw. I had a helper function called "flowershape", which I called twice in the "clicky" function to make the two shapes - the outer colored shape and the inner white shape.

I wanted to have the effect of random colors, but without the actual range that you get with the random module (I didn't want brown flowers!). So I ended up using a conditional statement to decide the color of the flower based on the x and y coordinates of where the user clicks, which limits the output to four colors. This function is "flowercolor". I separated this out as a helper function because it actually didn't work when the conditional was nested inside the "clicky" function - I'm still not sure why, but I ended up with all coral-colored flowers when I did it like that.

I'm pretty happy with the result! My original idea was to make ripples in the water when you placed Tina somewhere, but I wasn't sure how to make circles grow over time. Maybe we'll learn the tools to do this later. But this was a really good learning experience for me, with both polygons and helper functions.
