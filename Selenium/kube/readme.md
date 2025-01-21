## Usage
Prima di tutto creare il namespace
kubectl apply -f selenium-namespace.yaml

Poi creare l'hub e successivamente i nodes
kubectl apply -f selenium-hub.yaml 
kubectl apply -f selenium.yaml

Infine deployare lo scraper
kubectl apply -f scraper.yaml

Per autoscaling
kubectl apply -f https://github.com/kedacore/keda/releases/download/v2.8.0/keda-2.8.0.yaml
kubectl apply -f keda-scaler.yaml


