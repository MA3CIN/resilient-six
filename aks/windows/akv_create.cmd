az keyvault create --name resilientsixkeyvault2 --resource-group resilientSixGroup --location polandcentral

az keyvault secret set --vault-name resilientsixkeyvault2 --name ExampleSecret --value MyAKSExampleSecret
