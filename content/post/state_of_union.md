+++
title = "State of the Union Address"
date = "2017-09-15"
author = "Logan Connolly"
cover = "img/state_of_union/cover.jpg"
description = "What do presidents really say during the State of the Union?"
+++

# Introduction

The State of the Union address was originally intended to be an address given by the President to Congress in order to report on the condition of the nation and what the President believes the nation’s priorities should be going forward. 

It has now shifted towards an address to not only Congress but the American people as well. I thought these addresses would be a great way to practice text analytics. I expect there to be distinct changes in text sentiment during war time. I plan to also extract important topics unique to each presidency through *Term Frequency Inverse Document Frequency (tf-idf)*. More on that later.

I gathered data from 1980 to 2017 from the [American Presidency Project](http://www.presidency.ucsb.edu/index.php), a non-profit and non-partisan of presidential documents on the internet. For the sake of this analysis, we will only look at presidencies starting with Ronald Reagan onward.

# Who talks the most?

The first thing I want to look at is who is the chattiest out of the presidents. It appears that Bill Clinton and Barack Obama have consistently longer addresses than the other presidents. It is perhaps interesting to note that they are the only two Democratic Presidents in the data.

{{< image src="/img/state_of_union/word_count.jpg" alt="Word Count Bar Chart" position="center" style="border-radius: 8px;" >}}


# Term Frequency Inverse Document Frequency

In this part of our analysis, we are going to use tf-idf in order to derive the importance of words in comparison to the word's frequency in other addresses. The more frequent "rare" words that are in a given address have higher tf-idf scores. According to [Wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), tf-idf is defined as:

>In information retrieval, *tf–idf* is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in information retrieval, text mining, and user modeling. The tf-idf value increases proportionally to the number of times a word appears in the document, but is often offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general. Nowadays, tf-idf is one of the most popular term-weighting schemes. For instance, 83% of text-based recommender systems in the domain of digital libraries use tf-idf.

With *tf-idf* calculated for each word grouped by president, we can plot the top words for each President. By doing so, we should be able to identify topics that were particularly important to for a given Presidency.

{{< image src="/img/state_of_union/tf_idf.jpg" alt="tf-idf for each Presidency" position="center" style="border-radius: 8px;" >}}

Some of the words that appear in the plots seem to be obvious like Sadam Hussein which appears in both Bush Presidencies or the large prevalence of ISIL in Obama’s term.

This is intuitive because the State of the Union is meant to address the most prevalent problems that the nation faces. However, others were not so easy to understand, notably “100th” from Reagan’s addresses and “Ryan” in President Trump’s. In order to find out the meaning of these words, I had to dig into the text.

After doing this I realized that “100th” referred to the 1988 State of the Union address given by President Ronald Reagan to the 100th United States Congress, and “Ryan” referred to U.S. Navy Special Operator, Senior Chief William “Ryan” Owens who died in battle and whose wife attended the 2017 State of the Union address.

This gives a glimpse into the power of text analytics and how you can explore a huge amount of text with relatively few lines of code in order to get an idea of what the general message is about. At the very least, it gives you hints into what is important and where you should look to learn more.

# Negative Sentiment

Let’s take a look at two recent addresses that we expect to draw relatively high negative sentiment: first President Bush’s State of the Union following **September 11, 2001** and second the **2008 economic crash** that happened during Obama’s Presidency. 

Can you tell which wordcloud belongs to which event?

{{< image src="/img/state_of_union/wordcloud.jpg" alt="Negative Sentiment Wordcloud" position="center" style="border-radius: 8px;" >}}