# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-23T10:36:05-07:00
# @Email:  agupta@juniper.net
# @Filename: run_all.sh
# @Last modified by:   agupta
# @Last modified time: 2018-10-23T10:37:37-07:00
kubectl apply -f rabbitmq-deployment
kubectl apply -f rabbitmq-service
kubectl apply -f redis-deployment
kubectl apply -f redis-service
kubectl apply -f celery-deployment
kubectl apply -f python-service
kubectl apply -f python-deployment
