az network vnet subnet create   --resource-group resilientSixGroup   --vnet-name vnet-resilientsix   --name aks-subnet  --address-prefixes 10.25.2.0/24

SUBNET_ID=$(az network vnet subnet show --resource-group resilientSixGroup --vnet-name vnet-resilientsix --name aks-subnet --query id -o tsv)

az aks create -n resilientSixCluster -g resilientSixGroup --generate-ssh-keys --network-plugin azure --attach-acr resilientsixregistry --node-count 2 --enable-managed-identity --enable-addons azure-keyvault-secrets-provider --enable-addons open-service-mesh --service-cidr 10.0.0.0/16 --service-cidr 10.0.0.0/16   --dns-service-ip 10.0.0.10  --vnet-subnet-id $SUBNET_ID  --dns-name-prefix resilientSixCluster

az aks enable-addons --addons azure-keyvault-secrets-provider --name resilientSixCluster --resource-group resilientSixGroup

az aks get-credentials --resource-group resilientSixGroup --name resilientSixCluster

# kubectl create ns mesh-ns

# osm namespace add mesh-ns

# kubectl apply -f ./yaml .


# kubectl get pods -n kube-system -l 'app in (secrets-store-csi-driver,secrets-store-provider-azure)'
