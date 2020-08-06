+++
title = "Moneyball Lacrosse"
author = "Logan Connolly"
date = "2017-08-15"
keywords = ["python", "ai", "data science", "selenium", "plotly"]
tags = ["python", "selenium", "plotly", "statsmodels"]
description = "Is there a competive advantage to be had using statistics?"
+++

# Introduction

I drew inspiration for this project from a variety sources. First, from the movie [Moneyball](http://www.imdb.com/itle/tt1210166/) based off the book by [Michael Lewis](https://www.goodreads.com/book/show/1301.Moneyball). Then, from [Analytics Edge](https://www.edx.org/course/analytics-edge-mitx-15-071x-3), a course offered by edX and MIT, where we went step-by-step through how the Oakland A's used statistics to gain a competitive edge over opponents. 

After I completed the course, I thought why not do it for Lacrosse, a sport that I have played since I was five. As I researched whether or not such an analysis had been done before, I stumbled upon an insightful article written in 2011 by [Michael Mauboussin](http://www.laxpower.com/content/mauboussin/stats_analysis.php). I borrowed insights that he described in the article in addition to exploring different metrics.

# Data

I scraped the data from the http://stats.ncaa.org/. I did this mainly with the [Selenium]() package. Selenium is a great tool that allows you to write scripts that can do a variety of different actions on a website (i.e. clicking). This is really import when dealing with websites that are interactive.

The NCCA stats website is one of these types of websites. So in order to retrieve all the data, one would need to select and filter data. After running the script defined [here](https://github.com/logan-connolly/portfolio-posts/blob/issue-1/posts/moneyball_lacrosse/main.py) that does just that, the data extracted from the NCAA look like this:


```
          Team  Conference  Year  Games  Won  Lost  Goals        GPG
0    Air Force        ECAC  2011     13    6     7    117   9.000000
1    Air Force        ECAC  2012     13    6     7    142  10.923077
2    Air Force        ECAC  2013     14    7     7    149  10.642857
3    Air Force        ECAC  2014     17   11     6    199  11.705882
4    Air Force        ECAC  2015     15    8     7    145   9.666667
..         ...         ...   ...    ...  ...   ...    ...        ...
597       Yale  Ivy League  2015     16   11     5    182  11.375000
598       Yale  Ivy League  2016     16   13     3    198  12.375000
599       Yale  Ivy League  2017     16   10     6    207  12.937500
600       Yale  Ivy League  2018     20   17     3    278  13.900000
601       Yale  Ivy League  2019     19   15     4    296  15.578947

Goals Allowed       GAPG Playoffs
          112   8.615385       no
          129   9.923077       no
          136   9.714286       no
          160   9.411765      yes
          131   8.733333       no
          ...        ...      ...
          130   8.125000      yes
          130   8.125000      yes
          165  10.312500      yes
          176   8.800000      yes
          216  11.368421      yes

[602 rows x 11 columns]
```

# Win Predictor

In Mauboussin's article, he uses a win predictor feature derived from the goals for and against per game. The following formula:

`WinPredictor = (0.5 + 0.08 * (Goals_perGame - GoalsAgainst_perGame)) * GamesPlayed`

And here is the reasoning behind Mauboussin's calculation:

> *In plain words, this equation says that goal differential (goals for minus goals against per game) for a season times a constant (α – .08 gives a best fit) added to .500 and then multiplied by the number of games played predicts actual wins (with error term ε).*

This calculation is intuitive because lacrosse is a combination of how efficient your offense is in converting possesions into goals, and how effective your defense is in preventing the other team from scoring on their possessions.


# Modeling

So once we calculate this feature we can create a simple linear model to see how well it predicts the number of games one for the 2019 season. The model will be trained on the 2011-18 seasons.

## Preprocess data

To get the data ready, we need to read in the data scraped from NCAA, calculate the  `WinPredictor` feature, and  split the data into train and test sets. The train set will be the 2011-18 seasons and the test will be the 2019 season:

{{< code language="python" title="Prepare Data" expand="Show" collapse="Hide" isCollapsed="true" >}}
import pandas as pd
from util import calculate_win_predictor, split_data

df = pd.read_csv("data/teams.csv")
df["WinPredictor"] = calculate_win_predictor(df)
train, test = split_data(df)
{{< /code >}}


## Training data

To start, we can train a simple ordinary least squares (ols) model using the [statsmodels](https://www.statsmodels.org/stable/index.html) package using the `Win_Predictor` feature based on Mauboussin's calculation.

{{< code language="python" title="Train Model" expand="Show" collapse="Hide" isCollapsed="true" >}}
import statsmodels.api as sm

X, y = train.WinPredictor, train.Won
model = sm.OLS(y, X).fit()
{{< /code >}}


For those who are not familiar with an OLS model, it basically fits a straight line to the data where the errors are the smallest. You can see the model plotted on the training data below:

{{< load-plotly >}}
{{< plotly json="/plotly/moneyball_lacrosse/model_plot_train.json" height="400px" >}}

As you can see, the model does a pretty decent job at predicting wins in the plot, but we can even get a more detailed view of its performance by looking at the `model.summary()`:

```
                      OLS Regression Results
==============================================================================
   Adj. R-squared:                  0.895
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.7547      0.115      6.548      0.000       0.528       0.981
WinPredictor   0.8911      0.013     66.998      0.000       0.865       0.917
==============================================================================
```

First thing to point out here is that the `WinPredictor` is indeed statistically significant (P>|t| < 0.05) in predicting the actual Wins. Another important is the adjusted R-squared results of 0.895 which means about 89.5% of the variance in the data can be explained by the `WinPredictor` calculation.

# Predict Wins

Now that we have a trained model for predicting wins, let's take the data for the 2019 season, which was not used to train our OLS model and make predictions.

```
    year             team  won       pred
0   2019        Air Force   10  11.038433
1   2019           Albany    5   5.616045
2   2019  Army West Point   13  12.200374
3   2019       Bellarmine    3   3.388993
4   2019       Binghamton    2   1.452425
..   ...              ...  ...        ...
68  2019          Vermont    8   9.005038
69  2019        Villanova    8   6.777985
70  2019         Virginia   17  15.686195
71  2019           Wagner    2   1.742911
72  2019             Yale   15  15.395710

[73 rows x 4 columns]
```

Here is how it looks graphically:


{{< plotly json="/plotly/moneyball_lacrosse/model_plot_test.json" height="400px" >}}


# What Leads to a Win

This shows only the big picture of what makes a team succesful, but it does not tell us what leads a team to win games. Thus we need to individually look at what contributes to a good Offense (efficient possessions that end in goals) and good Defense (possessions that lead to turnovers or saves). 

Predicting the nominal number of wins that a team will win is great in all, but not every team plays the same amount of games. So from now on we are going to concentrate on the variables that effect `WinPct`.

{{< code language="python" title="Win Percentage" expand="Show" collapse="Hide" isCollapsed="true" >}}
df.loc[:, "WinPct"] = round(df.Won / df.Games, 4)
{{< /code >}}

# Offense vs. Defense

We now know that a good offense and defense contributed to a successful season via our `WinPredictor` calculation, but which side of the field is *more* important? To determine this we are going to train to separate OLS models and compare whether Goals per Game or Goals Against per game is more influential on `WinPct`.

## Offense

{{< plotly json="/plotly/moneyball_lacrosse/model_plot_gpg_train.json" height="400px" >}}

```
                            OLS Regression Results
==============================================================================
  Adj. R-squared:                  0.558**
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.2962      0.031     -9.587      0.000      -0.357      -0.235
GPG            0.0780***   0.003     25.830      0.000*      0.072       0.084
==============================================================================
```

It appears from the OLS results that `GPG` is indeed significant`*` and explains roughly 55.8%`**` of the variance in the data. You can interpret the `GPG` coefficient as an increase in 1 goal per game results in a 7.8%`***` increase for a team's `WinPct`.

## Defense

{{< plotly json="/plotly/moneyball_lacrosse/model_plot_gapg_train.json" height="400px" >}}

```
                            OLS Regression Results
==============================================================================
  Adj. R-squared:                  0.477**
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.3108      0.038     34.493      0.000       1.236       1.385
GAPG          -0.0807***   0.004    -21.988      0.000*     -0.088      -0.074
==============================================================================
```

It appears from the OLS results that `GAPG` is also significant`*` and explains roughly 47.7%`**` of the variance in the data. You can interpret the `GAPG` coefficient as an increase in 1 goal against per game results in a 8.1%`***` decrease for a team's `WinPct`.
