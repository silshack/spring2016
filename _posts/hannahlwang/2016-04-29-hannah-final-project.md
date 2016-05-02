---
layout: post
author: hannahlwang
title: "Hannah's Final Project"
---

Link to my Github repo: https://github.com/hannahlwang/inls560-finalproject

For my final project, I chose to create a data analysis application that analyzes data exports from the Carolina Digital Repository. These data exports can be downloaded through the administrative interface in the CDR, and they contain information about all the objects in a collection. I had to first run this project by my supervisor, since these data exports are not available to the general public. He said that it was fine (and a great use of the data exports!), as long as I only used exports from collections that are publicly available. The three collections I chose were: UNC Scholarly Publications, Art MFA Theses, and SILS Masters Papers.

<h3>Cloud9 and Github</h3>

The first task I set for myself was to set up a Cloud9 workspace and Github repository. I wanted practice using a full IDE, just in case I want to use one to code in the future. Thanks to the Cloud9 and Github documentation, provided by both Elliott and the web services, it was fairly simple to set up my Cloud9 environment and connect to my new Github repo. I found that I really enjoyed working in Cloud9, and using git to push my changes.

<h3>Reading My Files</h3>

Concurrent with setting up my Github repo, I wrote some starter code to read my CSV files. At first, I started using CSV files, because that is the default export format from the CDR. However, I ran into a major problem using this format: the commas with Title or Label names were being read as delimiting commas by my program. Luckily, this was an easy fix: I just converted the files to tab-delimited value files in Excel before uploading them to Cloud9. This also gave me some insight into the constant struggles of the developers in the CDR to debug their code -- they must run into issues with commas and other punctuation all the time! I also ended up importing the Python CSV module to read my files. For whatever reason, a simple ```.readlines()``` wouldn't work with my txt files, but using ```csv.reader()``` worked great.

After I was able to read my files, I ran into some issues with the data itself. Not all lines were in the expected format (some were blank, some were repeated parts of other lines). I also didn't want to include the first row, which just contained the column headers. I solved this by using a regex solution that I used in <a href="http://silshack.github.io/spring2016/hannah-MOAR-dictionary-exercises.html">this exercise</a>, where I only added lines to a list (or table) that began with a certain value. In this case, I wanted any line that began with "File", "Folder", "Aggregate", or "Collection" (the four different possible object types).

<h3>Basic Info</h3>

I started by writing code to print out some basic information about the files. I wanted the user to be able to learn information about entire data files -- statistics about object types, file size, etc. I decided on these types of statistics because these are real use cases in the CDR -- the repository might want to know the most frequent MIME type, so that we know what file formats to invest in supporting. Or the repository librarian might want to know the average file size being deposited into a collection, in order to budget data storage and make projections about future deposits. 

At first, I thought that I would make a ```makedict()``` function, that would make a dictionary of values for any column, depending on the index. While this turned out to be useful to wrap my head around the kind of counter dictionary I wanted to create, it turned out to not be that useful -- I wanted to gather different types of data about the different columns, and I ended up writing a separate function for each dictionary. Even though I didn't ultimately use it in my code, this first ```makedict()``` function was important to my process, because I remembered how functions work, and learned how to use them to make dictionaries. I ended up using counting dictionaries for object types and MIME types, storing each type as a key and each number as a value.

I also wanted the user to be able to search for an object by its PID. Again, this was based on a real use case -- repository staff might receive an inquiry about a particular item, and they would look it up using its PID. The file titles and labels are generally useless in this case, because the depositor is free to choose their own names, and they are often not unique. I accomplished this by making a dictionary of dictionaries, where each PID (from one of the file columns) is the key for a dictionary, and all the rest of the column entries are stored as the value. Within this value, each column entry is stored as a key-value pair, with the column name as key and the column entry as value. I am really glad that I approached this problem in this way, rather than creating lists, because until doing it for this project, I never really understood the whole "dictionary of dictionaries" concept. I think that I needed to use it to solve my own problem to actually concretize the concept in my head.

<h3>Menu Structure</h3>

I had put it off long enough -- it was time to decide what to put in my menus, and how to structure them. In retrospect, I wish I had mapped it out on paper in a tree structure. That would have saved me a lot of time. Instead, I used trial and error to create a structure and menu options that made sense. Ultimately, I created four menus:

- File Menu
- Main Menu
- Data Summary Menu
- PID Menu
- Final Menu

Here's what the flow looks like mapped out:

<div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://www.lucidchart.com/documents/embeddedchart/70b0a15b-f84e-4aba-aa1b-458425536c79" id="mSqc3Ixokj5N"></iframe></div>

<h3>Making everything look nice</h3>

At this point, I had most of the information I wanted in dictionaries, but they were unformatted and didn't have any visualizations. For the PID information option, I ended up using <a href="http://ils.unc.edu/~eah13/textbook/09-dictionaries.html#looping-and-dictionaries">this method described by Dr Chuck</a> to make a list of the keys, sort them into alphabetical order, and print them, one on each line.

I knew that I wanted to use histograms to visualize the information about object types and MIME types. Using a for loop, I was able to print out each key for the dictionary on a separate line, followed by a string of asterisks corresponding to the value. Since some of the object types number in the thousands, I settled on dividing each value by 50 (using ```//``` instead of ```/```), and printing out that number of asterisks. Although the number of asterisks does not correspond to the number of objects, they visually represent that number. Unfortunately, reducing each value meant that some values do not register at all on the histogram. Because of this, I printed out a key below each histogram, that shows the abbreviation, what it stands for, and the number of objects associated with it. I accomplished this by adding another for loop, the results of which print below the histogram.

At this point, I also added the code to make a list of file sizes. This ended up being incredibly simple (especially after all that messy dictionary work), and I was able to calculate maximum, minimum, and average file size all using the same list.

<h3>Regex struggles</h3>

I used regexes in a few places in my program, and didn't have many problems with them (for example, using a regex to search for only the lines that began with "File", "Aggregate", "Collection", or "Folder"), but my MIME type visualization caused some major struggles. For the object and MIME type visualizations, I wanted to print out abbreviated labels, mostly to make the spacing consistent, so that the histograms would line up. For object types, this wasn't too difficult -- I just used string slicing to only print the first 3 letters of each label. For MIME types, it was a little more difficult. The way that MIME types are written, the top level type name goes before the slash, and the sub-type name goes after the slash. I really wanted to print out the part AFTER the slash, because it would be more meaningful to have two MIME types in the visualization labeled "xml" and "msw", rather than having them both labeled as "text". It took a very long time to figure out the right regex to use -- I did a lot of testing on regexr.com. This is what ended up working:

```
re.findall('[/]([a-z0-9][a-z0-9][a-z0-9])',mime_type)
```

After I solved this problem, some MIME types were still printing out blank. I realized that some had hyphens in them! So my new regex was:

```
re.findall('[/]([a-z0-9-][a-z0-9-][a-z0-9-])',mime_type)
```

After I solved THAT problem, some MIME types STILL weren't printing out correctly. In one case, the MIME type was not specified (I think that this was mostly folders, which don't have a MIME type). The other problem case was a MIME type labeled "$mimeResolver.getContentTypeFor($file.name)". I don't think that this is technically a MIME type, but I wanted to register it, because quite a few files had that in the MIME type field. It wasn't registering with the current regex, because it didn't have a slash in the name. Luckily, I was able to do a pretty simple conditional statement, which printed "N/A" if the MIME type wasn't specified, and printed "$mi" if it was that weird outlier.

<h3>Bad input</h3>

Up until this point, I hadn't implemented any of the while loops you see in my final code. My programs have always been pretty weak in dealing with bad input, so I kind of put off that part until the end. However, like creating a dictionary of dictionaries, problem solving to complete this assignment made me finally wrap my head around a difficult concept!

Essentially, I realized that I would have to make a ```while True:``` loop for every menu. If the user entered the correct input, the loop would ```break```. Until then, the program would loop through the menu. This turned out to be relatively simple for the latter three menus, because the user's only valid options are numbers. It got a little more complicated with choosing files...

<h3>Letting the user choose the file</h3>

My first issue was in where to put my first menu, which would let the user select a file. All the rest of my menus were in the main.py module, but my code to read the file and perform all the functions dependent on that was in the helpers.py module. I wanted to be able to put that first menu in with the rest of my menus on the main.py module, so that I would be able to loop through all of them, but out of necessity I ended up putting my file menu in the helpers.py module.

At first, I only gave the user the option to choose one of three files, which just required a ```while True:``` loop like the other ones. But then I added the option to enter a different data file. There were two different types of bad input I had to deal with here: 1) the user entering an invalid file name (e.g "sdfjskdflj"), and 2) the user entering the wrong type of file. I dealt with the first problem by using a regex to determine if the user-entered file ended in ".txt". For the second problem, I made a list of the column headers that comprise the first row of each valid file. Then I made another list in the initial read function that includes all lines, not just those beginning with valid object types. And so, I made another ```while True:``` loop that ends with this:

```
if file_table[0] == ['Object Type', 'PID', 'Title', 'Path', 'Label', 'Depth', 'Deleted', 'Date Added', 'Date Updated', 'MIME Type', 'Checksum', 'File Size (bytes)', 'Number of Children'] :
        break
```

And that dealt with the other type of bad input! You can test it by using the invalidfile.txt in my Github repo.

<h3>Final thoughts</h3>

I am really happy with my finished product. I think that it really demonstrates how much I have learned in the class, and it gave me a chance to get really comfortable with dictionaries and regex. I realized when making the ```file_table``` list in the section above that things like making lists, parsing them, and looping through them are all second nature for me now. I think that if I had more time, I might have messed with matplotlib, but I am actually really happy with how my histograms look. All in all, I'd rate this a success!
