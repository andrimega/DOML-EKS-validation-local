# Intro
This app is meant to be a test for the autoscaling capabilities of a web server in kubernetes.
The web server is a SPA that generates a random number. 

The `docker` folder contains the source code used to generate the docker image for the website.
The `kube` folder contains code and instrauctions used to deploy the container and other resources on the cluster.
The `test` folder contains the results of the stress test

## Usage
1. Generate the docker image, upload to the docker repository.
2. Deploy on kubernetes the metric-server, the SWS container and the autoscaler.
3. Run stress test and log results.