# Svelte.js + Flask Python Background Jobs and Web Spider

A super simple example of using Flask to serve a Svelte app and use it as a backend server. It run and rq, scrapy, selenium to perform queueing jobs and processing them in the background with workers.

Stack:

- Python
- Flask
- Svelte
- Docker
- Scrapy
- Selenium
- Redis
- [rq](https://python-rq.org/)

# 
Run the following for development:

- `python server.py` to start the Flask server.
- `cd client; npm install; npm run autobuild` to automatically build and reload the Svelte frontend when it's changed.

YOu can also run the worker node in docker container:

`docker compose worker up`