#!/usr/bin/python

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("client_supersecret.json", scope)
client = gspread.authorize(credentials)
gspread.Client.login(client)
sheet = client.open("WRFTAppTest").sheet1
nummy = ((sheet.row_count) - 1000)
if nummy <= 1:
	nummy = 1
elif nummy >= 1:
	nummy = nummy
nummyplusone = (nummy + 1)
rowin = ["salmon","40cm","Loch Maree","3kg"]
sheet.insert_row(rowin, nummyplusone)
exit()
