import requests

# Set the base URL for the Ergast API
base_url = 'http://ergast.com/api/f1/seasons.json?limit=1000'

# Send the GET request to the API
response = requests.get(base_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Retrieve the JSON data from the response
    data = response.json()
    print(data)

    # Process the data as needed
    # For example, print the list of seasons
    seasons = data['MRData']['SeasonTable']['Seasons']
    for season in seasons:
        print(season['season'], season['url'])
else:
    # Print an error message if the request was not successful
    print('Error:', response.status_code)
