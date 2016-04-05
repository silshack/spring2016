---
author: wookiemage
layout: post
title: "Colin's Tetris Refactor"
---
## Here's my refactor:
<iframe src="https://trinket.io/embed/python/e956c64129" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Here's my thinking:
Right off I saw that we should move the turtles away from the main.py page. Or rather, I thought that we could move them in order to make that page a little more readable.
So I set about pulling each turtle into it's own module. This is easier to read and modify because each one is separate and easily changed without effecting the others. While doing this I noticed that one turtle in particular behaved differently from the others. Most of the turtles drew static elements once at the beginning of the program, but one of them continually draws the screen.
Seeing this logical distinction, I created a new module that sets up the screen and draws the static elements and another that draws the dynamic elements.
While pulling these out, at first I was putting each variable into whichever module needed it, but the I figured I should put all of them in a different module so that they could be found easily and altered. And then I imported them from that module into the others. That way, there's only one place to change a variable and I don't have to worry about them getting mixed up.
  
Finally, I left these elements on the main page:

```
disp = turtle.Screen()
disp.tracer(1000)

#This draws the static elements of the gameboy
setupScreen()

disp.onkey(moveLeft, "Left")
disp.onkey(moveRight, "Right")
disp.onkey(moveDown, "Down")
disp.listen()

while True:
    draw_screen()
    draw_grid()
    draw_piece(piece, piece_x, piece_y)
    time.sleep(delay)

    piece_y -= 1
    if piece_y - piece_h < 0:
        piece_y = 22
        piece = random.choice(list(pieces))
        piece_h = len(pieces[piece].split("\n"))
        
    disp.update()

    
disp.exitonclick()
```

I left these here mostly because they contained the loop that would run continuously and the disp. elements that I couldn't figure out how to call to all the needed modules, so intead I called the modules here where it was already established.
