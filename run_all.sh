# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-23T10:36:05-07:00
# @Email:  agupta@juniper.net
# @Filename: run_all.sh
# @Last modified by:   agupta
# @Last modified time: 2018-10-23T10:37:37-07:00
kubectl apply -f rabbitmq-deployment.yaml
kubectl apply -f rabbitmq-service.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
kubectl apply -f celery-deployment.yaml
kubectl apply -f python-service.yaml
kubectl apply -f python-deployment.yaml
