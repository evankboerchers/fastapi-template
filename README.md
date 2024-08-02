<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>

<h1 align="center">Project Template</h1>

<b>Want to build a new API server but dont know where to start? Looking to learn an awesome new framework? Need a backend stack to quickly develop an API for your new project?</b>

This projects provides you an out of the box API service that demonstrates the wonders of [FastApi](https://fastapi.tiangolo.com/). This codebase provides the needed basics and some useful goodies out of the box. Simply clone this repository and customize to your own needs and requirements!

## Features

## Getting Started

### Requirements
1. Python 3.12 or greater
    - python3.XX-venv for virtual environment
2. Docker for postgresql container

### Setup

1. Create a virtual environment `python3 -menv venv ./venv/`
2. Activate env and install requirements
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
2. Setup database
    - Start docker container `docker compose up -d`
    - Setup and populate sample data `python3 ./scripts/populate_db.py`

### Running
1. Run database container `docker compose up -d`
2. Start fast app `fastapp dev`
3. Take a look at the api spec http://localhost:8000/docs 

## Future Additions
- Cleaner setup script
- Run app in docker container
- Authentication
    - Certain db access per user
    - only see own salaries/if admin
- Testing
- Error handling
- Logging
- db session pool
- pagination

## License
This project is licensed under the terms of the MIT license.