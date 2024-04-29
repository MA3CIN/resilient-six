# az mysql flexible-server create \
#   --resource-group resilientSixGroup \
#   --name resilientsix-mysql-db \
#   --database-name cache \
#   --admin-user admin_user \
#   --admin-password admin_password \
# 	--location polandcentral \
# 	--tier GeneralPurpose \
# 	--sku-name Standard_D2ads_v5 \
# 	--version 8.0.21 \
#   --yes


az mysql flexible-server create  --resource-group resilientSixGroup  --name resilientsix-mysql-db  --database-name cache  --admin-user admin_user --admin-password admin_password --location polandcentral 	--tier GeneralPurpose 	--sku-name Standard_D2ds_v4 	--version 8.0.21   --yes