---
author: wookiemage
layout: post
title: "Colin's Final App"
---
  [Here's my repo](https://github.com/wookiemage/inls560-final-app)
  
## Let’s talk about what my app does:

My app allows a user to choose one of three sets of premade data or import their own set of data. It then presents the user with 7 different ways to look at the data. Most of these functions present the data both as a number and a rudimentary visualization. The data set that this program is meant to analyze is a form of sales data automatically generated from [Mockaroo]( http://mockaroo.com/). I chose randomly generated data because I could choose the data types and content very specifically so that I would have the chance to try a lot of different techniques on the data. My data includes, names, emails, ip address, gender, referrer domain, and two different dollar amounts. This gives me lots of different options as far as what to analyze.
	
## Ambition Vs. Reality

When I started this project, I wanted to do some pretty remarkable things. I had some very ambitious milestones:
	
- [ ] Create a function that passes IP address to the google geolocation api
- [ ] Create a function that can retrieve a map link and pass that link to the bit.ly api
- [ ] Create a function that allows the user to launch a browser at that link
 

Turns out, some of that is not possible. For example, I could not find a way to take geolocation data from an IP address and turn it into a map. I could, and did, find an api that would guess the location of an IP address and I did put that into my code, but I didn’t find a way to query that API and get the kind of data I needed to plug into a google map api. [The documentation]( https://developers.google.com/maps/tutorials/data/importing_data) that I read said that I needed a specific data format called GeoJSON which I was unable to find an API to export. If I had found this data, then I could have created a file that held this data and uploaded it to a google map. I could have then taken that link and plugged it into the bit.ly API and gotten a shorter link. That would not have been hard. What would have been impossible, it turns out (at least in cloud9) would be to trigger the launch of a web browser at that link. I was able to launch Python’s built in text based browser at target addresses, but it doesn’t render google maps. Having investigated and abandoned those overly ambitious goals, I decided on a new one.

- [ ] Create a function that saves the data the user requests into a dictionary file.

Which is so much more possible. From what we’ve read in the textbook and additionally in Automate the Boring Stuff, this seemed like a good goal to set. Unfortunately, life gets in the way of ambitious plans. I spent nine hours working on this project on Friday last week. I spent a combined total of four more on Saturday and Sunday. I think that’s about all I have to give. Between the end of the semester, with all the other projects and papers due, and my son’s new habit of not sleeping from 4:00 AM to 6:00 AM, I just don’t have more time to devote to this project. I would like to say, though, that I wake up at night thinking about ways to implement this feature. I think I would build it by creating an integer variable that increases every time that a user tells it to store data. I would also create a new string variable that housed the information that the user asks to store. I would do this by creating a base name for the string variable and concatenating the current number from the counter onto it, to create a new variable name. Then, when the user wants to save and export the data, I would have the program open a file, and write each of those strings to the file and then save and close it. I just wish I had the time to work through this. Tempus Fugit.

## Looking ahead

A number of us in this class want to keep going. We’ve made a lot of progress in this class but feel there is still so much we don’t understand. As far as we know, there is no second level python class, so we are looking for other ways to go forward. One such option is INLS 690-224 Visual Analytics; another one is INLS 690-163W Information Analytics. Both these courses rely on a good understanding of programming and will likely help push us further. I’m looking forward to taking these skills that we’ve garnered in this class and applying them to bigger data sets to create good analytics and visualizations.

Personally, I intend to go back to [my open source contribution](https://code.alephobjects.com/T426,) and actually write the gcode needed to make the printer behave the way I want it to. I’ll test out my modification and upload to the community my results. I hope that it will work, but I’m assuming (perhaps wrongly) that if the solution were this simple someone would have already implemented it. We’ll see.

Over the summer, I hope to think of a few programming projects to keep going. I’m going to be involved with a new project at work that I hope will leverage some of these skills. The library is completely revamping how it uses Google Analytics. We will be adding and removing javascript tags on just about every page on the library’s website. We will be working with a contractor who will help us organize our data. We are also seeking to integrate (Google Tag Manager)[https://www.google.com/analytics/tag-manager/] which has an extensive API that interfaces through Python. Hopefully, I’ll be able to make some scripts that automate this process.

## Resources I’ve found

I’ve found a lot of useful resources throughout this semester. Here are some for regexs:
[pyregex]( http://www.pyregex.com/) This site is really useful for developing and testing a regex. It allows you to paste in your sample text and enter some regex. It will highlight any matches dynamically. Lots of sites do this; what makes this site special is the below cheat sheet.

[Regex Crossword](https://regexcrossword.com/) Here’s one that I don’t understand at all. The goal is to take the obscurity of regexs and turn it into a game. There are lots of levels that use different features of regexs. It really tests your knowledge.

Some Community Resources:

[Learn Python Reddit](https://www.reddit.com/r/learnpython/) This subreddit has over 50k subscribers of differing ability in Python who all have the same goal, to help others learn python. While I haven’t posted any questions to this subreddit, I have read a lot of great questions and explanations there. As with any subreddit, you get the bad with the good, so sometimes you see very terse answers with little explanation, but generally those get downvoted and nice verbose answers get upvoted. 

Another great feature of this community is our next resource:

[The Learn Python Subreddit Wiki](https://www.reddit.com/r/learnpython/wiki/index) This is a long list of community resources generated and maintained by the learnpython group. It has lots of different categories of resources, everything from video tutorials, to explanations of the differences between python 2 and 3. This is a good place to turn when google fails you, or you want some curated resources.

## A Semester in review

I’ve really learned a lot in this course. While I had some programming knowledge before we started, which was very helpful, I’ve really built up my skills this semester. Using turtle to work through flow of control and as a simple graphical user interface was a good scaffold. I am glad we had the chance to get our grounding in something a little less intimidating that the command line. I’m also glad we had the chance to progress on the command line and learn how to use a web based IDE. Similarly, building skills in github was very good practice for the future. I have a much better understanding of how a tool like github can help remote teams collaborate or even just manage version control for local teams.

One thing that I would like would be a list of further resources and project ideas to continue to push ourselves further. I feel like a have a good grasp of the basics of python, but I’m not really sure where to go next. I know this is a common feeling among new programmers, as there are lots and lots of threads about this exact topic on the learn python subreddit. The answer always seems to be a variation of “keep going” or “make something for yourself.” I think a lot of people find this answer unsatisfying. Maybe we can make some sort of list of project ideas as a community effort. Or, more likely, such a thing already exists and I haven’t run into it yet. In fact, one small google search later, I found [this](https://www.reddit.com/r/dailyprogrammer). I haven’t had a chance to assess whether these challenges are appropriate, but they're a place to start.
