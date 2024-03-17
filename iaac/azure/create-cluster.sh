# REQUIRES AZURE CLI!
# Create an SSH key pair using Azure CLI
az sshkey create --name "mySSHKey" --resource-group "myResourceGroup"

# Create an SSH key pair using ssh-keygen
ssh-keygen -t rsa -b 4096


# Create cluster
az deployment group create --resource-group myResourceGroup --template-file main.bicep --parameters dnsPrefix=<dns-prefix> linuxAdminUsername=<linux-admin-username> sshRSAPublicKey='<ssh-key>'
