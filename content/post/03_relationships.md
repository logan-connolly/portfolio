+++
title = "Reddit Relationships"
date = "2020-05-01"
author = "Logan Connolly"
cover = "/img/relationships/cover.png"
description = "A look into who posts to [/r/relationships](https://www.reddit.com/r/relationships/) and what they post about"
+++

# Introduction

[/r/relationships](https://www.reddit.com/r/relationships/) is a community that provides a platform for interpersonal relationship advice between redditors. They welcome posts from users who have specific and personal relationship issues that other redditors can help them try to solve.

Example posts:

* [*Bf (25M) thinks I'm (25F) overreacting about pandemic safety*](https://www.reddit.com/r/relationships/comments/gb8s1y/bf_26m_thinks_im_25f_overreacting_about_pandemic/)
* [*I (15F) Need Help With My Brother(11M)*](https://www.reddit.com/r/relationships/comments/gb9sdy/i_15f_need_help_with_my_brother11m/)
* [*I (24 F) think my boyfriend (33M) cheated on me with an escort*](https://www.reddit.com/r/relationships/comments/garohd/i_24_f_think_my_boyfriend_33m_cheated_on_me_with/)

Check out the source code of analysis in [Github](). 

# Goal

The goal of this project is to investigate the following questions:

1. **who is posting?** As you can see from the example headlines, there are distinctive patterns in how headlines are created ie. `Bf (25M)`, `my boyfriend (33M)`, `I (24 F)`. Using these patterns, we can extract valuable information like:
	* author of post's sex and age
	* subject of post's sex and age
	* relationship between author and subject

2. once we know **who is posting**, we can find out:
	* what types of relationships occur most often (gf, bf, mom, dad, etc.)
	* who posts more: males or females?
	* how old are the people posting?

3. lastly, we want to investigate the **content of the post**. To do this we will extract topics from the post. For this, we will need to analyze the post's text and classify them into categories.
