kubeadm reset

cp /root/10-contrail.conf /etc/cni/net.d/

kubeadm join 172.16.65.154:6443 --token $1 --discovery-token-unsafe-skip-ca-verification --ignore-preflight-errors=cri,ca-crt

systemctl start kubelet
