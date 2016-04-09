---
layout: post
author: hannahlwang
title: "Hannah's Web Dictionary Exercise"
---

<iframe src="https://trinket.io/embed/python3/862824f185" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I really enjoyed learning about how Python can read XML and JSON. I thought it was especially interesting that JSON actually takes its syntax from Python dictionaries, which makes it incredibly easy to read and mess with in Python. I decided to have my program print the location type(s), which required forming a loop, in case there was more than one location type (as there is for "Atlantic Ocean"). I also decided to have my program print the county of the location, if applicable. This was a little tricky, because the county information is not always located in the same place, so I couldn't just use one index. I <em>probably</em> could have used a regex to search for "administrative_area_level_2" in "types", then printed out the long name from this, but instead I just decided to copy and paste a couple of conditionals that covered the different indices where it could be located, which works just fine.
