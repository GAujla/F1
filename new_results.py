import requests
import csv


header_list = []
for i in range(1, 6):
    base_url = f'http://ergast.com/api/f1/current/{i}/results.json'

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']            
        race_names = [race['raceName'] for race in races]
        tracks = races[0]['raceName']
        header_list.append(tracks)
        with open("gfg3.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', 
                        fieldnames=header_list)
            dw.writeheader()

        
        print(header_list)

        
    


            
        results = races[0]['Results']
        for result in results:
            driver = result['Driver']['givenName']
            position = result['position']
    else:
        print(f'Error: {response.status_code}')
