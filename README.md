# Multi-tier-app
### Topology
![Topology](./myshop/images/flow.png)

# Procedure.
 To bring up all the pods and services, Run the following script. <br />
 `./run_all.sh`

 This should bring up all the pods. You can monitor it using: <br />
 ```
kubectl get pods -o wide
kubectl get svc
```
# Taint and untaint a node.
You can taint or untaint a node from a master using the following scripts.
```
[root@5b6s16 ~]# kubectl get nodes
NAME                     STATUS     ROLES     AGE       VERSION
5b6s16                   NotReady   master    4d        v1.9.2
5b6s17                   Ready      <none>    4d        v1.9.2
sanfrancisco-compute-1   Ready      <none>    17h       v1.9.2
```

To taint a node named `sanfrancisco-compute-1` use:

```
cd Multi-tier-app/
./taint_nodes.sh sanfrancisco-compute-1
```

To untaint the same node use:
```
cd Multi-tier-app/
./untaint_nodes.sh sanfrancisco-compute-1
```

To delete all pods except the frontend, use the following script:
```
cd Multi-tier-app/
./delete_pods.sh
```
