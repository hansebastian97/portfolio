from email.mime import base
import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_request(baseurl, endpoint,x):
    r = requests.get(baseurl + endpoint, f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for i in response['results']:
        char = {
            'name':i['name'],
            'gender':i['gender'],
            'status':i['status'], 
            'total_ep':len(i['episode']) 
        }
        charlist.append(char)

    return charlist
    

data = main_request(baseurl, endpoint, 1)
mainlist = []
for x in range(1,get_pages(data)):
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))
# print(parse_json(data))

df = pd.DataFrame(mainlist)

df.to_csv("testing.csv")
