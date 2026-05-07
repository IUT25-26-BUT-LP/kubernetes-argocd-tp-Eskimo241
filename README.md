# kubernetes-argocd-tp-Eskimo241

to create the cluster & namespace: kind create cluster --config kind-config.yaml

kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

wait for pending pods

kubectl port-forward svc/argocd-server -n argocd 8080:443

kubectl apply -f app/argocd-app.yaml



kyverno :
kubectl create namespace kyverno
kubectl apply -f https://github.com/kyverno/kyverno/releases/latest/download/install.yaml

kubectl apply -f kyverno-policy.yaml



docker registry : 
docker run -d -p 5000:5000 --restart=always --name local-registry 10.6.0.190:80/proxy/registry:2
docker network connect kind local-registry