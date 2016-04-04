---
author: yiyangshi
layout: post
title: "Yiyang's Drawing App"
---

Here is the program:
<iframe src="https://trinket.io/embed/python/615dee82e2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Reflection:

Okay, I know the man looks weird…

One key issue of my program is to store the locations. In the feature table, I need to store the location of the words “Eyebrows”, “Mouth”, and “Eyes” in order for the features to be drawn exactly in the rectangles. On the actual face, I need to store the natural location for eyebrows, mouth, and eyes so that when the selected features are drawn on the face, they are at the right position. After a lot of failures and unsuccessful tries, I found that list could best solve this issue. The advantage of list is that I can continuously add values to the list without creating extra variables. When the values are needed, I can call from the list using the location of the value. I can also traverse a list. For the locations on the actual face, I also used list for storage purpose.

Another key issue of my program is parameter. Because of the different shapes and sizes of these facial features, there are a lot of parameters in this program. Those parameters are imported into different “py” files and used several times at different places in the program. So, the lesson learned is that create clear name and store parameters independently is extremely important. At first, I did a lot of hand calculation and plugged in parameters directly as arguments into the functions. However, when my program became longer, I can hardly figure out all the distances on the graph. So, I went back and created independent variables for every parameter and created clear names for them. This is beneficial not only because it makes the program easier to read but also easier to adjust in the future. 

Something for the future:

I want the users to be able to drag those rectangles onto the face. Dragging seems to be a more natural way in a drawing app like this. 

Milestone:

- [x] Draw the empty face background.
- [x] For each facial feature, draw three choices.
- [x] Create a hiden turtle that draws user's choice on the empty face.
- [x] Draw color scale on the screen for user to choose.
- [x] Color the glassframe.
- [x] Limit user to only pick one choice for each facial feature.
