#!/bin/sh
# This is a comment!
echo "DELETE Cluster"
export GOOGLE_APPLICATION_CREDENTIALS=/home/bladeaico/security/blade-ai-282114-aedee4bdb9d8.json
export workspace=/home/bladeaico/blai/k8s
echo "Deleting cluster: $(terraform destroy -auto-approve $workspace)"
