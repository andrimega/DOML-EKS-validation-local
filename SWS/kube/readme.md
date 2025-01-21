## Resources
List of resources to deploy on the cluster.

metric-server: 
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    check with: kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
    edit the deployment with: 
        kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{
            "op": "add",
            "path": "/spec/template/spec/containers/0/args",
            "value": [
                "--kubelet-insecure-tls",
                "--kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname",
                "--cert-dir=/tmp",
                "--secure-port=10250",
                "--kubelet-use-node-status-port",
                "--metric-resolution=15s"
            ]
        }]'

SWS: 
    kubectl apply -f sws.yaml
