---
layout: post
author: nataliele
title: "Natalie's turtle poetry slam"
---

So I'm not sure if users are supposed to just enter words or they can enter phrases. If they're supposed to just enter words, I need to change their series of words into a list of words. I could split the words after I have append all of them to the list or I could split the words first as they're entered and then append them. The problem with the first one is split function only splits strings and not lists. The problem with the second one is that Python will then give me a list in a list, which is still not what I wanted.

So for this version I went ahead and assume that Tina will take phrases and not individual words for each entry.

while True:
  userinput=input(prompt)
  if userinput=="done" or userinput=="Done" or userinput=="DONE":
    break
  userwords=userinput.split()
  wordlist.append(userwords)

<iframe src="https://trinket.io/embed/python/1c51564c33" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
