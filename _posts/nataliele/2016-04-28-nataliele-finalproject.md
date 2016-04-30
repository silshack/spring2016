---
layout: post
author: nataliele
title: "Natalie's final project"
---

<iframe src="https://trinket.io/embed/python3/c89af16d90" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Wow, what a project! What a semester! First of all I want to say that I've learnt so much and had so much fun in this class! Thank you for your prep talks, inspirations and general directions on how to approach programming. I think I got everything that I wanted to learn out of this class: able to code simple programs, able to understand programming, having a good foundation to be able to keep learning. I feel really fortunate to have taken this class as my first programming class. I'm feeling sad this is my last commit to the class page… Thank you for all the emotions I've gone through writing codes!

Now on to the final project. I remember being torn at the beginning because I didn’t know which dataset to choose. I had a manageable dataset on health care expenditure that I’m familiar with and another huge, unfamiliar health insurance dataset from Kaggle. I wanted to try the second one but was intimidated by the size of it (some 5Gb in total!). It was also going to be a very steep learning curve because I have to read all the data dictionaries to understand how the dataset is structured, what the variables are etc. Bbbbut, I went for it anyway. Because, well I guess that's what this class is about, trying new things and stretching yourself.

So the dataset I selected has a couple of files: one with the rates information, one with the issuer (insurance company) information, one with the covered area information. The main file I want to work on with the rates information was 2Gb. And I wanted to code in Trinket, which means I have to break the dataset down and get a sample of it to paste into Trinket. And I want the sample to be random with different states' information so that means I cant just go through the first 500 lines of the file because that would only be 1 or 2 states. After some false starts, going to a Meetup meeting and Googling, StackExchange came to the rescue. I was able to find a solution that suitable for what I need and simple enough that I could understand and execute. After some trials and errors, I was finally able to make it work. 
It's interesting that I wanted to use Trinket because I didn’t want to mess with Cloud9 or PyCharm but I ended up using PyCharm to execute these codes to get a sample file for Trinket. But I'm glad I did because I could also test my program in PyCharm to make sure it works using the original files instead of the sample files.

```python
with open(r'C:\Users\Natalie Le.DESKTOP-1SOSUEB\OneDrive\Class\Spring 2016\INLS 560\Final project\Rate.csv',"r") as f:
    with open("rate 2016.csv", "w") as fo:
        fo.write(f.readline())
        for line in f:
            if re.search('^2016',line):
                line_extracted = f.readline()
                fo.write(line_extracted)
count = 0
with open ('out.csv','r') as f:
    for line in f:
      count = count +1
print(count)

lines_to_grab = random.sample(range(count),500)
with open('out.csv',"r") as f:
  with open("rate_sample.csv", "w") as fo:
      for i, line in enumerate(f):
          if i in lines_to_grab:
              line_extracted = f.readline()
              fo.write(line_extracted)
```

The way I design the program is for user to bring in a rate file that should also be from CMS. The sample file is for 2016 but user can have a 2015 file, 2014 file and it would still work.

As previously mentioned, I think the biggest problem I had to deal with was formulating what I want to do with the dataset. Because it's so complicated I had so many ideas of what information I can get out of it. I know I should plan ahead and I wanted to plan ahead what analysis functions I'm going to make but I honestly couldn’t. I couldn’t tell at the beginning how long it will take me to make one analysis function and how long it will take me to debug, add loops, catch input errors etc so I couldn’t estimate how many analysis functions I can do.

So I feel like I wanted to do a lot in the beginning but after embarking on the project and seeing programs from other people, I realized that I was overly ambitious and that it's better for me to make sure I have a few functions that work well. So my final milestones are considerably different from what I had envisioned in the beginning. 

The whole process is definitely one of learning and figuring things out as I code. I'm certainly aware that because I'm not fluent in this language, I still make a lot of small mistakes that made me scratch my head and rack my brain and then went "Ahhhh, that's why!!!" For example:

![bug_line](http://nataliele.web.unc.edu/files/2016/02/bug_line.png)

This is also an example of how there are 361230 variables and you have to be really intentional about naming them and be careful of which one you use. I couldn’t for the life of me figure out why it's printing 1s and not the third item of the list which is the state name. Then finally it dawned on me that I was using line[2] when I should have used line_list[2], which is the list I just created T___T. I also had some problems with looping but I was able to fixed them. My debugging procedure is to think about how the syntax works, examine the output, how it's different from what I want to see, try to guess what's happening in the black box. I definitely feel like some heroine slaying one bug after another. 

The previous exercises on lists and dictionary helped a lot. They're totally applicable to what I need to do for my dataset. For example, I needed to get a dictionary of all the states in the dataset, then compare what the user enter to that list. Or I needed a dictionary of the issuers ID and their corresponding names so I can swap the ID for the names when I display rate information (Because the info from the rate file only has ID and not names. This is kind of similar to the county codes and county names I was talking about.). You also  might notice that I had to use lists for the rate.csv file because there is no unique id in that file. There are multiple lines with the same PlanID but different age group. So only a combination of PlanID and Age would be unique.

It's also a reiterative process for me. I would write out the codes first, then realized I should put them in a function to reuse them later. I also go back to my codes and try to make them better, tidier. I'll give credits to Naveneet, who showed me how to take the codes outside my main function and put them in another function without getting the "Local variables referenced before assignment." by using parameters. We did this for Turtle a lot but I totally forgot about it. This has helped me to modularized and organized my codes better. Other things I added along the way to make user interface better like have "\n" before menus for readability, prompt user to enter to continue so user has time to look at the information displayed. After looking at my data to make sure they make sense, I also decided to drop the observations with rate 9999.0 as they're inapplicable and skewed the results. Or stop printing the highest rate for each state once 1 rate has been printed (Because there are multiple plans with the same rates and attributes). Even now there are still things that I can improve or add but I have to balance being a perfectionist with the limited time I have.

I think my program works really well but one thing that bugs me (no pun intended) is when I pass `row` into my function "highest_premium" for example, I have to mention "row" beforehand or I'll get the error that says "row is not defined.". So I ended up having to use `row = True`, which is probably not the best design possible.

![bug_row](http://nataliele.web.unc.edu/files/2016/02/bug_row.png)

Which brings me to my next point: good code design. I think I got a glimpse of how important a good code structure/design is. I tried to make things as efficient as possible and not have dubious workarounds. It's so important for me to be able to debug, or add other features, or for people to edit my codes. I learnt that sometimes fixing "that small thing" is so frustrating and time-consuming because "that small thing" is intertwined with everything else. 

My milestones:

 - [x] clean and attach relevant files into Trinket
   - [x] sampling main files from Kaggle dataset
 - [x] get to know the dataset (CMS website, data dictionary, etc)
 - [x] design menu selection screen
   - [x] user able to choose federal or state level
   - [x] help menu on description of the program and functions
   - [x] user able to access help menu, exit
 - [x] user able to choose options under federal level:  
   - [x] highest premium rate across all states
   - [x] highest premium rate for each age group across all states
   - [x] highest premium rate for each state
   For all the options:
   - [x] print heading, attributes
   - [x] visualization: bar charts where applicable
   - [x] user able to return to main menu, help menu, exit
 - [x] user able to choose state
 - [x] user able to choose options under state level: 
   - [x] highest premium rate across chosen state
   - [x] highest premium rate for each age group in the chosen state
   For all the options:
   - [x] print heading, attributes
   - [x] visualization: bar charts where applicable
   - [x] user able to return to main menu, help menu, exit

 - [x] stretch: linking issuer file to get issuer name to display instead of issuer ID
 - [ ] stretch: interaction functions (eg. How many plans in NC lower than $100?)
