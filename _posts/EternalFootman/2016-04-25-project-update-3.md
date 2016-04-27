---
layout: post
author: EternalFootman
title: "Kit's Project Update"
---

<iframe src="https://trinket.io/embed/python/3e833b92a7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

(Updated 4/27 to be a copy and not the original.)

I have the individual sections working, but the transition between them is (as anticipated) more complicated. I tried a great while loop first, but it has trouble with the Croquet section because that one has no set ending (players just stop when bored). The count updated and the next section of the loop ran on top of the game, so that was not usable. Now I've moved on to a menu that comes up between the games; this allows users to pick a section at will, which I rather like. The problem now is that I'm not sure how to limit the click function to the menu; it runs beautifully until you click on the screen during a game, but then it runs whatever command the menu connects with that location. Apart from that, everything is working well enough.

**Milestones:**

Done:

- [x] Refactor Daisies
- [x] Refactor Croquet
- [x] Refactor Yarn
- [x] Refactor Garden
- [x] Refactor Chessboard
- [x] Convert print to graphic in Garden
- [x] Convert print to graphic in Daisies
- [x] Write start screen. Not menu (games will be chronological) *-This was done but the purpose has now changed to a menu, which is also done.*
- [x] Add custom images, probably transitional screens *-These are drawings from the original book.*
- [x] Write transition between first two games
- [x] Apply transition to other games *-These last two are now the same menu as the start screen*

To do:

- [ ] Set moves in Chessboard
- [ ] Go through all games to make sure all turtle names are consistent (Alice for actions, Gardener for setup, etc.) *-This is actually no longer relevant, as each game is in a separate module*
- [ ] Incorporate help dialogue
- [ ] Write end screen. Nothing so unambiguous as winning. There will be an imported image of a crown.
- [ ] Include restart option in end screen
- [ ] Have chess game play from the end screen at the user's discretion *-New*
- [ ] Isolate click function in menu *-New*

**Stretch Goals:**

- [ ] Add new section – Walrus and Carpenter quiz *-I won't have time for this, which is sad*
- [ ] Incorporate chessboard into transition screens to show progress *-This no longer makes sense with the format of the game*
