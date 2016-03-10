---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Game App"
---

Here is my completed drawing app:
<iframe src="https://trinket.io/embed/python/d388636b70" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This assignment was the most difficult one yet, but I am overall quite pleased with how it turned out.  One of the biggest lessons that I learned while working on creating my game was that I need to reexamine my programming strategy and break down the goals that I have laid out into pieces of milestones rather than creating one big picture that needs to look exactly as I want it to.

Part of the problem was that I had initially settled on trying to recreate the Snake game, but after a few nights of little success and a lot of frustration (and talking things over with Elliott) it was decided that I needed to rethink my game approach.  What the final product of my game eneded up being is a sheep herding game.  Tina is the shepherd, and she has two sheep.  When the user presses the arrow keys, Tina moves a certain way, but so do her sheep.  I set my program to have the sheep move in different directions and pixels than Tina, so the user has to work out how to control Tina to get the sheep to eat all their apples that I have spaced out around the screen.  There are five apples total, and while the apples are being eaten, a count of how many apples have been eaten displays in the top right corner of the screen.  Once all the apples have been eaten, a "You Win!" statement is printed on the screen.

While this game was not what I had initially envisioned, I am very happy that it turned out the way that it did-partially because I was experiencing emotional distress in regards to my program and how I did not believe that I would be able to actually make this work.  I was able to acheive most of the requirements for the program, and I was also able to accomplish the majority of the milestones that I had set out from the beginning.  Here they are in their completed format:

Necessary Milestones: 
- [X] allow the user to start the game by clicking on the screen
- [X] allow the character to respond to key input for movement 
- [X] allow the user to win 
- [X] indicate winning by having the turtle write it on the screen or playing animation
- [X] keep track of how much the turtle has “eaten” by displaying the number on the screen

Because of the difficulties that I had been facing with my program I decided that I would just stick to accomplishing my necessary milestones and move to the optional and stretch milestones another time, especially since they were more relevant to my original plan with the Snake game.  It would have been nice to add further components to my game, such as restarting the game when the sheep went off the screen, but by the time I had gotten my program written and working, I decided that this was a battle I would leave for another day (or another program perhaps).

Other than the essential lesson I needed to learn about how I need to take each piece of my program a step at a time and break down even the milestones into the tiniest bits possible to get things to work, I also felt that this program helped enhance my understanding of what classes do and how I can use Boolean values as a way to count or loop through certain parts of the program.  I'll begin by addressing the use of Boolean values, which can be seen best in my check_intersect function.  Here is the overall code for my function:

```
def check_intersect():
  #Creating a Boolean that will store whether an apple has been hit or not
  tag = False
  # Check to see if a sheep ate an apple
  for Apple in Apples:
    if not Apple.hit and Apple.intersect(first):
      Apple.set_color("Lawn Green")
      Apple.hit = True
      tag = True
    if not Apple.hit and Apple.intersect(second):
      Apple.set_color("Lawn Green")
      Apple.hit = True
      tag =True
  # Add each apple to the list
  hits = []
  count = 0
  for Apple in Apples:
    hits.append(Apple.hit) 
    if Apple.hit == True:
      count += 1
  #Check to see if any apples hits were added to the list and update the counts
  #as needed  
  if tag == True:
    Matthew.show(count)
  #Check to see if the user wins 
  if count == 5:
    printwin()
```

I could not get my counter on the screen to work like I wanted it to for the longest time, since it keep looping through the apples and updating with values that did not accurately reflect how many apples had been eaten.  I discovered that what I needed was a way to count the number of apples that had been eaten.  It took me a ridiculously long amount of time to figure it out, but finally, I was able to realize that if I created the variable "tag" as a Boolean value that equaled False until each apple had been hit, then I could count this and then show the count to the screen.  When I finally got this to work, I was pretty excited.  Now I know that I can use Boolean values in a way that I had not previously thought of that actually helps simplify the code overall.

Learning about classes in this code was a concept that took my mind a while to wrap around, but simply by the nature of playing around with them and trying new things, I think that this idea finally clicked for me.  I can create a class that initializes a specific type of object, and then I can add special moves to the class to make this object do specific cool things that others in the program wouldn't be able to do unless they were a member of that class to begin with.  Here is one of the classes I created and adapted to add some custom methods to that I'm particularly prooud of:

```
class Writer(turtle.Turtle):
  def __init__(self, x=0, y=0, screen = myscreen):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.penup()
    self.speed(0)
    self.goto(x, y)
    self.screen = screen
  #Allows our counter to display in the top corner
  def show(self, message, alignment = "right", size = 18):
    self.screen.tracer(0)
    self.clear()
    self.write(message, font=("Arial",size), align=alignment)
    self.screen.tracer(1)  
  #This shows the front screen animation with directions
  def frontScreen(self):
    self.screen.bgcolor("yellow")
    self.penup()
    self.goto(0, 25)
    self.pendown()
    self.write("Welcome to the game!", font= ("Arial"), align = "center")
    self.penup()
    self.goto(0, -20)
    self.pendown()
    self.write("Tina is the shepherd and needs to get her sheep to eat.", font= ("Arial"), align = "center")
    self.penup()
    self.goto(0, -40)
    self.pendown()
    self.write("Make Tina move using the up, left, and right arrow keys.", font= ("Arial"), align = "center")
    self.penup()
    self.goto(0, -60)
    self.pendown()
    self.write("Each move that Tina makes influences the movements of her disobedient sheep.", font= ("Arial"), align = "center")
    self.penup()
    self.goto(0, -80)
    self.pendown()
    self.write("Adjust Tina's movements to help the sheep eat their apples.", font= ("Arial"), align = "center")
    self.penup()
    self.goto(0, -100)
    self.pendown()
    self.write("Make them eat all the apples.", font= ("Arial"), align = "center")
    self.penup()
    self.goto(0, -120)
    self.pendown()
    self.write("Click the screen to begin", font= ("Arial"), align = "center")
  #This sets the game to start where the counting begins
  def clearDirections(self, x, y):
    self.screen.bgcolor("Lawn Green")
    self.clear()
```

This class is my custom class for turtles that do any type of writing or display on the screen of my program.  In the initialization portion of my class, I created my special turtle and gave it the ability to connect to the screen.  The following special functions in this class allowed me to do some pretty exciting things.  My show() function allowed the count for the number of apples eaten to display on the screen.  My frontScreen() function was called at the beginning of the program and showed the directions for the game.  My clearDirections() function was used to remove the directions from the screen and allow the user to play the game.  It took a while for me to wrap my mind around how exactly I would use it, but I think that simply by nature of creating multiple classes and assigning different functions to them that I grasped this concept better.  Custom classes are useful and can help save a lot of time and lines of code when working on a project like this one.

In conclusion, this was an assignment that challenged me a great deal, but I learned a lot from it and am satisfied with the final product.  In the future, I will continue to work on breaking my program down into easily acheivable milestones, use Boolean variables to help keep track of certain things in the code, and create custom classes that will allow me to put a lot of useful information into just one portion of the code.

