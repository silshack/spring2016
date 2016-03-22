---
layout: post
author: elliott
categories:
  - exercise
title: "Clone and run our class website"
inclass: true
---


From Cloud 9:

```
git clone https://github.com/silshack/spring2016.git
```

(unless you set up SSH, in which case you should pick the SSH url from our class repo)

```
# Change into the new directory
cd spring 2016

# Install stuff
bunde install

# Start Jekyll (the port and host stuff is Cloud 9 specific)
jekyll serve --watch --port=$PORT --host=$IP
```