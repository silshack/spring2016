---
layout: post
author: elliott
categories: 
 - how-to
 - exercise
inclass: true
title: Github basics
date: 2016-01-14 11:58pm
---

# Can I Get A Volunteer?

* Create Github account
* Go to [http://github.com/silshack/spring2016]
* Create a new post with the filename `_posts/<yourname>/2015-01-12-<yourname>-first-post.md` **Remember the importance of careful typing**
* Add this to the top of it:

```
--- 
layout: post
author: <yourgithubname>
title: "Yourname's first post!"
---
```

**Remember, every character matters to a computer.**

* Then, underneath, write a bit about yourself.
* Write a commit message at the bottom of the github page describing what you did, like "Added Elliott's first post"
* Commit directly to the gh-pages branch
* Check it out on <yourname>.github.io/spring2016.  If you don't see your post, make sure you've committed to the gh-pages branch (that's what triggers the website getting created)
* Look good? Create Pull Request.  Or edit again if something's wrong.
* :+1: :sunglasses: :fire:


# Automated Tests

We use Travis-CI to automatically run tests on code.  When you submit a pull request, you'll see something like this:
![]({{ site.baseurl }}/img/travis1.png)

Behind the scenes it's building a whole new server and running various tests to make sure your code won't break the site.  You'll want to make sure your code passes these tests, after which you'll see a shiny green check mark next to your pull request.  The test status is also visible in the list of pull requests:

![]({{ site.baseurl }}/img/travis2.png)

If your build fails, don't panic!  It happens to the best of us.  Click 'Details' and see if you can figure out what went wrong.

Also, remember that passing tests is a minimum standard.  It doesn't mean that your code is perfect, so make sure to read over your code carefully.