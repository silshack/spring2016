---
author: clairewlj
layout: post
title: "Lingjie's Web Dict Exercise"
---

Exercise:
<iframe src="https://trinket.io/embed/python3/d1af344d5d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection: I've spent some time thinking about why the data extracted is in those types: js is a dictionary, js['results'] is a list, and js['results][0] is a dictionary. I was confused that, now that the list js['result'] only had one element, why not just making it a dictionary? Then I saw the list of js['results'][0]['address_components'], where three keys with the same name "short_name" might exist. As a key in a dictionary should be distinct, we need to put those keys in different dictionaries, and put these dictionaries in a list to extract data we need precisely. That's what I think about most during this exercise.
