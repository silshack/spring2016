---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Drawing App"
---
This is my drawing app final version:
<iframe src="https://trinket.io/embed/python/bfccfd4756" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This was most definitely the most difficult assignment that I have done so far for this class, and while I know that my program is not perfect and could use improvements still, I think that I challenged myself and am surprised that I got as far as I did.  I look forward to working to improve my program and skills into the future so that I can get better in time. I started my program with some pretty lofty milestones, although I did not know it at the time; I guess I got overambitious and did not realize that I was not thinking realistically about the program.  Here are my original milestones:

- [ ] Pressing certain keys allows changing the width of the star
- [ ] Allow the user to drag the turtle across the screen to make the shooting star
- [ ] Have the shooting stars clear when the user presses enter
- [ ] Have a setup module that creates a grassy ground and black night sky
- [ ] When the user drags the star across the screen, have the flowers glow

I realized as I worked with my code that there were definitely some things that were a bit out of my scope and things that could be nice additions to make my program "pretty" after I got the main foundations down.  One of these was when the user drags the star across the screen to have the flowers glow, so I decided to remove this milestone since it was a bit out of my scope and I wanted to make sure that other things worked in my program.  Once I get the kinks in my program worked out, this is something that I can work to improve.  The * * show areas of my code that I adapted.  Here are some milestones that I accomplished from both the original milestones and some additions that were more feasible:

- [x] Pressing certain keys allows changing the width of the star
- [x] Allow the user to drag the turtle across the screen to make the shooting star
- [x] Have the shooting stars clear when the user *clicks the button on the screen*
- [x] Have a setup module that creats a grassy ground and black night sky
- [x] Have the screen change modes when the user clicks on the screen

According to the instructions of the program, I have technically fulfilled all the requirements, but there are a few glitches that I'll address bit by bit.  The first is that I am able to switch modes, but when you switch from drawing stars to drawing planets mode, the planets still appear when you click on the screen to drag the turtle and when you click off the screen to let go of the turtle.  I've been unable to figure out how to change this so that the circles stop being drawn on click.  Even when I tried adding if and elifs to limit what happens in what areas of the screen, it cleared up the problem where I could at least switch between modes, but it did not get rid of the constant circle appearing tendencies.  I was okay with this for now, since in star drawing mode it was focused primarily on drawing the star and all other areas of this code worked.  This is the primary issue that I would like to sort out. 

The root of my problems seem to lie with the drawing planet function, since I also was uncertain how to get it to stop drawing circles everywhere without using the if and elif statements that I had in my code.  This is ultimately how I had to write my function to make it something that would ultimately work:

```
def the_circle(x, y):
  if int(y) >= -99:
    myscreen.tracer(0)
    lyn.hideturtle()
    lyn.fillcolor(random.choice(colors))
    lyn.begin_fill()
    lyn.penup()
    lyn.goto(x, y)
    lyn.circle(25)
    lyn.pendown()
    lyn.end_fill()
    myscreen.update()
    myscreen.tracer(1)
  elif int(x) >= -35 and int(x) <= 35 and int(y) <= -125 and int(y) >= -175:
    thistle.reset()
    rae.reset()
    rae.hideturtle()
    star_directions()
    the_star()
  elif int(x) >= 100 and int(x) <= 150 and int(y) <= -125 and int(y) >= -175:
    myscreen.tracer(0)
    tina.reset()
    tina.hideturtle()
    rae.reset()
    thistle.reset()
    setups()
    myscreen.update()
    myscreen.tracer(1)
```

I'm going to work to improve this in the future.  The next issue that I would like to work on is trying to make the shooting stars simply lines rather than the abstract features that they become (although it's kind of cool looking since they could be interpreted as Northern Lights).  I did use the tracer() and update() terms to help with this, but they did not seem to have the intended effect that I thought they would.  The final issue that I would like to improve upon is hiding the appropriate turtles, since they sometimes randomly pop up even though I have them hidden appropriately.  It's probably some small mistake that I'm making that isn't clear to me right now.

Despite all the obstacles that I have had throughout creating this program, I do feel like I really went through a lot of personal growth and challenging myself for this project.  I learned how to use the onkey() and onscreen() tools better, worked on changing with modes(although I could use some improvement there), and was able to accomplish more of my milestones than I had realized. Initially, I'd thought that I hadn't been able to complete any of them, but as I worked through the project, I found that my milestones evolved and adapted to make the program suit my needs.  I also did a pretty good job of documenting my code to explain the reasoning behind what I'd done.  I look forward to working on and improving my skills with programs like these into the future.







