# Cluster Manager

Version : 1

## Requirements
python: > 3.5

## Setup
Create a cloud VM (here we use GCP Debian 9)
Install python 
sudo apt update
sudo apt install python3 python3-dev python3-venv

### Local dev environment
execute the following in the console terminal within the directory

##### Install dependencies
1. pip3 install -r requirements.txt

##### Running server

1. uvicorn main:app --reload --host 0.0.0.0 --port 8000
2. Server now running on http://localhost:8000

### Deployment
link to deployment instructions and creating docker containers
https://fastapi.tiangolo.com/deployment/
