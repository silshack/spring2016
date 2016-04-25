Here are the major issues I ran into, and how I resolved them:

####Regex struggles

I used regexes in a few places in my program, and didn't have many problems with them (for example, using a regex to search for only the lines that began with "File", "Aggregate", "Collection", or "Folder"), but my MIME type visualization caused some major struggles. For the object and MIME type visualizations, I wanted to print out abbreviated labels, mostly to make the spacing consistent, so that the histograms would line up. For object types, this wasn't too difficult -- I just used string slicing to only print the first 3 letters of each label. For MIME types, it was a little more difficult. The way that MIME types are written, the top level type name goes before the slash, and the sub-type name goes after the slash. I really wanted to print out the part AFTER the slash, because it would be more meaningful to have two MIME types in the visualization labeled "xml" and "msw", rather than having them both labeled as "text". It took a very long time to figure out the right regex to use -- I did a lot of testing on regexr.com. This is what ended up working:

```
re.findall('[/]([a-z0-9][a-z0-9][a-z0-9])',mime_type)
```

After I solved this problem, some MIME types were still printing out blank. I realized that some had hyphens in them! So my new regex was:

```
re.findall('[/]([a-z0-9-][a-z0-9-][a-z0-9-])',mime_type)
```

After I solved THAT problem, some MIME types STILL weren't printing out correctly. In one case, the MIME type was not specified (I think that this was mostly folders, which don't have a MIME type). The other problem case was a MIME type labeled "$mimeResolver.getContentTypeFor($file.name)". I don't think that this is technically a MIME type, but I wanted to register it, because quite a few files had that in the MIME type field. It wasn't registering with the current regex, because it didn't have a slash in the name. Luckily, I was able to do a pretty simple conditional statement, which printed "N/A" if the MIME type wasn't specified, and printed "$mi" if it was that weird outlier.

####Bad input


####Letting the user choose the file
