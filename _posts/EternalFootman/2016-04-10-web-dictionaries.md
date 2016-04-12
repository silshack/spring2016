---
layout: post
author: EternalFootman
title: "Kit's Web Dictionary Exercise"
---

<iframe src="https://trinket.io/embed/python3/c4733e6d93" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It took me a while to figure out what this program was actually doing; I spent some time going through each 'print' command and finding its corresponding result. After I understood the process, the program became delightful; finding what it did with ambiguous input was, I think, the most entertaining use ('Anarctic' gives a result in Marrakesh, while 'Antarctica' gets the continent; Ellesmere Island is apparently unorganized).
I had no traceback issues because I chose data that were present in all of the locations that I tried (there were many, but the requested information is very generic). However, had there been an error, I would have used a try/except loop in the printing section of the code. For each input, it would try to find the information but would move on to the next print command if it weren't there.
