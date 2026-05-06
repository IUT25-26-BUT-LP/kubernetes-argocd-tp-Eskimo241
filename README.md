# kubernetes-argocd-tp-Eskimo241

to create the cluster & namespace: kind create cluster --config kind-config.yaml

kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

wait for pending pods

kubectl port-forward svc/argocd-server -n argocd 8080:443
