az network vnet subnet create \
  --resource-group resilientSixGroup \
  --vnet-name vnet-resilientsix \
  --name aks-subnet \
  --address-prefixes 10.25.2.0/25

SUBNET_ID=$(az network vnet subnet show --resource-group resilientSixGroup --vnet-name vnet-resilientsix --name aks-subnet --query id -o tsv)

az aks create \
  --resource-group resilientSixGroup \
  --name resilientSixCluster \
  --network-plugin azure \
  --service-cidr 10.0.0.0/16 \
  --dns-service-ip 10.0.0.10 \
  --docker-bridge-address 172.17.0.1/16 \
  --vnet-subnet-id $SUBNET_ID \
  --attach-acr resilientsixregistry \
  --dns-name-prefix resilientSixCluster \
  --generate-ssh-keys \
  --node-count 2
# Option '--docker-bridge-address' has been deprecated and will be removed in a future release.

az aks get-credentials --resource-group resilientSixGroup --name resilientSixCluster

# kubectl apply -f ./yaml .