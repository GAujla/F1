import csv
import requests

class Driver_Information:
    def __init__(self, base_url):
        self.base_url = base_url
        self.header_list = ['Driver']
        self.driver_data = {}

    def ReadingData(self):
        self.header_list = ['Driver']
        self.driver_data = {}  # Dictionary to store driver names and positions

        for i in range(1, 6):
            url = self.base_url.format(i=i)  # Update the URL with the correct value of 'i'

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                races = data['MRData']['RaceTable']['Races']
                track = races[0]['raceName']
                self.header_list.append(track)   

                results = races[0]['Results']
                for result in results:
                    driver = result['Driver']['givenName']
                    position = result['position']
                    if driver in self.driver_data:
                        self.driver_data[driver].append(position)
                    else:
                        self.driver_data[driver] = [position]

            else:
                print(f'Error: {response.status_code}')


    def write_to_csv(self):
        driver_names = list(self.driver_data.keys())
        # Write the driver names and positions to CSV
        with open("f1.csv", 'w') as file:
            dw = csv.DictWriter(file, delimiter=',', fieldnames=self.header_list)
            dw.writeheader()

            for driver_name in driver_names:
                driver_positions = self.driver_data[driver_name]
                row = {'Driver': driver_name}

                for i, position in enumerate(driver_positions):
                    row[self.header_list[i+1]] = position

                dw.writerow(row)

csv_writer = Driver_Information('http://ergast.com/api/f1/current/{i}/results.json')
csv_writer.ReadingData()
csv_writer.write_to_csv()
