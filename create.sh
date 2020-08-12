#!/bin/sh
# This is a cdomment!
export GOOGLE_APPLICATION_CREDENTIALS=/home/bladeaico/security/blade-ai-282114-aedee4bdb9d8.json
echo "creating k8s cluster"
export workspace=/home/bladeaico/blai/k8s
echo "Creating terraform cluster: $(terraform init $workspace)"
echo "Applying  terraform $(terraform apply -auto-approve  $workspace)"
