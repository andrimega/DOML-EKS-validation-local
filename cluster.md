This file contains informations about the cluster used for the tests.
The cluster was run using minikube

## Setup
Install minikube and kubectl.
Start docker desktop.
Create the cluster with:
    minikube start --cpus=4 --memory=4096 --driver=docker
then run:
    sudo minikube tunnel
