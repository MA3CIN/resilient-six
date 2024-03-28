# Install all dependencies
``` pip install -r requirements.txt ``` 

# Containerize and push services
``` docker build -t <repo name>:<tag version> . ```
``` docker build -t marcinziolkowski/infra-service:v1.0.1 . ```

``` docker push marcinziolkowski/infra-service:v1.0.1 . ```