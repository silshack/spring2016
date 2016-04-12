---
layout: post
author: payalpn
title: "Payal's Web Dictionary Exercise"
---

**Code:**

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode(
        {'sensor':'false', 'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    
    placeID = js['results'][0]['place_id']
    print("Place ID:", placeID) 
    location = js['results'][0]['formatted_address']
    print("Location:", location)
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('Latitude:',lat)
    print('Longitude:',lng)
    results = js['results']
    resultsLength = len(js['results'])
    if len(results) > 1:
      print("Other Locations With the Same Name:")
      x =resultsLength - 1 
      while x > 0: 
        print(results[(x)]['formatted_address'])
        x = x - 1
        # if x == -1: 
        #   break 
        

**Links:**

https://trinket.io/python3/b6547564e8


<iframe src="https://trinket.io/embed/python3/b6547564e8" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


**Reflection:**

This program pulls the Place ID, latitude, longitude, and formatted address.  The last three were already provided in the program, so pulling the Place ID was fairly simple because I was able to base the formatting off of those.  When I tried different location searches I realized that some searches had more results than others depending on what was entered by the user.  In order to accommodate this I created an if statement with a nested while loop that would print out the formatted addresses if there was more than one results for the users’ search.  I first tried to use a for loop for this, however, I kept getting errors so I tried using a while loop which ended up working.  
