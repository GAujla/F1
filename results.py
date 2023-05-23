import requests



def fetch_data():
    base_url = 'http://ergast.com/api/f1/current/last/results.json'

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
                
                print(f"Position: {position}")
                print(f"Driver: {driver}")
                print(f"Constructor: {constructor}")
                print()
        else:
            print('No race results available for the last race.')
    else:
        print('Error:', response.status_code)

