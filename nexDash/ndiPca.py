import click
import requests
import urllib3
import os, sys, time
import csv
from nexDashOps import nexDashGetToken

API_BASE_URL = "https://172.20.104.90"
payload = {
    "userName": "admin",
    "userPasswd": "DEVP@ssw0rd",
    "domain": "default"
}

igroup = "default"
sitename = "sandbox-aci"


@click.command()
@click.option("-u", type=str, help='NDI username')
@click.option("-p", type=str, help='NDI password')
def ndiPca(u, p):
    authDict = {"username": u, "password": p}
    cookie = nexDashGetToken(authDict)
    authString = "AuthCookie=" + cookie
    header = {"Cookie":authString,"content-type": "application/json"}
    epochUrl = API_BASE_URL +  f"/sedgeapi/v1/cisco-nir/api/api/telemetry/v2/events/insightsGroup/{igroup}/fabric/{sitename}/epochs?$size=1&$status=FINISHED&$epochType=ONLINE"
    response = requests.get(epochUrl, headers=header, verify=False)
    base_epoch_data = response.json()["value"]["data"][0]

    data = {
    "allowUnsupportedObjectModification": args.allowUnsupportedObjectModification,
    "analysisSubmissionTime": round(time.time() * 1000),
    "baseEpochId": base_epoch_data["epochId"],
    "baseEpochCollectionTimestamp": base_epoch_data["collectionTimeMsecs"],
    "fabricUuid": base_epoch_data["fabricId"],
    "description": args.descr,
    "name": args.name,
    "assuranceEntityName": args.site,
    "uploadedFileName": args.name
}
    print(base_epoch_data)
    
if __name__ == "__main__":
    ndiPca()