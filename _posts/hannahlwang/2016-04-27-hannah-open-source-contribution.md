---
layout: post
author: hannahlwang
title: "Hannah's Open Source Contribution"
---

For my open source contribution, I did some testing for WebRecorder (https://webrecorder.io/), which is a web archiving tool built by Rhizome. WebRecorder is still in a beta prototype stage, so you have to request an invitation to register right now. For my systems analysis project, we were looking at the UNC Libraries web archiving system, so WebRecorder had come up in our lit review as a recently developed tool to easily create high-fidelity archived files, using the WARC format.

Archiving social media is always difficult for web archiving tools (Archive-It, the most popular tool on the market, does a terrible job), so I wanted to see how WebRecorder would do with Twitter. It did fine for archiving a whole Twitter feed, but when I clicked on individual tweets, it would "record" a JSON file, rather than the whole webpage. WebRecorder is open source on Github, so I opened an issue, which is here: https://github.com/webrecorder/webrecorder/issues/78

I described the issue, and walked through to steps to recreate it. Before submitting this issue, I tried to archive tweets on several different pages, to make sure that I could replicate it.

Overall, I would say that this was a rewarding experience. I got to investigate a tool that I'm genuinely curious about, and hopefully the team will be able to take my input and improve the project! I am also planning on submitting a couple more issues related to the UI, which has some confusing elements.
