import requests, time
from getData import getGTData

def getresponse():
    gsdata = getGTData()
    payload_list = [('1bRT3njCRVcLayIqkMS0nCE_p_gw1ea6f5P_sLwOl9o8', 0)]
    for i, val in enumerate(gsdata):
        payload_list.append((','.join(val), i))
    requests.post('http://localhost:8000/canalservice/tabupd/', data = payload_list)

while True:
    try:
        getresponse()
    except:
        pass
    time.sleep(2)

