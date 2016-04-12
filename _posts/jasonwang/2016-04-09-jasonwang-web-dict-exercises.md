---
layout: post
author: wagerpascal
title: "Jason's Web Dictionary Exercise"
---

<iframe src="https://trinket.io/embed/python3/d7904dfb55" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Thoughts:
This was one of the more interesting assignments that we've done. It was useful to know that we can treat the JSON results similarly to calling list indices and dictionaries, which makes the whole process easy to understand.
It's intersting that the API data is formatted in this particular method (especially with each entity's type (from top to bottom) listed). It makes me curious if someone has needed to use every single bit of data from the API.

To cover for the general issue of data not existing for non-political entities (ex. bodies of water), I put the relevant political entity information in a try/except case to avoid an error occurring.
Since each location has a set latitude/longitude, it is still displayed for each entity.
