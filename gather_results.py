import requests
import pprint
import csv

DATA_DICT = {"Driver_Name": [], "Finished_Position": [], "Qualifying_Time_Q1": [], "Qualifying_Time_Q2": [], "Qualifying_Time_Q3": []}


pp = pprint.PrettyPrinter(indent=1)


class F1_Data_Information:
    def __init__(self, race_url, quali_url):
        self.race_url = race_url
        self.quali_url = quali_url
    
    def ReadData(self):

        race_response = requests.get(self.race_url)
        quali_response = requests.get(self.quali_url)
        self.race_data = race_response.json()
        self.quali_data = quali_response.json()


        #pp.pprint(quali_data)
        #pp.pprint(data)
    
    def DriversName(self):
        drivers = self.race_data['MRData']['RaceTable']['Races'][0]['Results']
        for result in drivers:
            family_name = result['Driver']['familyName']
            DATA_DICT["Driver_Name"].append(family_name)

    #print(family_name)

    def Finished_Position(self):
        finished_position = self.race_data['MRData']['RaceTable']['Races'][0]['Results']
        for position in finished_position:
            placement = position['position']
            DATA_DICT["Finished_Position"].append(placement)

    def Qualifying_Time(self):
        qualifying_time = self.quali_data['MRData']['RaceTable']['Races'][0]['QualifyingResults']
        for time in qualifying_time:
            if 'Q1' in time:
                time_finished_q1 = time['Q1']
                DATA_DICT["Qualifying_Time_Q1"].append(time_finished_q1)
            else:
                DATA_DICT["Qualifying_Time_Q1"].append('The driver didnt submit a time for Q1')

            if 'Q2' in time:
                time_finished_q2 = time['Q2']
                DATA_DICT["Qualifying_Time_Q2"].append(time_finished_q2)
            else:
                DATA_DICT["Qualifying_Time_Q2"].append('The driver didnt submit a time for Q2')

            if 'Q3' in time:
                time_finished_q3 = time['Q3'] 
                DATA_DICT["Qualifying_Time_Q3"].append(time_finished_q3)
            else:
                DATA_DICT["Qualifying_Time_Q3"].append('The driver did not submit a time for Q3')

    def WriteToCSV(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(DATA_DICT.keys())  # Write the headers
            writer.writerows(zip(*DATA_DICT.values()))  # Write the data rows


# Create an instance of F1_Data_Information
race_url = 'http://ergast.com/api/f1/current/results.json'
quali_url = 'http://ergast.com/api/f1/current/5/qualifying.json'
filename = "f1_data.csv"

f1_data = F1_Data_Information(race_url, quali_url)

# Read the race and qualifying data
f1_data.ReadData()

# Extract driver names
f1_data.DriversName()

# Extract finished positions
f1_data.Finished_Position()

# Extract qualifying times
f1_data.Qualifying_Time()

f1_data.WriteToCSV(filename)

