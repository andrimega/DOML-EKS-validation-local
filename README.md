# DOML-EKS-validation-local
Private repository to test locally the applications that will be used to validate the DOML EKS extension

The validation revolves around 3 tests:

## Scalable Web Server
A simple nginx web server, serving a single page application. The page contains a number that is randomly generated every time the page is loaded.
The web server is hosted in a Kubernetes pod with autoscaling capabilities. The server will scale up when too many requests are generated.

## Selenium Grid
A selenium grid with autoscaling hosted on Kubernetes. The application will perform scraping on the SWS, and collect the average of the scraped value. A stress test will allow scaling up to 100 nodes, the hope is to stress also the server in order to cause autoscaling.

## Cassandra
https://github.com/kubernetes/examples
