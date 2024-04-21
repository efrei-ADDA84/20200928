# RAPPORT TP4

Installation de TERRAFORM :
brew tap hashicorp/tap
brew install hashicorp/tap/terraform


Installation de Azure CLI :
brew update && brew install azure-cli


Connexion à Azure avec l'Azure CLI :
az login


Création clé SSH :
ssh-keygen -t rsa -b 4096 -C "mordjane.aribi@efrei.net"


Your identification has been saved in /Users/mordjanearibi/.ssh/id_rsa
Your public key has been saved in /Users/mordjanearibi/.ssh/id_rsa.pub

Connaitre l'adresse du sous-réseau :
az network vnet subnet show --name internal --resource-group ADDA84-CTP --vnet-name network-tp4 --query "addressPrefix"


### Il faut ensuite importer des ressources existantes dans le state de Terraform avant de pouvoir les gérer avec Terraform.

Importer la ressource azurerm_public_ip :
terraform import azurerm_public_ip.myvmip /subscriptions/765266c6-9a23-4638-af32-dd1e32613047/resourceGroups/ADDA84-CTP/providers/Microsoft.Network/publicIPAddresses/my-public-ip

Importer la ressource azurerm_subnet :
terraform import azurerm_subnet.internal /subscriptions/765266c6-9a23-4638-af32-dd1e32613047/resourceGroups/ADDA84-CTP/providers/Microsoft.Network/virtualNetworks/network-tp4/subnets/internal


Créer l'interface réseau "devops-20200928" :
az network nic create \
    --resource-group ADDA84-CTP \
    --name devops-20200928 \
    --vnet-name network-tp4 \
    --subnet internal

Importe la ressource existante dans le state Terraform :
terraform import azurerm_network_interface.myvmnic /subscriptions/765266c6-9a23-4638-af32-dd1e32613047/resourceGroups/ADDA84-CTP/providers/Microsoft.Network/networkInterfaces/devops-20200928


### Problemes rencontrés : 
Supprimer l'adresse IP publique de la configuration IP de l'interface réseau :
az network nic ip-config update --name myNicConfiguration --nic-name my-nic --resource-group ADDA84-CTP --public-ip-address null


Problème de location rencontré pour la création de la VM :
az vm image list : liste des iamges disponibles
La modification des paramètres dans "source_image_reference" m'a permis de régler le problème.


## Commande terraform à utiliser :

- terraform init
- terraform plan
- terraform apply
- terraform destroy

