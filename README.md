# FBscrapper

This app aims to scrap a given public facebook page.

- Using selenium and beautiful soup we get to scrap the poster, the date of posting and the content of the post.
- This API is build using FastAPI and the scrapped data is stored in a mondb cluster.
- This repository contains a requirements.txt file that contains the required python libraries needed for this project, a main.py containing the project's code, a Dockerfile that can be used to build a docker for the API and a docker-compose file to setting up a MongoDB container.

#Test the API

Please find below the tests that you can try after setting the environment

This request would scrap posts from the page “linkedin”
http://127.0.0.1:8000/scrap/?page=linkedin&limit=2&save=false

This request would scrap and save the posts in the database
http://127.0.0.1:8000/scrap/?page=linkedin&limit=3&save=true

This request would show all the data that we scrapped from the database
http://127.0.0.1:8000/load/
