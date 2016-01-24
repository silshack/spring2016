---
layout: post
author: nataliele
title: "Natalie's treasure exercise"
---

This is my treasure hunt exercise:
<iframe src="https://trinket.io/embed/python/06b21bdfcb" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I think the biggest decision that I had to make was whether to give the user feedback on each coordinate or just a general one for both. I decided that it's simpler to give a general feedback. Otherwise it'll be too many ifs. Maybe other people have some other way to approach it.

For the feedback I had some concern about semantics: I tell users they're between so and so pixels from the treasure. But actually the operators are  not the same.
0   5      50      100
   ](      )[      ](
So "between 5 and 50" doesnt include 5 or 50 but "between 50 and 100" does include 50 and 100. I dont know how to make everything standard.

I got rid of user_has_won and just use still_doing because I think the two convey the same information.

I was also able to handle bad input to let user keep playing instead of restarting.

I wanted to make Tina go to the treasure so I thought of adding treasure picture as shape for Tina but not sure how to. Also couldnt change the size of Tina to be bigger. So I ended up just print the treasure coordinates out.
