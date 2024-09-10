# TA-Dashboard

## Install pipx
```
sudo apt install -y pipx
pipx ensurepath
eval "$(register-python-argcomplete pipx)"
```

## Install poetry
```
pipx install poetry
poetry completions bash >> ~/.bash_completion
```

## Poetry run lint and start flask app
```
poetry shell
poetry run pylint ta/
poetry run flask --app ta run --debug
```

## Run flask app locally
```
flask --app ta run --debug
```

## Pull docker image
```
docker pull ghcr.io/eonuallain/ta-dashboard:main
```

## Run docker image
```
docker run -p5000:5000 ghcr.io/eonuallain/ta-dashboard:main
```

## Install minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube start
```

## Install chart
```
helm install ta-dashboard ./chart
```

## Uninstall chart
```
helm uninstall ta-dashboard
```

## minikube show service URL
```
minikube service ta-dashboard --url
```

## Install postgres
```
helm repo add bitnami https://charts.bitnami.com/bitnami

helm install pg-minikube --set auth.postgresPassword=<your-postgres-password> bitnami/postgresql
```

## Install postgres output
```
NAME: pg-minikube
LAST DEPLOYED: Thu Jul 25 00:40:22 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: postgresql
CHART VERSION: 15.5.19
APP VERSION: 16.3.0

** Please be patient while the chart is being deployed **

PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:

    pg-minikube-postgresql.default.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace default pg-minikube-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

To connect to your database run the following command:

    kubectl run pg-minikube-postgresql-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:16.3.0-debian-12-r22 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host pg-minikube-postgresql -U postgres -d postgres -p 5432

    > NOTE: If you access the container using bash, make sure that you execute "/opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash" in order to avoid the error "psql: local user with ID 1001} does not exist"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/pg-minikube-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432
```

