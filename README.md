# Cluster Manager

Version : 1

## Requirements
python: > 3.5

## Setup

### Local dev environment
execute the following in the console terminal within the directory

##### Install dependencies
1. pip3 install -r requirements.txt

##### Running server

1. uvicorn main:app --reload --host 0.0.0.0 --port 8000
2. Server now running on http://localhost:8000


## Setup
### GCP Compute engine environment
### ON GCP execute the following to create a cluster manager vm, this will spin up a new VM that will spin up the API on port 8000
gcloud beta compute --project=blade-ai-282114 instances create bladeai-clustermanager --zone=europe-west1-b --machine-type=g1-small --subnet=default --network-tier=PREMIUM --metadata=startup-script=\#\!\ /bin/bash$'\n'cd\ /home/bladeaico/blaid-cluster-manger$'\n'echo\ \"\$\(ls\ /home/bladeaico/blaid-cluster-manger\)\"$'\n'echo\ \"\$\(/home/bladeaico/.pyenv/bin/pyenv\ versions\)\"$'\n'/home/bladeaico/.pyenv/bin/pyenv\ global\ 3.7.2$'\n'/home/bladeaico/.pyenv/shims/pip3\ install\ -r\ requirements.txt$'\n'nohup\ /home/bladeaico/.pyenv/shims/uvicorn\ main:app\ --reload\ --host\ 0.0.0.0\ --port\ 8000\ \& --no-restart-on-failure --maintenance-policy=TERMINATE --preemptible --service-account=terraform-spinup@blade-ai-282114.iam.gserviceaccount.com --scopes=https://www.googleapis.com/auth/cloud-platform --min-cpu-platform=Automatic --tags=freeworld,http-server,https-server --labels=node=clustermanager --reservation-affinity=any

### Deployment
link to deployment instructions and creating docker containers
https://fastapi.tiangolo.com/deployment/
