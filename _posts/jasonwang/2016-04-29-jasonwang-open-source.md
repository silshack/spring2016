---
layout: post
author: wagerpascal
title: "Jason's Open Source Contribution"
---

To be honest, it was pretty tough to find an open source project that fit my interests, was mainly in python, and was overall easy enough for me to understand.

I took a peek through the Github trending open source projects (under the Python listing) and kept reading through (maybe 15-20 different projects) until I found https://github.com/YongHaoWu/NeteaseCloudMusicFlac . It was a pretty simple program, which only required the one python file to crawl through Baidu music players and downloading the resulting FLAC file from the site. Pretty cool small project, and I was really glad that I’m semi-literate in Chinese to the point that I understood the gist of what the guy wrote. I found the TODO list on the main page, and read through it (Rough translation here for convenience).

1. Reorganize into PEP8 format.
2. The program currently matches the song name, but it would be better to also match artist name.
3. The success rate isn’t very high, and could consider going to other websites to scrape.
4. Automatically delete song files that are under 10 Mb.

I tried to look through the PEP8 Format page but found that as far as I can tell, he mainly followed it. However, I looked through the OS library that he imported, and found a getsize() method that may fit what he was looking for. I also found a StackExchange thread that also supports my theory. http://stackoverflow.com/questions/8626325/most-efficient-way-to-delete-a-file-if-its-below-a-certain-size

I made a pull request to his repository that added the functionality so that he can see. As I’m writing this, apparently someone (not the original author) made a comment on my pull request. I’ll have to follow up on it later, but it looks like it is networking related with HTTP headers? https://github.com/YongHaoWu/NeteaseCloudMusicFlac/pull/2

I tried to run his file within Cloud 9, but I ran into an issue involving the JSON or UTF formatting of the page. I tried looking into the error code that I got, but I came out more confused than I entered the issue. So, I opened an issue on his repo as well. https://github.com/YongHaoWu/NeteaseCloudMusicFlac/issues/1

It was kind of fun to look for a project that would fit my interests, and trying to understand and get it to work. I’ve never really had any interest in open source projects before, so it was interesting to get a peek of the general landscape (at least on Github). Unfortunately it seems that my knowledge of coding languages is narrow, as most of the projects are in Java, Ruby, PHP, or Go (up and coming language? Might be fun to get into). The language challenge was also kind of fun- I used to go onto Baidu as a kid to download music as they had an mp3 download feature (and I believe they got into trouble with American companies because of it), and it was a much needed exercise in my already rusty Chinese. Anyways, it is pretty cool to interact with people on the other side of the world for a common goal.

I already came into the assignment thinking that I most likely would just change something regarding documentation, but it was a pretty rewarding (and mildly surprising) event to find that I could actually present input that may help the project in the future.
