---
author: clairewlj
layout: post
title: "Lingjie's First Meetup"
---

On April 17th I attended People programming hosted by Triangle Hacker Hours. There was no specific theme for the meetup, people who wanted to attend it just needed to bring a laptop and code something, get help with something you're working on, offer help to someone who's trying to become a better programmer, or just chat about technologies you're working with. 

I went there with my friends, and we met someone discussing about their projects using JavaScript. Then we happened to meet some of our classmates in this course and we sat together and focused on our own python projects. Basically we talked about our final projects - how to correctly import and open/read csv files, how to print out information correctly, etc. With the James's help, I figured out the problem of .readlines() used in Cloud9, which was about the correct switch of python 2 to python 3, and learned more about the structure of data after it was read. I also tried some codes from the first chapter of Data Science from Scratch First Principles with Python, and learned that I could use two 'indexes'(item?) in one loop:
for i, j in friendships:
    users[i]["friends"].append(j)
    users[j]["friends"].append(i)
and also how to sort multiples using the sorted function:
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
print(sorted(friendships,key=lambda user:(user[1],user[0]),reverse=True))

From this experience I think meetups are helpful to quickly get help about some details we're stuck on, and I'd love to attend more to learn something new.
