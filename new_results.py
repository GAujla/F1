import csv
import requests

header_list = ['Driver']
driver_data = {}  # Dictionary to store driver names and positions
print(driver_data)

for i in range(1, 6):
    base_url = f'http://ergast.com/api/f1/current/{i}/results.json'
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        races = data['MRData']['RaceTable']['Races']
        track = races[0]['raceName']
        header_list.append(track)

        results = races[0]['Results']
        for result in results:
            driver = result['Driver']['givenName']
            position = result['position']
            if driver in driver_data:
                driver_data[driver].append(position)
            else:
                driver_data[driver] = [position]
                print(driver_data)

    else:
        print(f'Error: {response.status_code}')

driver_names = list(driver_data.keys())

# Write the driver names and positions to CSV
with open("f1.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',', fieldnames=header_list)
    dw.writeheader()

    for driver_name in driver_names:
        driver_positions = driver_data[driver_name]
        row = {'Driver': driver_name}

        for i, position in enumerate(driver_positions):
            row[header_list[i+1]] = position

        dw.writerow(row)
