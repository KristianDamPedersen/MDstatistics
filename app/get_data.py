# This document is for getting the data, converting to a CSV file and storing it in 'data/raw'.

""" Connect to google sheets """
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('../MDstatistics/app/credentials/creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Master Duel - Deck stats').sheet1

data = sheet.get_all_records()

## Convert to excel
import pandas as pd

df = pd.DataFrame(data)

df.to_excel('../MDstatistics/app/data/raw/raw.xlsx')
