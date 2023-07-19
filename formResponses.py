from __future__ import print_function
from googleapiclient import discovery
from google.oauth2.credentials import Credentials
from httplib2 import Http
from oauth2client import client, file, tools
from quickstart import quickstart
import json, re, os
from data import *

def updateResponses():
    names = []

    creds = quickstart()
    service = discovery.build('forms', 'v1', credentials=creds ,discoveryServiceUrl=DISCOVERY_DOC)
        
    # Prints the responses of your specified form:
    form_id = '1BJztZfOCigwlMXLBzH85XR6UytYa3lJlPqCUKcc4prE'
    result = service.forms().responses().list(formId=form_id).execute()

    with open("JSON\\names.json", "w") as output:
        for i in range(len(result['responses'])):
            names.append(re.sub("[^a-zA-Z0-9]+", "", result['responses'][i]['answers']['0e717468']['textAnswers']['answers'][0]['value'].lower()))
        json.dump(names, output) 