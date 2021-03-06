# -*- coding: utf-8 -*-

import requests
import json
import math
import datetime
import openpyxl
import pprint

SLACK_URL = "https://slack.com/api/conversations.history"
TOKEN = "xoxp-1829892296706-1842519970865-1826870140725-367558dc5f37972ed861759b6800be32"
SLACK_CHANNEL_ID = 'C01QL1S4952'
headers = {"Authorization" : "Bearer "+ TOKEN}
def fetch_text():
    payload = {
        "channel": SLACK_CHANNEL_ID,
        "as_user": True
    }
    response = requests.get(SLACK_URL,headers = headers, params=payload)
    json_data = response.json()
    msgs = json_data['messages']
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
    for msg in msgs:
      ts = int(float(msg['ts']))
      # print(msg)
      date = datetime.datetime.fromtimestamp(ts).strftime("%Y/%m/%d")
      sheet['B1'] = date
      if msg['user'] == 'U01QSF9UJRF':
        for row in sheet['A1:C10']:
          for col in row:
            if col.value == date:
              cell = col.offset(0,1)
              cell.value = '出社'
              if msg['text'] == '業務を開始します':
                time = datetime.datetime.fromtimestamp(ts).strftime("%H:%M")
                cell = col.offset(0,2)
                cell.value = time
              elif msg['text'] == '業務を終了します':
                time = datetime.datetime.fromtimestamp(ts).strftime("%H:%M")
                cell = col.offset(0,3)
                cell.value = time

    wb.save("Sample.xlsx")
    return [msg['text'] for msg in msgs]

messages = fetch_text()