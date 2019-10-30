+++
title = "German Election 2017"
date = "2017-10-12"
author = "Logan Connolly"
cover = "img/german_election_2017/cover.jpg"
description = "Analyze the results of the 2017 German Election"
+++

# Introduction

The data that I used for this analysis is hosted at [Kaggle](https://www.kaggle.com/jenslaufer/german-election-2017). The dataset caught my attention because of the availability of geo spatial data. I recently discovered the `sf` package, a tidy package in R built for plotting geometry data. Find more about the package at [https://github.com/r-spatial/sf](https://github.com/r-spatial/sf).

The dataset deals with the German 2017 Election Results and how votes were distributed among regions. I wanted to visualize the results of the German Election at both the State and District level. In Germany there are two separate votes, and you can learn more about the process [here](https://en.wikipedia.org/wiki/Electoral_system_of_Germany). I primarily the **second vote** because according to Wikipedia:

> For the distribution of seats in the German Bundestag, the second vote is more important than the first vote. This second vote allows the elector to vote for a party whose candidates are put together on the regional electoral list.

The voting system is more nuanced than I had ever imagined, but I figured that the second vote would be more telling of how affiliated voters are with certain parties.


# Voter Turnout

It appears that voter turnout has increased overall by over the past three election cycles. There is much higher turnout in the souther states of Baden-Württemberg and Bayern.

{{< image src="/img/german_election_2017/turnout.jpg" alt="Voter Turnout Map" position="center" style="border-radius: 8px;" >}}


# Voting Distribution by Party


#### plot the distribution on the map by district

It turned out that where you live plays a big role on who you are likely to vote for. In these maps, you can see that *AfD* and *die LINKE* were highly concentrated in the former DDR, while *die GRÜNE* has a large presence in the former West Germany.

{{< image src="/img/german_election_2017/distribution.jpg" alt="Voter Distribution Maps" position="center" style="border-radius: 8px;" >}}


#### plot box-plots to see the distribution of individual districts

The points in the plot are markers for each district, while the box aspect portrays how narrow or wide the distribution is. From looking at the plot, *AfD* and *die Linke* have many outliers that are from the Eastern states. On the contrary, *FDP* has a similar median as *AfD*, but a very tight distribution among all districts. Notice the how *AfD* and *die LINKE* have some districts they dominated and appear as outliers for their respective parties.

{{< image src="/img/german_election_2017/boxplots.jpg" alt="Voter Box Plot by Party" position="center" style="border-radius: 8px;" >}}


#### plot the voting results for each state

These bar charts show how voting for individual parties were distributed among staes. In most states, *CDU-CSU* dominates the vote; however, that is not always the case. Berlin proves to be a very diverse place to live politically (makes sense). Also *AfD* in Sachsen is on par with *CDU-CSU*, which must have been a surprise in this past election.

{{< image src="/img/german_election_2017/barchart.jpg" alt="Barchart by State" position="center" style="border-radius: 8px;" >}}