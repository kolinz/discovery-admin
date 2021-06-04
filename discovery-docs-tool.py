# coding: UTF-8
import json
import sys
import settings
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

args = sys.argv
apikey = settings.apikey
url = settings.url
environment_id = settings.environment_id
collection_id = settings.collection_id

if args[1] == 'delete':
    document_id = args[2]
    
    authenticator = IAMAuthenticator(apikey)
    discovery = DiscoveryV1(
        version='2019-04-30',
        authenticator=authenticator
    )
    
    discovery.set_service_url(url)
    delete_doc = discovery.delete_document(environment_id, collection_id, document_id).get_result()
    print(json.dumps(delete_doc, indent=2))