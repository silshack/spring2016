--- 
layout: post
author: batlopez
title: "Nat's Final Project Idea and Milestones"
---

For my final project, I will be working on the data analysis option. Specifically, I will take a spreadsheet with UNC course information and search through course titles, departments, and course descriptions to find specific keywords relating to data studies, visualization, and mapping. This will ultimately be used at my job in the Research Hub to identify possible classes to partner with. I may generate the keywords by looking first at one spreadsheet of classes that have already received support from the Research Hub and generating a list of most frequently used words. I imagine I can do this by creating a dictionary that counts the number of times each word was used. The spreadsheet of current course offerings exists (I was able tor request it from the registrar's office) and I believe I can access a spreadsheet with information about classes already supported. 

Milestones:
- [ ] For file with data about classes supported in the past, create dictionary with values that count number of times each word appears.
- [ ] Return a list of words with highest values. 
- [ ] For file with course data information, search for most frequently used terms. I can create a for loop that goes through each word in the list and searches each row in a the course description column and returns the course title (will have to print a different column then the one being searched) plus the column with the full description. 
- [ ] Possibly see if I can see if multiple terms are used within the same course description and use the number of keywords used plus their frequency to rank them in order. 
- [ ] If time permits, return a list of departments with the highest returns of frequently used terms. 
- [ ] Create graph of departments with courses that have the highest returns of frequently used terms.
