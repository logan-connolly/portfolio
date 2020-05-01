+++
title = "Am I the asshole?"
date = "2020-05-01"
author = "Logan Connolly"
cover = "/img/asshole/cover.png"
description = "Build a text classifier trained on data from [/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/) that accepts a story as input and detects whether or not you're the asshole"
+++

# Introduction

[/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/) is a reddit community that allows you to post an argument that you've had (or are currently having) in the hope that others can quiet your conscience. Redditors are judge, jury and executioner. Taken from the about page:

> "A catharsis for the frustrated moral philosopher in all of us, and a place to finally find out if you were wrong in an argument that's been bothering you." -/r/AmItheAsshole

Based on how redditors in the comments have voted, the argument is categorized accordingly:

- **YTA**: You're the Asshole
- **NTA**: Not the Asshole
- **ESH**: Everyone Sucks here
- **NAH**: No Assholes here
- **INFO**: Not Enough Info

# Goal

The idea is to build an app where you can submit your issue directly and get an asshole prediction. This could be handy if you want a quick answer and do not want to risk a reddit post being traced back to you. 

In order to accomplish our goal, the following steps need to be taken:

1. **Gather data** from the top posts of [/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole), extracting the asshole classification result and the original text of the post.
2. Annotate posts to **tag entities** in the posts, which will help the model determine how many parties are involved and what type of people are involved (ie. friends, family, strangers, etc.) 
3. **Train model** on annotated data that makes an asshole prediction; Use active learning techniques to make sure that the model is predicting accurately.
4. Add **explainability** to model which will highlight which part of the text led it to make its decision.
5. **Test model** with posts that the model has not trained on and posts where a final classification has not been given.
6. Create a **front-end** that accepts text and makes a prediction based on the input

At the end of the project, a user should be able to go to a website hosting the asshole predictor, type in their issue, and get a response instantly.
