# get K8s metrics server: ALL FILES!
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


kubectl patch -n kube-system deployment metrics-server --type=json \
  -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
  
# https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

# https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/