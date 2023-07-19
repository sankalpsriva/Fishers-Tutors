from formResponses import updateResponses
import pandas as pd 
import re, json, pygsheets
from data import *

pyg = pygsheets.authorize(service_account_file = 'service_account.json')
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
unformattedNames = []
hours = []

updateResponses()
with open("JSON\\names.json", 'r') as file:
    unformattedNames = json.load(file)
    
df = pd.read_csv(URL)

for name in df['Name']:
    hours.append(unformattedNames.count(re.sub("[^a-zA-Z0-9]+", "", name).lower()))
    
df["Current Hours"] = hours

df = df.fillna("")


for index in range(len(df['Name'])):
    if df["Current Hours"][index] != "" and df["First Year Hours / Offset Hours"][index] != "": 
        total = df["Current Hours"][index] + int(df["First Year Hours / Offset Hours"][index])
        df['Total Hours'][index] = total
        
        print(f'Curr Hours: {df["Current Hours"][index]}, Offset Hours: {df["First Year Hours / Offset Hours"][index]}')
    # if df['First Year Hours / Offset Hours'][index] == 0:
    #     df['First Year Hours / Offset Hours'][index] = ""
    # if df['Current Hours'][index] == 0:
    #     df['Current Hours'][index] = ""
        
# splice = df["Name"][]
        
df.drop(columns = "Unnamed: 4")
df = df.rename(columns = {"Unnamed: 4": ""})
        
# sheet = pyg.open(r'Tutors Attendance (Responses)')[1]
# sheet.set_dataframe(df, (0,0))