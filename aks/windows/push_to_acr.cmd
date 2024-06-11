docker build -t resilientsixregistry.azurecr.io/geo-service:v2.0.3 ../../services/geo-service/.
docker push resilientsixregistry.azurecr.io/geo-service:v2.0.3

docker build -t resilientsixregistry.azurecr.io/infra-service:v2.0.3 ../../services/infra-service/.
docker push resilientsixregistry.azurecr.io/infra-service:v2.0.3

docker build -t resilientsixregistry.azurecr.io/stats-service:v2.0.3 ../../services/stats-service/.
docker push resilientsixregistry.azurecr.io/stats-service:v2.0.3