---
layout: post
author: camazotz
title: "Navaneet's Drawing App!"
---

Drawing App:
<iframe src="https://trinket.io/embed/python/c04703bc26" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The goal of my app was to enable the user to fill the screen with tessellation shapes by clicking on any given shape to draw its adjacent shapes. Below are the milestones I had for my project:

Milestones:

- [x] Create a tessellation shape module
- [ ] Place one shape at a random location on the screen as a starting point for the user
- [x] Add width/height parameters and color in the appropriate parts
- [x] Add a click handler function that draws adjacent shapes with the appropriate color patterns

I completed three of my four milestones. I was not able to complete the second milestone (placing one shape at a random location on the screen) because doing so would have required adding a considerable amount of code to account for four adjacent sides. My app currently draws tessellation shapes on two adjacent sides (on the right and below). 

Each of those cases required custom code to handle, so addressing the cases for left and up would have taken even more time. As a result, instead of placing the shape at a random location, I place it at the top left corner of the screen, so that way the user is guaranteed to be able to fill the screen (since the shapes are drawn to the right and bottom).

Thus, my revised milestone list is as follows:

Milestones:

- [x] Create a tessellation shape module
- [x] Add width/height parameters and color in the appropriate parts
- [x] Add a click handler function that draws adjacent shapes with the appropriate color patterns
- [x] Be able to fill the screen with tesselation shapes

Reflection:

This app revealed to me how much I am still not able to do in Python with my current knowledge. Since the user would be clicking on any given shape on the screen, I wanted to register a click listener with each shape object but I didn't know how to do so. The only click listener I knew how to implement was screen click and turtle object click, both of which aren't suitable for this case. I even tried to overlay an invisible turtle shape on top of each shape that was drawn to implement the click listener but I was not able to resize the default square shape that turtle provides. The API seems to provide some methods to resize but they gave an invalid method error (either I was not using them properly or Trinket did not recognize them).

After attempting a variety of options and hacky workarounds for this problem without luck, I decided on using lists to store the coordinates of each shape and searching through the list on each screen click to determine whether the coordinates of the click fall within one of the shape boundaries. It works but it's pretty inefficient and I'm not happy with the solution - there has to be a way of registering the shapes directly. Even if I used classes and created shape objects, I had no idea how to actually map those objects with their screen coordinates and register a click listener.

I signed up for the trial of the video lectures on O'Reilly and watched some segments and thought it was pretty helpful. I'll continue to watch them and hopefully registering shape objects with click listeners or some variety of that concept is covered there so I can use it for a future project.
