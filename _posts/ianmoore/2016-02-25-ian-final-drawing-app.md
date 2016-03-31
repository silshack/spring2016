---
layout: post
author: touchwick
title: "Ian's Drawing App"
---
This is my drawing app:

<iframe src="https://trinket.io/embed/python/622c3769c0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### These are my milestones:
- [x] Build starter code
- [x] Working interface - Buttons respond to clicks, mode buttons clear when one mode is selected.
- [x] Mode 1 - First mode will draw
- [x] Mode 2 - Second mode will draw
- [x] Mode 3 - Third mode will draw
- [x] Clear and reset - Clear button functions correctly, program resets to initial state, ready for user to reinitiate
- [x] Debugging - Check to make sure that everything <i>actually works</i>.

I believe that I met them all. My buttons respond to clicks, the mode buttons disappear and are replaced by the "Clear" and "Switch Mode" buttons, and the current mode is displayed at the top of the screen. Each mode draws as I wanted it to. The "Clear" and "Switch Mode" buttons function correctly. "Clear" resets the program to its initial state, while "Switch Mode" leaves the user's drawing as-is and allows the user to select another mode in order to continue drawing. As far as I have been able to determine, there are no show-stopping bugs in the program. Ultimately, I think I expanded my scope. I had initially intended for the color selection to take place only within the Line mode. When I realized I had more time than anticipated, I added it to the other modes and implemented pen size selection as well. (I'll admit that size 50 is a little impractical, but I think it's fun.)

There were two significant challenges for me during this process. Getting the program to reset was very frustrating. I had not thought about how one might exit a function before this, and my attempts to make this program into a ```while``` loop resulted in my browser crashing. Calling the ```primary``` function back works quite well. My loops back on itself not because it uses loops (though it is worth noting that there are several ```for``` loops in the drawing functions), but because the user must call back ```primary``` in order to erase a drawing or select a new mode. I'm very proud of that.

When I got everything working, I tried to set up Line mode to use ```.ondrag```. This went... fine? I got my turtle to drag, but I couldn't get him to stop dragging. If ```.ondrag``` is working during Floral mode, the browser will crash as the turtle attempts to draw a new flower at every pixel. The problem was intriguing, but I believe that my app meets the requirements of the assignment without the dragging functionality, and I don't know that I needed to make more work for myself.

I did at one point have a different app, one that served to let me try a few things before I decided to rewrite my program almost entirely. That app is here:

<iframe src="https://trinket.io/embed/python/cf9a42eff0" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

There are problems with it, problems I was able to overcome in the revision. The biggest is the issue of color. I had three different turtles doing my drawing, and, as a result, I had to bind color keys for all of them. In the final version, embedded at the top of the post, I use one turtle to do all of the user's drawing. One turtle, one set of key-bindings, and the ability to make colors persist from mode to mode. I hope that this initial version serves to demonstrate improvement from version to version.
