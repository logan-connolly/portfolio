from diagrams import Cluster, Diagram
from diagrams.programming.language import Python, Rust
from diagrams.programming.framework import Vue
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

graph_attr = {
    "bgcolor": "transparent"
}

with Diagram("Basic Architecture", outformat="png", graph_attr=graph_attr):

    with Cluster("Docker Swarm"):
        host = [
            Server("Cloud Host")
        ]

    with Cluster("Frontend"):
        frontend = Vue("Nuxt + Vuetify")
        host << frontend

    with Cluster("Search Engine"):
        search = Rust("MeiliSearch")
        frontend << search

    with Cluster("API"):
        api = Python("FastAPI")
        search >> api
        api >> search

    with Cluster("Database"):
        db = PostgreSQL("Recipes")
        api >> db
        db >> api

    with Cluster("Web Scraper"):
        scraper = Python("Scrapy")
        scraper >> api
