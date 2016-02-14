---
layout: post
author: camazotz
title: "Navaneet's Midsemester Reflection!"
---

Over the course of the last month and a half, I have become more familiar with Python syntax and am pretty comfortable writing basic programs without having to look things up as much. Python is pretty widely used in industry, especially for data analysis (which is what I hope to specialize in) so it would be good to get the basics strong. 

It has also been fun using Github for managing our projects since it’s pretty widely used in industry. I’m looking forward to learning Git from command line in the next half of the semester. I hope while learning Git we deliberately make mistakes in our commits so that we become familiar with fixing them. As of right now, I have a clear-cut algorithm in my mind for the way I commit and merge into Github and after the first week or so there haven’t been any issues because I’m the only one pushing and merging into my directory. In industry, however, an entire team will be editing the same files and pushing and merging onto the same master branch, causing weekly or even daily merge conflicts. I’m not sure if we would have time to get practice in such a scenario but I think it would be great real-world experience if we did. 

Maybe we could simulate some “fake” class project in which all of us are editing parts of the same file and trying to commit onto the master branch. As other people commit, we will have to update our own fork and make sure their commits haven’t interfered with any code changes we made.

I’m particularly looking forward to learning about lists, tuples and dictionaries because they would be used often while working with large amounts of data. I was pretty satisfied with my use of lists and tuples in the Enhanced Tetris exercise. To store the previous pieces, I created a list and appended each piece as a tuple consisting of the piece itself, its x coordinate, y coordinate, and height (since all of those are required to draw the piece). To learn how to to do this, I consulted a short Python tutorial on lists [here]( http://www.thegeekstuff.com/2013/06/python-list/).

This was my implementation:

```
# Create list to store previous pieces
storedPieces = list()
numPieces = 0

while True:
    finTurtle.draw_screen(fin)
    finTurtle.draw_grid(fin)
    
    # Draw previous pieces
    for aPiece in storedPieces:
      draw_piece(aPiece[0], aPiece[1], aPiece[2], fin)
      
    draw_piece(piece, piece_x, piece_y, fin)
    time.sleep(delay)

    piece_y -= 1
    if piece_y - piece_h < 0:
        piece_y += 1    # Line up the piece with the bottom of grid
        
        # Add piece to list of stored pieces
        storedPieces.append([piece, piece_x, piece_y])
        
        # Check number of pieces added and increase display tracer
        # speed accordingly. For every three pieces added, increase
        # the tracer speed by 1000 so there is enough time to 
        # display
        if (numPieces + 3 < len(storedPieces)):
          numPieces = numPieces + 3
          tracerSpeed = tracerSpeed + 1000
          disp.tracer(tracerSpeed)
        
        # Create a new piece to draw on the next loop iteration
        piece_y = 22
        piece = random.choice(list(pieces))
        piece_h = len(pieces[piece].split("\n"))
        
    disp.update()

```

Along the same lines of using different data structures, I also want to experiment with numpy arrays and matrices and become comfortable using them to read in and move around data because numpy (along with scikit-learn) is a pretty popular choice for data analysis.

I thought the Tetris refactor exercise was really good practice in modularizing code and identifying redundancies. Because I treated each turtle as a separate module, I was able to include small snippets of code to handle all of their drawing functions, like so:

```
# Default code to setup turtles
def turtleSetup():
  someTurtle = turtle.Turtle()
  someTurtle.speed(9)
  someTurtle.hideturtle()
  return someTurtle
  
jay = turtleSetup()
sam = turtleSetup()
fin = turtleSetup()
but = turtleSetup()
key = turtleSetup()
speak = turtleSetup()

#Draw body
jay = jayTurtle.draw(jay)

#sam.showturtle()
sam = samTurtle.draw(sam)
sam = samTurtle.dostuff(sam)

#Draw buttons
#but.showturtle()
but = butTurtle.draw(but)

#Draw keypad
#key.showturtle()
key = keyTurtle.draw(key)
    
#Draw Speaker
speak = speakTurtle.draw(speak)
```

I’ve enjoyed collaborating and interacting with my classmates as well; it’s good to see the kinds of things other people are doing in their projects as that gives me more ideas on how I can use the tools at my disposal. I also like pair programming because I get to see how my partner approaches problems (in ways that are often more efficient than I would have thought of independently). It’s also good practice in explaining and communicating your line of thought with other people – another skill that will come in handy in industry.

I have struggled with making objects move concurrently. Most of my game ideas involve more than one moving object and what we have learned with turtles so far doesn’t seem to allow that. 

As an example, for the clicky turtles exercise I was hoping to making two or three other turtles moving in a periodic fashion across the screen and the objective of the game would be avoiding collision and making it to the treasure. Since I wasn’t able to make more than one turtle move simultaneously, I created a bunch of static turtles at random locations and had the main turtle navigate among them to reach the treasure, like so:

```
# Creates a turtle at a random location
def setTurtles():
  someTurtle = turtle.Turtle()
  someTurtle.shape("turtle")
  someTurtle.penup()
  someTurtle.speed(0)
  someTurtle.setx(random.randint(-200, 200))
  someTurtle.sety(random.randint(-200, 200))
```

According to what I’ve read online, the way to accomplish simultaneous movement/action would be using threads so I’m looking forward to learning about multithreading in python. This could also come in handy for data analysis. One thread could be scraping for data on the web, another thread could be reading data from a database, and another could be analyzing that data. From this example, I guess it’s obvious that I also want to learn how to scrape webpages using Python (so I’d have to familiarize myself with Scrapy and/or BeautifulSoup) and learn how to use Python to interact with databases. I’ve been curious about how NoSQL databases work so maybe I could look into using Python with MongoDB or Cassandra.

I’m not sure how much of the above I will have time to delve into in a semester but that’s my eventual goal and motivation for learning Python. I think at a minimum I would want to become comfortable with multithreading and using lists/tuples/dictionaries by the end of the semester.
