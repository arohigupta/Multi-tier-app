kubectl delete pods $(kubectl get pods| awk '{print $1}' | grep -v "NAME" | grep -v "python")
