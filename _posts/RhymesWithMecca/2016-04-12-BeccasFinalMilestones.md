---
layout: post
author: RhymesWithMecca
title: "Becca's Final Project Milestones"
---

For my project, I'd like to make a tool that analyzes gDNA or cDNA sequences.  The program will come with a sample of each type of sequence, and the user can add their own sequence to the appropriate module for analysis.  The program will have a help function that the user can call to see what its capabilities are.  The program should be iterable and the user can exit when they'd like.  

For cDNA, the tool should be able to transcribe the sequence into mRNA, translate it into a protein (I did this in my starter code, but I'd like to fiddle with making the output cleaner [and maybe change the code slightly]), count the number of each amino acid (i.e. six leucines, one serine, two valines, etc.), print the length of the sequence, print the reverse complement, and print the complementary DNA strand.

For gDNA, the tool should be able to find the percent AT/GC content (useful to know when amplifying by PCR), print the length of the sequence, print the reverse complement, and print the complementary DNA strand. The user should be able to select which sequence they'd like to analyze or if they'd like to view the help function (this is currently just LC3B, but eventually will be specified by user input).  I'm thinking the visualization part will be for the % AT/GC content (unless I can come up with/have time to make a graphical way of representing amino acids).  
 
**Starter Code**

<iframe src="https://trinket.io/embed/python3/84d05dedeb" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Milestones**

  - [ ] cDNA (various functions accessible by user input): program can transcribe the sequence into mRNA, translate it into a protein, count the number of each amino acid, print the length of the sequence, print the reverse complement, and print the complementary DNA strand
  - [ ] gDNA (various functions accessible by user input): program can find the sequence's percent AT/GC content, print the length of the sequence, print the reverse complement, and print the complementary DNA strand
  - [ ] program has help function, accessible by user input
  - [ ] program has visual component
  - [ ] program is iterable ("What would you like to do?" after each step) and user can exit if they so desire (test multiple cases!)
  - [ ] program has been debugged
 
___
 
**For Tuesday - cDNA Capabilities**  

  - [ ] transcribe sequence into mRNA
  - [ ] make translate output pretty
  - [ ] count the number of each amino acid
  - [ ] print the length of the sequence
  - [ ] print the reverse complement
  - [ ] print the complementary DNA strand
