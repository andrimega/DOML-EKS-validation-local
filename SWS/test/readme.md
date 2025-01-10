## Usage
To run stress test:
hey -z 1m -c 50 http://10.100.190.33

To see results:
kubectl get pods -w
kubectl describe hpa