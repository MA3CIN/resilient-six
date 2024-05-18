az aks create -n resilientSixCluster -g resilientSixGroup --generate-ssh-keys --attach-acr resilientsixregistry --node-count 2 --enable-managed-identity --enable-addons azure-keyvault-secrets-provider

az aks get-credentials --resource-group resilientSixGroup --name resilientSixCluster

# kubectl apply -f ./yaml .


# kubectl get pods -n kube-system -l 'app in (secrets-store-csi-driver,secrets-store-provider-azure)'
