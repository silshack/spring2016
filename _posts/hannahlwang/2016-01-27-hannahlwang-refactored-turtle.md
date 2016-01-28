---
layout: post
author: hannahlwang
title: "A Refactored Logical Turtle"
---

For this assignment, I chose to refactor my logical turtle, who originally made balloons based on user input and demanded politeness.

Original:
<iframe src="https://trinket.io/embed/python/28c80d3d0a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I chose this turtle exercise because I had to do a lot of copying and pasting, which made it a good candidate for functions. I wanted to make the entire act of drawing a balloon one function. This required first defining the two parts of the balloon as two separate functions: the circle and the triangle (tail). Then I called these functions in the drawballoon function.

I also wanted to use the random module to make randomly colored balloons, but I couldn't figure out how to do that, so instead I used the random module to make randomly-sized balloons, rather than relying on user input.

I loved turning the balloon drawing into a function, because for each balloon I only had to specify the color and the starting point (based on the randomly selected integer).

Politeness is still required.

Refactored:
<iframe src="https://trinket.io/embed/python/a9751441ba" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
