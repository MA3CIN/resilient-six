# az aks create -n resilientSixCluster -g resilientSixGroup --generate-ssh-keys --attach-acr resilientsixregistry --node-count 2 --enable-managed-identity --enable-addons azure-keyvault-secrets-provider

az network vnet subnet create \
  --resource-group resilientSixGroup \
  --vnet-name vnet-resilientsix \
  --name aks-subnet \
  --address-prefixes 10.25.2.0/24

SUBNET_ID=$(az network vnet subnet show --resource-group resilientSixGroup --vnet-name vnet-resilientsix --name aks-subnet --query id -o tsv)

az aks create \
  --resource-group resilientSixGroup \
  --name resilientSixCluster \
  --network-plugin azure \
  --service-cidr 10.0.0.0/16 \
  --dns-service-ip 10.0.0.10 \
  --vnet-subnet-id $SUBNET_ID \
  --attach-acr resilientsixregistry \
  --dns-name-prefix resilientSixCluster \
  --generate-ssh-keys \
  --node-count 2

az aks get-credentials --resource-group resilientSixGroup --name resilientSixCluster

# kubectl apply -f ./yaml .
# kubectl get pods -n kube-system -l 'app in (secrets-store-csi-driver,secrets-store-provider-azure)'
