from diagrams import Cluster, Diagram
from diagrams.programming.language import Python
from diagrams.programming.framework import Vue
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx

graph_attr = {
    "bgcolor": "transparent"
}

with Diagram("Basic Architecture", outformat="png", graph_attr=graph_attr):
    ingress = Nginx("Web Server")

    with Cluster("Service Cluster"):
        gcp = [
            Server("GCP")
        ]

    with Cluster("Frontend"):
        frontend = Vue("Vue + Vuetify")
        gcp >> frontend

    with Cluster("API"):
        api = Python("FastAPI")
        frontend >> api

    with Cluster("Database"):
        db = PostgreSQL("Recipes")
        api >> db

    with Cluster("Web Scraper"):
        scraper = Python("Scrapy")
        ingress >> gcp >> scraper >> api
