# get K8s metrics server: ALL FILES!
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


kubectl patch -n kube-system deployment metrics-server --type=json \
  -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
  
helm repo add chaos-mesh https://charts.chaos-mesh.org

kubectl create ns chaos-mesh

# Change socket to containerd for kind
helm install chaos-mesh chaos-mesh/chaos-mesh -n=chaos-mesh --version 2.6.3 --set dashboard.securityMode=false --set chaosDaemon.runtime=containerd --set chaosDaemon.socketPath=/run/containerd/containerd.sock

kubectl apply -f infra-deploy.yaml

kubectl apply -f infra-hpa.yaml

# kubectl apply -f chaos-mesh/stress.yaml