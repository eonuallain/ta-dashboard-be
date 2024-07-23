# rot13-dashboard

## Pull docker image
```
docker pull ghcr.io/eonuallain/rot13-dashboard:main
```

## Run docker image
```
docker run -p5000:5000 ghcr.io/eonuallain/rot13-dashboard:main
```

## Install chart
```
helm install rot13-dashboard ./chart
```

## Uninstall chart
```
helm uninstall rot13-dashboard
```

## minikube show service URL
```
minikube service rot13-dashboard --url
```
