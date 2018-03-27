#!/usr/bin/python
#Code to find a laptop id and group ID via the SimpleMDM API and some python

import requests
import json

key = "I am a variable containing a SimpleMDM API key"

def get_simplemdm_device_id(serial_number):
    url = 'https://a.simplemdm.com/api/v1/devices?search={SERIAL_NUMBER}'.format(SERIAL_NUMBER=serial_number)
    laptop_data = requests.get(url, auth=(key, ''))
    json_laptop_data = laptop_data.json()
    try:
        simplemdm_machine_id = json_laptop_data['data'][0]['id']
        print('Laptop serial number {} has a SimpleMDM machine id of {}'.format(serial_number, simplemdm_machine_id))
        return simplemdm_machine_id
    except:
        print ('{} is not in SimpleMDM'.format(serial_number))
        return

def query_simplemdm_group(simplemdm_machine_id):
    url = 'https://a.simplemdm.com/api/v1/devices/{}'.format(simplemdm_machine_id)
    response = requests.get(url, auth=(key, ''))
    json_response = response.json()
    try:
        simplemdm_group = json_response["data"]["relationships"]["device_group"]["data"]["id"]
        print ('Machine id {} is in SimpleMDM Group {}'.format(simplemdm_machine_id, simplemdm_group))
        return simplemdm_group
    except:
        print "no such group"
        return

def list_all_groups():
    url = 'https://a.simplemdm.com/api/v1/device_groups'
    response = requests.get(url, auth=(key, ''))
    json_response = response.json()
    print json_response

def main():
    serial = "a valid serial number in SimpleMDM"
    device_id = get_simplemdm_device_id(serial)
    groupid = query_simplemdm_group(device_id)
    list_all_groups()

if __name__ == "__main__":
    main()
