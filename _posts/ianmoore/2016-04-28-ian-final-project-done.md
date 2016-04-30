---
layout: post
author: touchwick
title: "Ian's Final Project"
--- 
This is my final project:
<iframe src="https://trinket.io/embed/python/175654b483" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Extending this project was more difficult than I initially had anticipated it being. My plan at first was to place the bulk of the game inside a ```while``` loop, forcing the program to check the status of the ```game_state``` variable whenever it wanted to restart the loop. Unfortunately, this proved difficult for a couple of different reasons. The first was the problem of trouble-shooting. A broken ```while``` loop is more than enough to bring my web browser crashing to a halt, making it difficult to tell what's going wrong. The second issue was the question of modularity. I found it difficult to efficiently build and test functions to fit inside the  ```while``` loop without making it incomprehensible to someone attempting to read the code. 

The solution to both these issue was, of course, to avoid the loop and use a ```go``` function, which Elliot suggested. Rebuilding my text adventure around this made it easy to test and refactor the game as I progressed. The ```go``` function lets the program know what it should do depending on the game state. This did not appear to work until I made my variables global. This is something I hadn't had to do before, so it was interesting to see how it worked and how it affected the implementation of my program. Looking back, I think using global variables might have been helpful in the past. I suspect that a couple of the programs for which I felt like my code was going through contortions would have benefitted from these, particularly my last game, which had far too much code stuffed into ```main.py```.

This was, as far as I'm concerned, at least, the biggest problem with my first game. There was little, if any, modularity. The program relied on a series of interconnected click functions that, because they were interconnect, had to be placed in an order opposite that in which they were called. The new game does not have this problem. I have one click function with conditionals for each game state. Having just the one click function lets it control the game state variable while keeping the actual game functionality within the ```go``` function. The ```go``` function checks in with the game state whenever it's done reacting to whatever it is the game needs to do. 

At first I had trouble preventing the ```go``` function from re-running each section of the game over and over and over again, but making the program turn a ```level_run``` variable ```False``` solved this. However, turning the ```level_run``` variable ```False``` complicated things later, when I had to implement a way for the game to restart. It took me a little too long to figure out that I could just turn everything ```True``` again in the final scenes. 

Restarting the game was a particular challenge. At first I had placed the animation of the owl picture in a ```while``` loop, the idea being that it would break if it detected that that the game had restarted. This did not work. The game would restart, sure, but the owl picture would continue to bounce around the screen regardless of what I tried. Ultimately, I settled on placing the owl in a ```for``` loop, which guarantees that it will end and disappear at a certain point. Once the owl has disappeared, the user has the option to restart the game with a key press. 

Having the owl finish a ```for``` loop creates another set of difficulties, though. Remember, the ```go``` function is checking for a change in game state. If the key press is to work, then the game state has to change back to what it was initially. If the game state changes and nothing is there to delay the ```go``` function, the game will start over as soon as it completes. In the end, the ```go``` function and I settled on a compromise. Once the owl completes its ```for``` loop, the player has a one-minute window in which he or she can press "A" and restart the game. ```time.sleep``` keeps the game from beginning again without specific input until the minute is up. At that point the user is informed that the game will restart in five seconds, and ```time.sleep``` holds off the restart again. After that, the game begins again with all the ```level_run``` variables reset to ```False```. It's not quite the smooth solution I was looking for, but! No one has to push the Run button now, right? The game actually restarts of its own volition, which is a clear improvement over last game, when there was just a castle at the end. 

A key component of my new version of this game is modularity. In this context, I think modularity means creating a set of functions that can be used interchangeably across the different game states. I have a function that allows me to create two options for a user to select and a separate function that allows for three options. The ```write_start``` function allows Jinglebell (the turtle who writes all of the game's text), while the ```list_write``` function incorporates ```write_start``` to build a function capable of using the lists from my dictionary to write not just one line, but  a whole scene.

The use of these and a few other functions means that unless a scene is an ending or the opening, the only differences between it and any of the others should be limited to which dictionary entries the functions use and which choices are presented at the conclusion of a given scene. This limits the amount of work needed to extend the game to modification of the click function and selection of the text to be written for the scene. With the basic functions written, this version of the game could be extended with relatively little effort, provided the text of the story is available. If you refer back to the previous game, you'll notice that this is absolutely, definitely, in no way the case. The previous version of the game require the creation of a separate click function for each scene, making it difficult to keep track of what was going on and what options needed to be implemented. The new version is much simpler.

I was worried before beginning this program that I would have forgotten some of the turtle functions and how to build the game. I am pleased, therefore, to note that this process was nowhere near as difficult as I thought it would be. I had some struggles along the way, but being able to build upon and refine a program I already had going made the whole thing much, much easier than I had expected it to be. In some ways this is representative of the back half of the semester as a whole. As we moved into the more complicated material and as we began dealing with data, I expected that I would have a lot more trouble with the work. It was a comfort and a surprise that for the most part everything felt like a very natural extension of the material we worked on during the first couple of months. (JSON was a real bear, though. Getting used to another data structure is tricky.)

I also wanted to reflect on the syntax and structure of a few different things. For instance, I now know that instead of writing:
```
level_run1 = False
level_run2 = False
```
and so on, I could instead write:
```
level_run1, level_run2, level_run3, level_run4 = (False,)*4
```
The latter is more concise, requiring less effort on the my part and taking up less space within my code. Something similar happens when making different things global. Instead of writing:
```
global grumpy_owl
global level_run1
global level_run2
global game_state
```
and so on, I can instead write:
```
global grumpy_owl, level_run1, level_run2, game_state
```

To be honest, this weirds me out. I understand that in spoken and written language I can do different things in multiple ways. Contractions and synonyms aren't things we do just for fun, after all. Regardless, it's a little unnerving to discover that one line of code can do what I thought would have taken quite a few. It's a good lesson to get right at the end of the course, I think. I definitely have a lot left to learn and it's worth putting in the time to learn it. After all <i>who wants to write ```global``` a couple dozen times</i>.
