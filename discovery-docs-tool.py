# coding: UTF-8
import os
import json
import sys
import requests
import settings
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas.io.json import json_normalize

args = sys.argv
apikey = settings.apikey
url = settings.url
environment_id = settings.environment_id
collection_id = settings.collection_id

authenticator = IAMAuthenticator(apikey)
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
    )

if args[1] == 'docslist':
    params = (
        ('version', '2019-04-30'),
        ('return', 'extracted_metadata.filename'),
        )
    response = requests.get(url+'/v1/environments/'+environment_id+'/collections/'+collection_id+'/query', params=params, auth=('apikey', apikey))
    data = response.json()
    df = json_normalize(data['results'])
    print(df)

if args[1] == 'add':
    file_path = args[2]
    discovery.set_service_url(url)
    with open(file_path) as fileinfo:
        add_doc = discovery.add_document(environment_id, collection_id, file=fileinfo).get_result()
    print(json.dumps(add_doc, indent=2))

if args[1] == 'update':
    file_path = args[2]
    document_id = args[3]
    discovery.set_service_url(url)
    with open(file_path) as fileinfo:
        add_doc = discovery.update_document(environment_id, collection_id, document_id, file=fileinfo).get_result()
    print(json.dumps(add_doc, indent=2))

if args[1] == 'delete':
    document_id = args[2]    
    discovery.set_service_url(url)
    delete_doc = discovery.delete_document(environment_id, collection_id, document_id).get_result()
    print(json.dumps(delete_doc, indent=2))
