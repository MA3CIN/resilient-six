#!/bin/sh
# Build all 3 services, re-tag them and push to ACR
# PARAMETER = TAG of image

if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided"
    exit 1
fi


# geo service
docker build -t resilientsixregistry.azurecr.io/geo-service:v1.0.3 ../services/geo-service/.
docker push resilientsixregistry.azurecr.io/geo-service:v1.0.3

# infra service
docker build -t resilientsixregistry.azurecr.io/infra-service:v1.0.3 ../services/infra-service/.
docker push resilientsixregistry.azurecr.io/infra-service:v1.0.3

# stats service
docker build -t resilientsixregistry.azurecr.io/stats-service:v1.0.3 ../services/stats-service/.
docker push resilientsixregistry.azurecr.io/stats-service:v1.0.3