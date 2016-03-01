--- 
layout: post
author: wfh1972
title: "Wayne Homan's Corrected Clicky Turtle Post"
---


<iframe src="https://trinket.io/embed/python/1330cefbf6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I had major problems debugging this code. For some reason I kept messing code up that I had already written and was working fine. By
the time I was done I would have a great big mess of spaghetti code. Things I learned:

1) When I am progressing along and I get a section done that works then save the completed code as a duplicate in trinket.
2) Don't be excited that I got something right in the code and then rush on without documenting the code. It makes it much harder
to reconstruct if I have to redo a portion.
3) Don't trouble shoot code by cutting-and-pasting sections of code. I ended up erasing my code twice (don't ask me how I ended 
up doing that) which led to me having to redo all of the coding up to that point. Instead use the shift-arrows to select and 
control-/ keys to make them comments. This means that I will never be in danger of losing the code I have cut-and-pasted.

Onto the program itself:

I based my program on the running theme of tina, tommy and if she loves steve or tommy. In the beginning I set up tommy (blue turtle) to 
be closely following tina (red turtle). The setup screen function gave me grass. When the user clicks the screen they are prompted to
answer: "does tina love tommy?". If yes then tina moves to the place where the screen click happened and tommy follows her. If no, then
tina moves to the place where the screen was clicked and tommy moves to the opposite coordinates (e.g. tina moves to 100,50; tommy moves
to -100, -50). Thats about all there is to the program.

