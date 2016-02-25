---
layout: post
author: hannahlwang
title: "Hannah's Drawing App"
---

<h4>Drawing App</h4>
<iframe src="https://trinket.io/embed/python/6407e7f1e6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<h4>Milestones</h4>
- [x] create starter code with modules for setup and shapes
- [x] create background with water and sky
- [x] create onclick drawing action that deals with perspective
- [x] define shapes in shapes module (boat, cloud, seagull)
- [x] random from list of colors for boat sails
- [x] make a different turtle draw ripples in the same location as boats
- [x] use for loop to make several differently-sized circles for ripples
- [ ] make combined "key-and-click" function to press "b" for birds and THEN click in location in the sky for bird to be drawn
- [x] use onkey to draw bird in random location when user types "b"
- [x] create instructions for user in graphical interface
- [x] create clear button and if statement to deal with clear

<h4>Reflection</h4>
For my drawing app, I made an ocean scene with boats, clouds, and birds. When the user clicks a location in the water, a boat with a randomly colored sail is drawn, with ripples in the water preceding the boat. When the user clicks a location in the sky, a cloud is drawn. When the user types "b", a bird is drawn in the sky at a random location. There is a "Clear" button that clears the screen of all drawings (but not the background), allowing the user to start fresh with his/her drawing.

I ran into a couple of roadblocks in this program. The first major problem I had was with the ripples. I originally wanted to create oval-shaped ripples, making the ripples a turtle and using the shapesize attribute. However, I ran into a problem using shapesize in Trinket, and had to use circular-shaped ripples instead.

My other major issue was with my incompleted milestone. I wanted to find a way to create a kind of combined "key-and-click" function, where the keystroke would define the shape of the object (bird or cloud), and the click would determine the location (as with the boat). However, after many attempts, I was unable to do this. My original solution was to call both the bird and cloud shapes with keystrokes, and have them drawn at random locations in the sky, but I found that this was an unsatisfying and sloppy experience for the user, especially when there was no control over where the clouds would go. I settled on keystrokes creating birds at random locations, and clouds being drawing where the user clicks.

Despite these challenges, I am fairly pleased with my final result. The user is able to interactively create a nice picture, with some variation every time.
