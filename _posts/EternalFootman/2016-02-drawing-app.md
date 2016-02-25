+---
+layout: post
+author: EternalFootman
+title: "Kit's Drawing App"
+---
+
+<iframe src="https://trinket.io/embed/python/9e2395502d?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
+
+Updated milestones:
+
+- [x] Setup screen (question and buttons)
+- [x] Functions module
+- [x] Define turtles (gardener, referee, timer, hedgehog)
+- [x] Normal croquet mode (move hedgehog to numbered wickets in order and spacing as in an ordinary game)
+- [x] Wonderland mode (freestyle drawing with randomly colored lines and surprise stamps)
+- [x] Transition easily between modes
+- [x] Reset mode from within
+- [x] Have hedgehog path stay on screen to create abstract art
+- [x] Add comments for context
+
+This is the next installment in my series of Alice in Wonderland programs. It is vaguely inspired by the mad croquet game at the end of the book. For the first mode, I modeled the screen after a standard croquet setup. If one follows the numbered hoops, the effect is that of a connect-the-dots game resulting in a roughly symmetrical hourglass shape. Alternately, one may ignore the numbers and draw freehand, but the color, shape, and line thickness never change. I find this mode simple and satisfying. The second mode does not really follow the rules of Lewis Carroll’s game save that there are no set goals or end time, but making it more accurate would have turned it into a game rather than a drawing app. I enjoy creating little colonies of shapes in the corners.
+
+The drawing sections were fairly straightforward (though the code went through several incarnations, becoming gradually more efficient. For example, the hoop function did not originally exist and the place_hoops one was much longer. Credit for the idea goes to Natalie; she mentioned it in our peer clinic). Transitioning, however took rather a lot of trial and error. Eventually I got all of the resets and clears in the right places, but I’m still not completely satisfied with the organization of the code. It runs well, and I’ve cleaned it up as much as possible, but I feel (possibly irrationally) like the functions should be separated into clearer modules. Every time I tried (which was at least several and possibly many), the transitions stopped working properly. Eventually, I settled on the functionality you see before you. Perhaps when I have more experience, I’ll go back and refactor it.
+
+The general concept remained the same, but my specific milestone goals adjusted a good deal. I didn’t mention the opening screen or the rules screens, and those turned out to be complicated and important. I eliminated the moving hoops from the Wonderland mode because they did not add to the drawing part of the app (and they would have been complicated to design). Similarly, incorporating an ending fits a game better than a drawing app.
