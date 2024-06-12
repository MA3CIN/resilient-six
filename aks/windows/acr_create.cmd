az group create --name resilientSixGroup --location polandcentral

az acr create --resource-group resilientSixGroup --name resilientsixregistry --sku Basic

az acr login --name resilientsixregistry
