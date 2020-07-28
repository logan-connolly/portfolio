+++
title = "MyChef Recipe Recommender"
date = "2020-03-20"
author = "Logan Connolly"
cover = "/img/mychef_overview/cover.jpg"
description = "Creating an app that finds recipes based on what I have in the kitchen"
+++

# Goal of MyChef

The goal of the application is to help you decide what to cook based on what you have in the kitchen. This is also an excellent opportunity to develop software development skills, in particular how to develop microservices and bring them together into one application.

Following this post, there will be series of articles detailing how you can bring such an application to life: 

* Setting up services with docker compose
* Designing the API 
* Building a web scraper
* Using natural language processing (nlp) to extract ingredients from recipe text
* Develop UI to recommend recipes based on ingredients
* Deploy application using nginx webserver

# Tools

The main tools that I will be using throughout this series are:

All:
* [Docker](https://www.docker.com/): for containerization of microservices
* [PostgreSQL](https://www.postgresql.org/): relational database for storing recipe information
* [Scrapy](https://scrapy.org/): a python library for scraping recipes from websites

API:
* [FastAPI](https://fastapi.tiangolo.com/): a python async api framework
* [Spacy](https://spacy.io/): a python library for nlp 

UI:
* [Vue](https://vuejs.org/): a js framework for creating reactive component based frontends
* [Vuetify](https://vuetifyjs.com/en/): bootstrap like js framework for creating components

# Architecture

When put all together, the basic application architecture looks like:

![](/img/mychef_overview/basic_architecture.png)

I generated the above image using the handy `diagrams` package. Check out how I created it here: https://github.com/mingrammer/diagrams.

In the next post, we will setup the development environment that we will use to build the app using docker. Stay tuned!
