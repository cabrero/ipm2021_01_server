#!/usr/bin/env python3

import csv
import sys
from pathlib import Path

from flask import Flask, abort


#-- Data

intervals = {
    "2m": "1ST",
    "2M": "1T",
    "3m": "1T1ST",
    "3M": "2T",
    "4j": "2T1ST",
    "4aum": "3T",
    "5j": "3T1ST",
    "6m": "4T",
    "6M": "4T1ST",
    "7m": "5T",
    "7M": "5T1ST",
    "8a": "6T"
}

def key(interval, asc_des):
    return ",".join((interval, asc_des))

filepath = Path(__file__).parent / 'data' / 'intervalos.csv'

data = {}
with open(filepath, newline= '') as f:
    reader = csv.reader(f, skipinitialspace= True, quotechar= '"')
    for row in reader:
        interval, asc_des, *song = row
        k = key(interval, asc_des)
        songs = data.get(k, [])
        songs.append(song)
        data[k] = songs


#-- API

app = Flask(__name__)

@app.route('/intervals', methods=['GET'])
def _intervals():
    return {'data': intervals}

@app.route('/songs/<interval>/<asc_des>', methods=['GET'])
def _interval(interval, asc_des):
    k = key(interval, asc_des)
    if k in data:
        return {'data': data[k]}
    else:
        abort(404)


def main():
    app.run()

