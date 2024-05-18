az login

az group create --name resilientSixGroup --location polandcentral

az network vnet create \
  --resource-group resilientSixGroup \
  --name vnet-resilientsix \
  --address-prefixes 10.25.0.0/16 \
  --subnet-name mysql-subnet \
  --subnet-prefix 10.25.1.0/24
# vnet dedicated to mysql flexible server - WARNING: DO NOT USE FOR ANYTHING ELSE

az mysql flexible-server create \
  --name resilientsix-mysql-db \
  --resource-group resilientSixGroup \
  --location polandcentral \
  --admin-user admin_user \
  --admin-password admin_password \
  --vnet vnet-resilientsix \
  --subnet mysql-subnet \
  --tier GeneralPurpose \
  --sku-name Standard_D2ds_v4 \
  --version 8.0.21 \
  --yes
# Do you want to create a new private DNS zone resilientsix-mysql-db.private.mysql.database.azure.com in resource group resilientSixGroup (y/n)

az mysql flexible-server db create \
  --resource-group resilientSixGroup \
  --server-name resilientsix-mysql-db \
  --database-name cache

az mysql flexible-server db create \
  --resource-group resilientSixGroup \
  --server-name resilientsix-mysql-db \
  --database-name geolocation

az mysql flexible-server db create \
  --resource-group resilientSixGroup \
  --server-name resilientsix-mysql-db \
  --database-name devices

az mysql flexible-server db create \
  --resource-group resilientSixGroup \
  --server-name resilientsix-mysql-db \
  --database-name statistics