
# import required modules
import pandas as pd
import csv
  
# assign header columns
headerList = ['col1', 'col2', 'col3', 'col4']
  
# open CSV file and assign header
with open("gfg3.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',', 
                        fieldnames=headerList)
    dw.writeheader()