import requests
import json
import sys, getopt, csv

def nxosGetToken(specDict2, hostAddress):
  baseURL = "http://" + hostAddress
  tokenURL = baseURL + "/api/aaaLogin.json"
  print(tokenURL)

  #urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
  tokenHeader = {"content-type": "application/json","response-type": "application/json"}
  jsonPayload = {'aaaUser':{'attributes':{'name':specDict2['username'],'pwd':specDict2['password']}}}
  tokenResponse = requests.post(tokenURL, headers=tokenHeader, json=jsonPayload, verify=False)
  print(tokenResponse)
  jsonData = tokenResponse.json()
  token = jsonData["imdata"][0]["aaaLogin"]["attributes"]["token"]
  newCookie = {'APIC-cookie':token}
  return newCookie


def nxosAddFeature(specDict):

  with open(specDict['infile'], 'r') as csv_file:
      csvread = csv.DictReader(csv_file)
      csvDict = list(csvread)

  print(csvDict)
  for i in range(len(csvDict)):
    k = 0
    if(csvDict[i]['mgmtIP'] != ""):
      baseUrl = "http://" + csvDict[i]['mgmtIP'] + "/ins"
      headers={'content-type':'application/json'}
      print(csvDict[i]['feature'])
      print(csvDict[k]['feature'])
      for k in range(len(csvDict)):
        if(csvDict[k]['feature'] != ""):
          featureInput = "feature " + csvDict[k]['feature']
          payload={
            "ins_api": {
                "version": "1.0",
                "type": "cli_conf",
                "chunk": "0",
                "sid": "sid",
                "input": featureInput,
                "output_format": "json",
                "rollback": "stop-on-error"
            }
          }
          response = requests.post(baseUrl,data=json.dumps(payload), headers=headers,auth=(specDict['username'],specDict['password'])).json()

def nxosGetVlans(specDict):

  with open(specDict['infile'], 'r') as csv_file:
    csvread = csv.DictReader(csv_file)
    csvDict = list(csvread)
  keys = csvDict[0].keys()

  for i in range(len(csvDict)):
    if (csvDict[i]['mgmtIP'] != ""):
      nxosHostToken = nxosGetToken(specDict, csvDict[i]['mgmtIP'])
      baseUrl = "http://" + csvDict[i]['mgmtIP'] + "/api/mo/sys/bd.json?query-target=children&target-subtree-class=l2BD"
      headers={'content-type':'application/json'}

      try:
        response = requests.get(baseUrl, headers=headers, cookies=nxosHostToken, auth=(specDict['username'],specDict['password']))
        responseJson = response.json()
        #print(responseJson)
        for i in range(len(responseJson['imdata'])):
          vlanEncap = responseJson['imdata'][i]['l2BD']['attributes']['fabEncap']
          hostKeyList = [csvDict[i]['hostname']]
          hostKey = hostKeyList[0]
          print(hostKey)
          print(vlanEncap)
          csvDict[i][hostKey] = vlanEncap
    
      except requests.exceptions.Timeout:
        print("Host " + hostIp + " Unavailable")

      with open(specDict['infile'], "w", newline='') as out_file:
        dictWrite = csv.DictWriter(out_file, keys)
        dictWrite.writeheader()
        dictWrite.writerows(csvDict)

  return 0

     
     

 