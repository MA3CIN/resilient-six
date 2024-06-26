az network vnet create   --resource-group resilientSixGroup --name vnet-resilientsix   --address-prefixes 10.25.0.0/16   --subnet-name mysql-subnet   --subnet-prefix 10.25.1.0/24

az mysql flexible-server create   --name resilientsix-mysql-db2  --resource-group resilientSixGroup   --location polandcentral   --admin-user admin_user --admin-password admin_password   --vnet vnet-resilientsix   --subnet mysql-subnet   --tier GeneralPurpose   --sku-name Standard_D2ds_v4   --version 8.0.21   --yes

# az mysql flexible-server db create  --resource-group resilientSixGroup --server-name resilientsix-mysql-db  --database-name cache

az mysql flexible-server db create  --resource-group resilientSixGroup   --server-name resilientsix-mysql-db2   --database-name geolocation

az mysql flexible-server db create   --resource-group resilientSixGroup   --server-name resilientsix-mysql-db2   --database-name devices

az mysql flexible-server db create   --resource-group resilientSixGroup   --server-name resilientsix-mysql-db2  --database-name statistics


# mysql -u admin_user -padmin_password -h resilientsix-mysql-db2.mysql.database devices

# source databases/devices_db_schema.sql
# source databases/devices_sample_data.sql