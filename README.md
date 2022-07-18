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
[daoneill@fedora aa-dns-checker-bot]$ kubectl logs -f automation-analytics-dns-checker
+ gunicorn dnslookup:app --bind 0.0.0.0:8000 --workers 1 --worker-class uvicorn.workers.UvicornWorker --capture-output
[2022-07-18 12:08:52 +0000] [11] [INFO] Starting gunicorn 20.1.0
[2022-07-18 12:08:52 +0000] [11] [INFO] Listening at: http://0.0.0.0:8000 (11)
[2022-07-18 12:08:52 +0000] [11] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2022-07-18 12:08:52 +0000] [12] [INFO] Booting worker with pid: 12
[2022-07-18 12:08:52 +0000] [12] [INFO] Started server process [12]
[2022-07-18 12:08:52 +0000] [12] [INFO] Waiting for application startup.
Mon, 18 Jul 2022 12:08:52 + 1010: heartbeat
[2022-07-18 12:08:52 +0000] [12] [INFO] Application startup complete.
```

