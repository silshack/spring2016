---
layout: post
author: camazotz
title: "Navaneet's Game App!"
---

Game App:
<iframe src="https://trinket.io/embed/python/4c3a6d671f" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Originally planned Gameplay: I want to build the classic game 'Snake'. The snake moves on the screen according to user input (with arrow keys) towards objects on the screen. As it swallows these objects, it grows in length. The snake is not allowed to collide with any of the four "walls" of the screen (defined by some preset coordinates and perhaps outlined by a colored border) or itself.

Revised Gameplay: It was extremely difficult to resize the shape of the snake and have it move on the screen accordingly so I revised the game to be more of an obstacle course game. The user has to move the primary object towards "food" objects without colliding into an obstacle or a wall. As the user continues to collect food objects, the number of obstacles increases and the speed increases (this increases the difficulty).

My originally planned milestones were as follows.

Milestones:

- [ ] Create the snake shape
- [x] Set the boundaries of the walls
- [x] Take user keyboard input and move the snake accordingly
- [x] Randomly place objects on the screen
- [ ] Grow the snake when it swallows an object
- [x] End the game if snake collides with the wall
- [ ] End the game if snake collides with itself

Stretch milestones:

- [ ] Make the objects images of food rather than random shapes
- [x] Add additional obstacles on the board
- [ ] Add objects that reduce snake's size if the user reaches them within a given time
- [x] Add a point system that increases as the snake swallows more objects

My revised milestones for the modified gameplay is as follows:

Revised Milestones:

- [x] Set the boundaries of the walls
- [x] Take user keyboard input and move the snake accordingly
- [x] Randomly place objects on the screen
- [x] Move the obstacles in a random direction
- [x] End the game if snake collides with the wall
- [x] End the game if snake collides with another obstacle

Reflection:

My original plan to create a game like 'Snake' but the difficult aspect of that plan was getting the snake to grow in size and move on the screen as a snake (not as one whole block). To this end, I tried the turtle resize method but found out later that it was no longer supported. I also tried stamping to give the visualization of a snake's movement on the screen but I would then have no way of detecting a collision with the snake itself. As a result, I tried to maintain a list of turtle objects and appended onto the list whenever the main turtle object (or the head of the snake) swallowed an object. However, it was very difficult to get all of the turtle objects to follow one another precisely behind one another and to bend appropriately when the snake turns in a particular direction.

As a result, I abandoned the snake game idea and opted for an obstacle course-like game in which the user has to navigate his "snake" (or circular object) towards a target. Every time the user acquires a target, a new target is randomly placed on the screen along with a randomly placed obstacle that moves in a random direction. I used the check_intersect function from one of the O'Reilly videos to check if the main turtle collided with an obstacle or reached a target.

One of the difficult aspects of this game was handling the snake movement on the screen corresponding to the arrow key inputs. For example, if the snake is moving left, and the user presses the right arrow, the snake should not respond. So I had to check the snake's heading and for each case to decide the appropriate heading to change to.

I also added in difficulty levels so that as the user acquired more targets, the speed of the snake increased, making it more difficult not to collide with obstacles or the wall. I kept track of the number of targets acquired via a global variable.
