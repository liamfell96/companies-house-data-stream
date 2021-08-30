import requests
from requests.auth import HTTPBasicAuth
from keys import api_key
import json


def main():
    r = requests.get('https://stream.companieshouse.gov.uk/companies', stream=True, auth=HTTPBasicAuth(api_key, ''))
    print(r.status_code)
    for line in r.iter_lines():

        # filter out keep-alive new lines
        if line:
            decoded_line = line.decode('utf-8')

            repsonse_dict = json.loads(decoded_line)
            event = repsonse_dict['event']
            resource_uri = repsonse_dict['resource_uri']

            print(event)
            print(resource_uri)

    return


main()
