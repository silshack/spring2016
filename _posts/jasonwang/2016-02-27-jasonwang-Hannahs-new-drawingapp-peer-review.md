---
layout: post
author: wagerpascal
title: "Peer Review of Hannah's Drawing App"
---
 
 Overall Hannah's project was pretty close to completing the objectives that were set out for her, as well as her own. The only text that appears is
 the clear button and the instructions that display at the bottom of the screen; the boundaries that separate the text from the "canvas" also
 seems very polished. The way that she approached the mode was interesting- rather than a conventional button or key, Hannah used the canvas
 to separate her "modes" (drawing sailboats vs. clouds) by position. For the other app requirements, they were completed without any issue. Overall, the app looks
 very clean, and does not have a lot of visual clutter. Besides the issue that her instructions were slightly cut off (but the meaning still is understandable), the
 functionality and interface are clear, and make utilization intuitive and simple.
 
 Hannah's code is compartmentalized cleanly, with her main.py file having a relatively short amount of code (only 26 lines). She also did a great job
 with dividing her modules, as well as limiting the number of functions (something I definitely wasn't able to achieve). Her commenting as well as her organization
 allowed for her code to be highly readable. I only got this the first time, and I'm not entirely sure what exactly happened for replication's sake, but 
 I ended up having every drawable object show up sideways (if it helps, with the top of each image pointing to the left instead). Also, (nothing against Hannah,
 but it's still an issue of turtle), rapidly clicking before the cursor is done drawing results in distortion of images, as well as 180 degree flips of the image.
 Overall, the neatness of which the code is set up allows for a lot of flexibility in functionality and interface appearance.
 
 Judging from the organization of the application, Hannah seems to have planned out what exactly she wanted to draw; the modules are split into the background,
 the drawables (clouds, birds, and boats), and the ripples (while the ripples are the only things that show up before the final image, if another object required
 another object to precede it, I would imagine that it would also be put here). Hannah has also confined everything that isn't involved with setup within a function;
 in the end, there are four executable lines in her main section of code, which is a very nice organization for anyone looking at her code.
 Her snapshot was largely the same structure to her final version, minus some changes related to her uncompleted milestone. When I met with Hannah to discuss her snapshot, she brought up
 some issues related to the sky area regarding drawing clouds and birds. I helped her in figuring out the randomly-generating version, but it's great to see that she found the necessary changes to fix the cloud-drawing.
 Most of her milestones were very achievable given the amount of time that was required. However, the one milestone she couldn't fix was similar to a limitation that I also ran into- that keys and clicking cannot
 be combined. 
 
 Hannah took on a project idea that she knew that she could do well, and delivered a well-polished product. My app, however, suffers a little bit from disorganization as well as "time crunch" syndrome. The modular method
 of which she took on the project is a technique that I really would like to adopt for general neatness of code, as well as ease of debugging and altering values. The only thing I disliked about the application is that the boundary
 between the sky and sea might be too small, leading to clouds being much too close; a little room for error might be beneficial there. After that, there is only the issue that the drawings are easy to break (again, not related to
 Hannah's code). Looking back on what I accomplished, I wish that I had tackled my application via modules than separate instances, which would have saved me a lot of grief with better organization and alterability. In the end, I
 would definitely rate Hannah's application above my own.
