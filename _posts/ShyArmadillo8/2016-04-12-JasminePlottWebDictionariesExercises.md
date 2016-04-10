---
layout: post
author: ShyArmadillo8
title: "Jasmine Plott's Web Services Exercises"
---

Here is my web dictionaries exercise:
<iframe src="https://trinket.io/embed/python3/7f50e1f025" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

At first, I thought that this exercise would be a very simple one, since I figured out fairly quickly how to work through the list to get to a particular item.  What I'd originally started with was working to pull out the city, county, state, and country from the code, but I discovered as I tested my code with other locations that the city, county, state, and country information was not always in the same location.  Here is what I had to begin with:

```
city = js["results"][0]["address_components"][0]["long_name"]
print("County Name:", city)
county = js["results"][0]["address_components"][1]["long_name"]
print("County Name:", county)
state = js["results"][0]["address_components"][2]["long_name"]
print("State Name:", state)
country = js["results"][0]["address_components"][3]["long_name"]
print("Country Name:", country)
```

I did try a strategy where I created an if statement for if the type was set to a certain value to print out the name of the value for that piece, but I was not able to get this to work.  The formatting I had looked like this:

```
if types == "locality" and types == "political":
  county = js["results"][0]["address_components"][1]["long_name"]
  print("County Name:", county)
else:
  print("Sorry, this type doesn't exist")
```

Perhaps my formatting was off, since whenever I would do this, I discovered it would say "Sorry, this type doesn't exist." no matter what the location was. I'll need to look into exploring this idea further later.  

As a compromise, I decided that I would focus on printing all the parts of the address components by using a for loop.  This way, it would show relevant information to the user, and it would suffice as a different way of solving the problem that I had had before.  I made sure to create the count variable in the for loop for ensure that I would be progressing through each item in the list.  Here's what the bulk of my code looked like:

```
    for i in addresses:
      place_name = js["results"][0]["address_components"][count]["long_name"]
      place_short = js["results"][0]["address_components"][count]["short_name"]
      place_type = js["results"][0]["address_components"][count]["types"]
#I printed the information for each component of the address.
      print("Details of Place Long Name: ", place_name)
      print("Details of Place Short Name: ", place_short)
#I was able to get rid of the brackets and out ' but couldn't get the inner ones
#to leave
      print("Place Types: ", str(place_type).strip("['']") , "\n")
```

This definitely helped me accomplish my goal and printed out more information about the location that the user had entered.  This also helped show me that there was more information about each location in address components than I had realized, but this helped me break down the code I had into more readable chuncks for the user.  As you can see by my comment, I wasn't able to split my code as perfectly as I had wanted to, but I was able to make most of it look beautiful.

Pulling out information about the zip code, county, state, etc. was definitely the most challenging part of this project for me, since I easily pulled out the full address and place_id fairly quickly; I figured that these pieces of information would be more useful for a user than having latitude and longitude coordinates (although I guess that this depends on your purpose with the information).

Overall, this was a pretty good exercise, and I liked seeing how XML and JSON could be used here.  I'd learned about these in my Organization of Information course, so it was pretty interesting to see how these could be used and adapted within a different class setting.
