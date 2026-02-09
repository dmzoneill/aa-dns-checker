# aa-dns-checker

## Create pod
```
kubectl create -f dns.yaml
```

## Delete pod
```
kubectl delete -f dns.yaml
```

## Review logs
```
kubectl logs -f automation-analytics-dns-checker
curl -v http://endpoint/unformatted | jq
```

## Expected output
```
[2022-07-18 12:20:32 +0000] [11] [INFO] Starting gunicorn 20.1.0
[2022-07-18 12:20:32 +0000] [11] [INFO] Listening at: http://0.0.0.0.12000 (11)
[2022-07-18 12:20:32 +0000] [11] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2022-07-18 12:20:32 +0000] [12] [INFO] Booting worker with pid: 12
[2022-07-18 12:20:32 +0000] [12] [INFO] Started server process [12]
[2022-07-18 12:20:32 +0000] [12] [INFO] Waiting for application startup.
[2022-07-18 12:20:32 +0000] [12] [INFO] Application startup complete.

```

