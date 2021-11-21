Hi Team,

For the Task 2 , I have created the single YAML file to include both the deployment and servie specifications

The deployment will spin-up/keep one POD as the replica set to 1

The service uses ClusterIP as a kind as mentioned.

Please note :

* I assume that a kubernetes cluster is already set-up and the nginx-deployment.yml can be directly used to create a deployment/ service.

* We need to first create a name space with name "nginx" as I wanted to keep these with respective name space (not on defult)

* For my test I hae deployed this in GKE as I go not have self managed cluster ready with me.

kubectl create namespace nginx

![This is an image](/assets/7.png)


kubectl create -f deployment.yml

Once the deployment gets executed, check the deployment

kubectl get deployments -n nginx

![This is an image](/assets/8.png)

* There are 2 PODS in the deployment, reason for this is, I have added another container to test a multiple replica scenario.

Check the pods

kubectl get pods -n nginx

![This is an image](/assets/9.png)


Check the service nginx 

kubectl describe service nginx -n nginx

![This is an image](/assets/10.png)


Test to validate the nginx container. as a quick test, spin-up another pod (I used ubuntu container) and addess using cluster IP to the nginx pod


![This is an image](/assets/11.png)




Regards,
Pradeep