from fastapi import FastAPI
import socket
import asyncio
from time import gmtime, strftime
import pprint


class BackgroundRunner:
    def __init__(self):
        self.servers = [
            "tower-analytics-prod.ckxxru2ayexw.us-east-1.rds.amazonaws.com",
            "insights.unleash.devshift.net",
            "pdf-generator-api.pdf-generator-prod.svc.cluster.local",
            "backoffice-proxy.apps.ext.spoke.prod.us-west-2.aws.paas.redhat.com"
        ]

        self.log = []
        self.failed = 0
        self.success = 0
        self.total = 0

    async def run_main(self):
        while True:
            for X in self.servers:
                self.total += 1
                try:
                    await asyncio.sleep(0.5)
                    socket.gethostbyname(X)
                    self.success += 1
                except Exception as e:
                    line = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime()) + ": " + str(e) + ": " + X
                    self.log.append(line)
                    print(line)
                    self.failed += 1
            await asyncio.sleep(10)

            if len(self.log) > 10000:
                self.log = self.log[-1000:]

app = FastAPI()
runner = BackgroundRunner()

@app.on_event('startup')
async def app_startup():
    asyncio.create_task(runner.run_main())

@app.get("/")
def root():
    return "ya try /formatted or /unformatted"

@app.get("/formatted")
def formatted():
    return pprint.pformat({
        "servers": runner.servers,
        "success": runner.success,
        "failed": runner.failed,
        "total": runner.total,
    }, indent=4)

@app.get("/unformatted")
def unformatted():
    return {
        "servers": runner.servers,
        "success": runner.success,
        "failed": runner.failed,
        "total": runner.total,
    }