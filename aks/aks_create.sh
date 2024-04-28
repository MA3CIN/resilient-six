az aks create -n resilientSixCluster -g resilientSixGroup --generate-ssh-keys --attach-acr resilientsixregistry --node-count 2

az aks get-credentials --resource-group resilientSixGroup --name resilientSixCluster

# kubectl apply -f ./yaml .