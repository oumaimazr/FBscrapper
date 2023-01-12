# FBscrapper

This app aims to scrap a given public facebook page.

- Using selenium and beautiful soup we get to scrap the poster, the date of posting and the content of the post.
- This API is build using FastAPI and the scrapped data is stored in a mondb cluster.
- This repository contains a requirement.txt file that contains the required python libraries needed for this project, a main.py containing the project's code, a facebook cookies extracted form google chrome browser using get cookies extension , a Dockerfile that can be used to build a docker for the API and a docker-compose file to setting up a MongoDB container.
