# Cluster Manager

Version : 1

## Requirements
python: > 3.5

## Setup

### 1. Local dev environment
execute the following in the console terminal within the directory

##### Install dependencies
1. pip3 install -r requirements.txt

##### Running Local Environment Test instruction
1. Open test.py in text editor
2. uncomment the lines to test CREATE and SHUTDOWN
3. run 'python test.py' in terminal

##### Running server

1. uvicorn main:app --reload --host 0.0.0.0 --port 8000
2. Server now running on http://localhost:8000

### 2. GCP Compute engine environment

### On google cloud shell execute the following to create a cluster manager vm, this will spin up a new VM that will spin up the API on port 8000
gcloud beta compute instances create bladeai-clustermanager \
    --project=blade-ai-282114 \
    --zone=europe-west1-b \
    --source-machine-image projects/blade-ai-282114/global/machineImages/bladeai-clustermanager-image \
    --service-account terraform-spinup@blade-ai-282114.iam.gserviceaccount.com

#### This command will return an output similar to :
#### NAME                            ZONE            MACHINE_TYPE  PREEMPTIBLE  INTERNAL_IP   EXTERNAL_IP   STATUS
#### bladeai-clustermanager-image-1  europe-west1-b  g1-small      true         XX.XX.XX.XXX  XX.XX.XX.XXX  RUNNING

Server now is running on http://EXTERNAL_IP:8000

### Deployment
link to deployment instructions and creating docker containers
https://fastapi.tiangolo.com/deployment/
