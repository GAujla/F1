import requests
import csv

f = open('f1_info.csv', 'a')

for i in range(1, 6):
    base_url = f'http://ergast.com/api/f1/current/{i}/results.json'
    print(base_url)

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        print(races)