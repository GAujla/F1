import requests


def fetch_data():
    for i in range(1,6):
        base_url = f'http://ergast.com/api/f1/current/{i}/results.json'

        # Get the last race results for the current season
        response = requests.get(base_url)

        if response.status_code == 200:
            data = response.json()

            # Check if the RaceTable element is not empty
            if 'RaceTable' in data['MRData'] and data['MRData']['RaceTable']:
                # Retrieve the list of results
                results = data['MRData']['RaceTable']['Races'][0]['Results']

                # Process the results as needed
                for result in results:
                    position = result['position']
                    driver = result['Driver']['givenName'] + ' ' + result['Driver']['familyName']
                    constructor = result['Constructor']['name']


        return driver, position, constructor





if __name__ == '__main__':
    print(fetch_data())