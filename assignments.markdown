---
layout: default
title: "Assignments"
---
 
## {{ site.course.number }} Assignments

Assignments will be added below.  Readings should be done by the beginning of class.  Exercises should 
be completed by the date and time listed.  Class notes are for your reference of if you have to miss a class.

{% comment %} Jekyll 2.4 doesn't support the concat filter so we hack it with push {% endcomment %}
{% assign assignments = "" | split: "" %}
{% for exercise in site.categories.exercise %}
{% if exercise.published != false %}
    {% assign assignments = assignments | push: exercise %}
{% endif %}
{% endfor %}
{% for reading in site.categories.reading %}
    {% assign assignments = assignments | push: reading %}
{% endfor %}
{% for note in site.categories.notes %}
    {% assign assignments = assignments | push: note %}
{% endfor %}

{% assign all_assignments = (assignments | sort: 'date') %}

<table>
 
    <th>Type</th>
    <th>Title</th>
    <th>Due Date</th>
 
{% for post in all_assignments  %}
    <tr>
        <td>
            {% if post.categories contains "exercise" %}
            <span class="label round {% if post.inclass == true %}warning">In-class {% else %}success">{% endif %}Exercise</span>
            {% endif %}
            {% if post.categories contains "reading" %}
            <span class="label round info">Reading</span>
            {% endif %}
            {% if post.categories contains "notes" %}
            <span class="label round">Class Notes</span>
            {% endif %}
        </td>
        <td>
            {% if post.link %}
                {% assign link = post.link %} 
            {% else %}
                {% capture link %}
                    {{ site.baseurl }}{{ post.url }}
                {% endcapture %}
            {% endif %}
            <a href="{{ link }}">{% if post.categories contains "notes" %} {{ post.date | date: "%b %d" }} - {% endif %}{{ post.title }} </a>
        </td>
        <td>
            {% if post.categories contains "notes"%}
            {% else %}
            <span>{{ post.date | date: "%a, %b %d, %Y" }} {% if post.categories contains "exercise" %}{% if post.inclass == true %} by midnight{% else %} at {{ post.date | date: "%I:%M %p" }}{% endif %}{% endif %}</span>
            {% endif %}
        </td>
    </tr>

{% endfor %}
</table>
