az aks create -n resilientSixCluster -g resilientSixGroup --generate-ssh-keys --attach-acr resilientsixregistry --node-count 2 --enable-managed-identity --enable-addons azure-keyvault-secrets-provider --enable-addons open-service-mesh

az aks get-credentials --resource-group resilientSixGroup --name resilientSixCluster