from unittest import mock
from requests import Response

# Import the class and function to be tested
from gather_results import F1_Data_Information

def test_ReadData():
    # Create an instance of F1_Data_Information
    race_url = 'http://ergast.com/api/f1/current/results.json'
    quali_url = 'http://ergast.com/api/f1/current/5/qualifying.json'
    f1_data = F1_Data_Information(race_url, quali_url)
    
    # Create mock responses
    race_response = Response()
    race_response.json = mock.Mock(return_value={"MRData": {"RaceTable": {"Races": [{}]} }})
    quali_response = Response()
    quali_response.json = mock.Mock(return_value={"MRData": {"RaceTable": {"Races": [{}]} }})
    
    # Patch the requests.get method to return the mock responses
    with mock.patch('requests.get') as mock_get:
        mock_get.side_effect = [race_response, quali_response]
        
        # Call the method to be tested
        f1_data.ReadData()
    
    # Assert that the race_data and quali_data are set correctly
    assert f1_data.race_data == {"MRData": {"RaceTable": {"Races": [{}]}}}
    assert f1_data.quali_data == {"MRData": {"RaceTable": {"Races": [{}]}}}
