# ocasionally on Linux this gets very wonky. I recommend logging in before running the script
#az login

az group create --name resilientSixGroup --location polandcentral

az acr create --resource-group resilientSixGroup --name resilientsixregistry --sku Basic

az acr login --name resilientsixregistry
