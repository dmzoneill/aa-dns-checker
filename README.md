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
`
kubectl logs -f automation-analytics-dns-checker
curl -v http://endpoint/unformatted | jq
`


