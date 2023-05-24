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
        
        with open('innovators.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            
            race_names = [race['raceName'] for race in races]
            race_names_string = ','.join(race_names)  # Join race names into a comma-separated string
            writer.writerow([race_names_string])  # Write the race names string as a single row
            
            results = races[0]['Results']
            for result in results:
                driver = result['Driver']['givenName']
                position = result['position']
                print(f'{position}  {driver}')
    else:
        print(f'Error: {response.status_code}')
