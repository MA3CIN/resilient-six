az keyvault create --name resilientsixkeyvault3 --resource-group resilientSixGroup --location polandcentral

az keyvault secret set --vault-name resilientsixkeyvault3 --name DB-URL --value resilientsix-mysql-db.mysql.database

az keyvault secret set --vault-name resilientsixkeyvault3 --name DB-USER --value admin_user

az keyvault secret set --vault-name resilientsixkeyvault3 --name DB-PSWD --value admin_password