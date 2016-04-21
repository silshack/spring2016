---
layout: post
author: hannahlwang
title: "Hannah's Project Update #2"
---

https://github.com/hannahlwang/inls560-finalproject

<h3>Milestones</h3>

- [x] Set up Cloud9 workspace
- [x] Import CSV files
- [x] Write starter code to read files
- [x] Set up separate Github repo
- [x] Push code to Github repo
- [x] Clean up data or figure out another way to deal with commas in file names
- [x] Write code to print out summary of file
- [ ] Deal with bad user input (wrong type of file, etc)
- [ ] Determine what options will be available on main menu (and secondary menu(s), if needed)
- [ ] First option should be print out column headers and allow user to choose one
- [ ] Code the other options (once I figure them out)
- [ ] Write code to create visualizations

<h3>Reflection</h3>

This week was a little frustrating because, although I did a lot of work and figured out a lot of things, it LOOKS like I didn't make much progress. It took me a while to figure out how to deal with the comma problem I was dealing with before, where commas in filenames were making each file name read as comma-separated-values. I ended up having to use the CSV module, while enabled me to read a file with tab delimiters (for some reason, this wasn't working before when I was trying to delimit with tabs). But it finally worked! Now the application can read a tab-separated value file, and it separates each value correctly. This means that I am able to print out accurate statistics about file types, etc, because I can search by index.

Another revelation came in the form of me remembering that functions were a thing (duh). I was creating a separate block of code for each type of data (object, deleted state, mimetype, etc), and realized that I was copying and pasting a lot. I realized that I could create a "makedict" function that creates a dictionary, makes a dictionary counter, and prints the contents of the dictionary, regardless of the data type. This will make it a lot easier moving forward, because I will be able to easily get a statistics for each data type, without having to write a block of code every time.

I am a little frustrated with my attempts to deal with bad user input. I tried doing it with a "while" loop, with the condition being that the first line does not equal the first line of CDR export files:

```
while first_line_tabbed != 'Object Type'+'\t'+'PID'+'\t'+'Title'+'\t'+'Path'+'\t'+'Label'+'\t'+'Depth'+'\t'+'Deleted'+'\t'+'Date Added'+'\t'+'Date Updated'+'\t'+'MIME Type'+'\t'+'Checksum'+'\t'+'File Size (bytes)'+'\t'+'Number of Children' :
  print("Please enter a file name: ")
```

However, I can't define "first_line_tabbed" until I read the file, but I can't read the file until I get the input from "Please enter a file name: "! It feels like a catch-22, and I'm hoping that asking around in class tomorrow will help me solve it.
