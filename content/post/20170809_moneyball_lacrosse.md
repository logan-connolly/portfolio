+++
title = "Moneyball Lacrosse"
author = "Logan Connolly"
date = "2017-08-15"
keywords = ["python", "ai", "data science", "selenium", "plotly"]
tags = ["python", "selenium", "plotly", "stats"]
description = "Is there a competive advantage to be had using statistics?"
+++

# Introduction

I drew inspiration for this project from a variety sources. First, from the movie [Moneyball](http://www.imdb.com/itle/tt1210166/) based off the book by [Michael Lewis](https://www.goodreads.com/book/show/1301.Moneyball). Then, from [Analytics Edge](https://www.edx.org/course/analytics-edge-mitx-15-071x-3), a course offered by edX and MIT, where we went step-by-step through how the Oakland A's used statistics to gain a competitive edge over opponents. 

After I completed the course, I thought why not do it for Lacrosse, a sport that I have played since I was five. As I researched whether or not such an analysis had been done before, I stumbled upon an insightful article written in 2011 by [Michael Mauboussin](http://www.laxpower.com/content/mauboussin/stats_analysis.php). I borrowed insights that he described in the article in addition to exploring different metrics.

# Data

I scraped the data from the http://stats.ncaa.org/. I did this mainly with the [Selenium]() package. Selenium is a great tool that allows you to write scripts that can do a variety of different actions on a website (i.e. clicking). This is really import when dealing with websites that are interactive.

The NCCA stats website is one of these types of websites. So in order to retrieve all the data, one would need to select and filter data.

{{< load-plotly >}}
{{< plotly json="/plotly/moneyball_lacrosse/model_plot.json" height="400px" >}}
