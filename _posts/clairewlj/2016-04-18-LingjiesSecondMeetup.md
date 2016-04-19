---
author: clairewlj
layout: post
title: "Lingjie's Second Meetup"
---

On April 18th I attended Durham Project Night hosted by Tripython. As it was again a free meetup with no specific speackers, it was like the one I attended on April 17th. I went there with my friends, and basically we were working on our final projects. I was completing some miletones planned, and also kept doing practice from the first chapter of Data Science from Scratch First Principles with Python, and learned some new things. For example, I've learned the function of all, which is a built in function to return True if all elements of the iterable are true/empty. Also, I found that the function of Counter from collections was quite efficient for counting things in list and dictionaries. Moreover, I learned some interesting way of writing code, and I'm not sure which way is more efficient in the meaning of practical application, which is quite important especially when the size of dataset is really large.

The code I learned was below:
def friends_of_friends_ids(user):
    return Counter(users[foaf]["id"]
                   for friend in users[user]["friends"] # for each of my friends
                   for foaf in users[friend]["friends"] # count *their* friends
                   if not_the_same(user,foaf) # who aren't me
                   and not_friends(user,foaf)) # and aren't my friends
                   
Generally, I still did not discuss with others much in the meetups, and I think I'll need to share more in the future. Anyway, working surrounded by like minded Python lovers is a pretty good experience.
