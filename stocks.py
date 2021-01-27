import requests
import gspread
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
sys.stderr = open("errlog.txt", "w")
import time


def send_msg():

    text = create_msg()
    token = "1552295010:AAH-EKxdbMC9cbNOHKCTO2mn9oK74B64kw0"
    chat_id = "612299579"

    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=html"
    requests.post(url_req)


def create_stock_row(row):
    row = f'<b>{row[0]}:</b>\n' \
          f' Today value: {row[5]}, yesterday value: {row[4]}\n' \
          f' Today change: {row[3]} and in INS: {row[2]}\n' \
          f' <i>Total earning from stock: {row[1]}</i>\n'
    return row


def create_msg():
    msg = '<b><i>Today status:</i></b>\n'
    current_stocks = ["Pharmoocan", "Pasternak Shoham", "Unitronics", "Together"]
    filename = 'C://Users//Administrator//Documents//Stocks//cred.json'
    gc = gspread.service_account(filename=filename)
    sheet_key = '1WAjKb5aPOBnL-KYlF_Fu26o26qYZJdvjckRXxMwyYIE'
    print(gc.auth._project_id)
    sh = gc.open_by_key(sheet_key)
    # print(sh)

    worksheet = sh.sheet1

    rows = worksheet.get_all_values()

    for row in rows:
        if row[0] not in current_stocks:
            continue
        msg += create_stock_row(row)
    msg += '\n'
    msg += f'Total earning so far: {rows[-1][1]}'

    return msg

import traceback
import sys
import os
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
paths = sys.path
for path in paths:
    if 'PyCharm' in path:
        continue
    print(path)
x = 1


print("here")
send_msg()
time.sleep(10)

day_seconds = 86400


