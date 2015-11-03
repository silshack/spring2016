---
layout: post
author: elliott
categories: how-to
title: Adding interactive Python to your posts
---

Include interactive trinkets in your Jekyll site with 2 lines of code.  Why?  Because static sites are better when they're interactive!  

Use trinkets to submit interactive code with your assignments.

## Usage

Add these lines before and after the code you want to make interacive:

{% highlight liquid %}{% raw %}{% include trinket-open %}{% endraw %}
# your code here
{% raw %}{% include trinket-close %}{% endraw %}{% endhighlight %}

That's it!  As of Sept 2014 Jekyll Tools supports Python and HTML/CSS.

## Python

This code:
{% highlight liquid %}
{% raw %}{% include trinket-open type='python' %}{% endraw %}
import turtle

tina = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    tina.color(c)
    tina.forward(75)
    tina.left(90)

tina.penup()
tina.backward(100)
tina.write("Hello world!")
{% raw %}{% include trinket-close %}{% endraw %}
{% endhighlight %}

Gives you this interactive Python trinket on your Jekyll site:

{% include trinket-open type='python' %}
import turtle

tina = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    tina.color(c)
    tina.forward(75)
    tina.left(90)

tina.penup()
tina.backward(100)
tina.write("Hello world!")
{% include trinket-close %}

## HTML

This code:

{% highlight liquid %}
{% raw %}{% include trinket-open type='html' %}{% endraw %}
<html>
<head>
    <style type="text/css">
        body {
            background-color: #008aff;
            text-align: center;
        }
        .logo {
            position: relative;
            top: 50%;
            transform: translateY(-60%);
        }
        .logo img {
            max-width: 90%;
        }
    </style>
</head>
<body>
    <div class="logo">
        <img src="https://trinket.io/img/trinket-logo-big.png" />
    </div>
</body>
</html>
{% raw %}{% include trinket-close %}{% endraw %}
{% endhighlight %}

Gives you this interactive HTML trinket  on your Jekyll site:

{% include trinket-open type="html" %}
<html>
<head>
    <style type="text/css">
        body {
            background-color: #008aff;
            text-align: center;
        }
        .logo {
            position: relative;
            top: 50%;
            transform: translateY(-60%);
        }
        .logo img {
            max-width: 90%;
        }
    </style>
</head>
<body>
    <div class="logo">
        <img src="https://trinket.io/img/trinket-logo-big.png" />
    </div>
</body>
</html>
{% include trinket-close %}

Note: These trinkets support most of HTML and CSS, but not Javascript (yet).  Also, you can find a live version of the trinket above [here](https://trinket.io/html/47807974be).

## Customize!

Make your trinkets the right height:
{% highlight liquid %}
{% raw %}{% include trinket-open type='python' height='100' %}{% endraw %}
for i in range(10):
    print "Only the lines you need"
{% raw %}{% include trinket-close %}{% endraw %}
{% endhighlight %}
Gives you this interactive Python trinket:

{% include trinket-open type='python' height='100'%}
for i in range(10):
    print "Only the lines you need"
{% include trinket-close %}

## Acknowledgements

Our interactive Python trinket makes heavy use of the awesome [Skulpt project](http://skulpt.org), which uses client side Javascript to interpret Python in your browser.  Check em out and [contribute on Github](http://github.com/skulpt/skulpt)!  

The interactive HTML trinket is soulmates with [Mozilla Thimble](https://thimble.webmaker.org), which is another awesome project that you can [contribute to on Github](https://github.com/mozilla/thimble.webmaker.org).