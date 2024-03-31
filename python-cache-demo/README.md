# Install all dependencies
``` pip install -r requirements.txt ``` 

# Containerize and push services
``` docker build -t <repo name>:<tag version> . ```
``` docker build -t marcinziolkowski/infra-service:v1.0.1 . ```

``` docker push marcinziolkowski/infra-service:v1.0.1 . ```

# Docker compose - bring up the whole project in 1 command

```docker compose up ```

```docker compose down ```

```docker compose up --build ```