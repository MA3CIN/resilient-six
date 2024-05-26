#az keyvault create --name resilientsixkeyvault --resource-group resilientSixGroup --location polandcentral --enable-rbac-authorization
# RBAC is a pain in the ass unfortunately :)


az keyvault create --name resilientsixkeyvault2 --resource-group resilientSixGroup --location polandcentral

az keyvault secret set --vault-name resilientsixkeyvault2 --name DB_URL --value resilientsix-mysql-db.mysql.database

az keyvault secret set --vault-name resilientsixkeyvault2 --name DB_USER --value admin_user

az keyvault secret set --vault-name resilientsixkeyvault2 --name DB_PSWD --value admin_password