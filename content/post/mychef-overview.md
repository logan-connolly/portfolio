+++
title = "MyChef Recipe Recommender"
date = "2020-10-02"
author = "Logan Connolly"
keywords = ["python", "vue", "scrapy", "spacy"]
tags = ["python", "vue", "scrapy", "spacy"]
description = "App that tells you what to make based on what you have in the kitchen"
+++

# What is MyChef?

An application developed to help you decide what to cook based on what you have in the kitchen. It is able to do this by scraping recipes from the best plant-based recipe sites on the web and bringing them together in one place. The search engine built into the application ranks the recipes based on the ingredients that you enter.

# Architecture

From a bird's eye view, the basic application architecture looks like:

![](/img/mychef_overview/basic_architecture.png)

# Tools

General:

- [Docker](https://www.docker.com/): for containerization of microservices
- [PostgreSQL](https://www.postgresql.org/): relational database for storing recipe information
- [Scrapy](https://scrapy.org/): a python library for scraping recipes from websites

API:

- [FastAPI](https://fastapi.tiangolo.com/): a python async api framework that is fast and super easy to use
- [Spacy](https://spacy.io/): a python library for nlp that comes with a bunch of great pre-trained language models
- [MeiliSearch](https://docs.meilisearch.com/) batteries included search engine developed in Rust

UI:

- [Nuxt](https://nuxtjs.org/): a js framework built on [Vue](https://vuejs.org/) for creating reactive sites with server side rendering
- [Vuetify](https://vuetifyjs.com/en/): bootstrap like js framework for creating pretty components

# Find out more

The website is not yet deployed, but visit https://github.com/logan-connolly/mychef to see the current status of the project.
