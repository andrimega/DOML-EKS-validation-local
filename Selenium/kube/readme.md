## Usage
Prima di tutto creare il namespace
kubectl apply -f selenium-namespace.yaml

Poi creare l'hub e successivamente i nodes
kubectl apply -f selenium-hub.yaml 
kubectl apply -f selenium.yaml

Infine deployare lo scraper
kubectl apply -f scraper.yaml

Per autoscaling
Crea prometheus
kubectl apply -f namespace.yaml
kubectl apply -f config.yaml
kubectl apply -f prometheus-server.yaml
kubectl apply -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/main/bundle.yaml

Crea exporter, monitor e scaler
kubectl apply --server-side -f https://github.com/kedacore/keda/releases/download/v2.13.0/keda-2.13.0.yaml
    se kubectl logs -n keda -l app=keda-operator da errore
    kubectl edit apiservice v1beta1.external.metrics.k8s.io
        spec:
    insecureSkipTLSVerify: false
kubectl apply -f exporter.yaml
kubectl apply -f monitor.yaml
kubectl apply -f keda-scaler.yaml
