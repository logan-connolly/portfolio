+++
title = "German Election 2017"
date = "2017-10-12"
author = "Logan Connolly"
cover = "/img/german_election_2017/cover.jpg"
description = "Does where you live determine how you vote?"
+++

***
All code used to create this post can be found on my [GitHub](https://github.com/logan-connolly/portfolio-posts/blob/master/posts/german_election_2017/german_election_2017.md).
***

# Introduction

The data that I used for this analysis is hosted at [Kaggle](https://www.kaggle.com/jenslaufer/german-election-2017). The dataset caught my attention because I enjoy plotting data on maps. I recently discovered the `sf` package in R, so I used this as an opportunity to learn it. Find out more about the package here at [https://github.com/r-spatial/sf](https://github.com/r-spatial/sf).

The dataset deals with the German 2017 Election Results and how votes were distributed among regions. I wanted to visualize the results of the German Election at both the State and District level. In Germany there are two separate votes, and you can learn more about the Electoral System in Germany [here](https://en.wikipedia.org/wiki/Electoral_system_of_Germany). 

I concentrated primarily on the **second vote** because according to Wikipedia, it is the more important vote:

> For the distribution of seats in the German Bundestag, the second vote is more important than the first vote. This second vote allows the elector to vote for a party whose candidates are put together on the regional electoral list. [Wiki]

# Voter Turnout

It appears that voter turnout has increased over the past three election cycles. There appears to be a higher turnout in the southern states of Baden-Württemberg and Bayern.

{{< image src="/img/german_election_2017/turnout.jpg" alt="Voter Turnout Map" position="center" style="border-radius: 8px;" >}}


# Voting Distribution by Party


#### plot the distribution on the map by district

It turns out that where you live indeed plays a role in who you vote for. In these maps, you can see that *AfD* and *die LINKE* were highly concentrated in the former DDR, while *die GRÜNE* has a large presence in former West Germany.

{{< image src="/img/german_election_2017/distribution.jpg" alt="Voter Distribution Maps" position="center" style="border-radius: 8px;" >}}


#### plot box-plots to see the distribution of individual districts

The points in the box plots are markers for each district, while the box aspect portrays how narrow or wide the distribution is. From looking at the plot, *AfD* and *die Linke* have many outliers. 

On the contrary, *FDP* has a similar median as *AfD*, but *FDP* has low variation among districts while *AfD* has very high variation and a handful of big outliers. Notice how *die LINKE* also has its share of outliers.

{{< image src="/img/german_election_2017/boxplots.jpg" alt="Voter Box Plot by Party" position="center" style="border-radius: 8px;" >}}


#### plot the voting results for each state

These bar charts show how voting for individual parties were distributed among different states (Bundesländer). In most states, *CDU-CSU* dominates the vote; however, that is not always the case. 

Berlin proves to be a very diverse place to live politically (makes sense). Also, *AfD* in Sachsen is on par with *CDU-CSU*, which must have been a surprise in this past election.

{{< image src="/img/german_election_2017/barchart.jpg" alt="Barchart by State" position="center" style="border-radius: 8px;" >}}


# Conclusion

I highly recommend checking out the `sf` package if you get your hands on some geo-spatial data and want to plot it. The package makes it easy to get up and running and integrates well with  `ggplot2`. 

Going forward I think it would be interesting to see if:

* voter turnout continues to increase in the next election
* regions become more or less polarized regarding who they vote for

Have a look at the source on [GitHub](https://github.com/logan-connolly/portfolio-posts/blob/master/posts/german_election_2017/german_election_2017.md) if you are interested in replicating the analysis.
