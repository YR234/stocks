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
    msg += '<b><i>Real stocks status:</i></b>\n'
    demo_stocks = ["Unitronics", "Together"]
    real_stocks = ["Pharmoocan", "Pasternak Shoham"]
    filename = './cred.json'
    gc = gspread.service_account(filename=filename)
    sheet_key = '1WAjKb5aPOBnL-KYlF_Fu26o26qYZJdvjckRXxMwyYIE'
    # print(gc.auth._project_id)
    sh = gc.open_by_key(sheet_key)
    # print(sh)

    worksheet = sh.sheet1

    rows = worksheet.get_all_values()

    for row in rows:
        if row[0] not in real_stocks:
            continue
        msg += create_stock_row(row)

    msg += '\n<b><i>Demo stocks status:</i></b>\n'
    for row in rows:
        if row[0] not in demo_stocks:
            continue
        msg += create_stock_row(row)

    for row in rows:
        if '_True' in row[0]:
            msg += '\n\n'
            msg += f'Total Real earning so far: {row[1]}'
        if '_Demo' in row[0]:
            msg += '\n'
            msg += f'Total Demo earning so far: {row[1]}'



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
day_seconds = 86400
while True:
    send_msg()
    print("Sleeping until tommarow")
    time.sleep(day_seconds)
