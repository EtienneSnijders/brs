
"""
Created on Wed Oct 20 17:56:14 2021

@author: Eti
"""

from flask import Flask, redirect, url_for, render_template, request, session
from numpy import average
from pandas.core.frame import DataFrame
import requests
import pandas as pd
from pandas import json_normalize
import datetime
import numpy as np

headers_dict = {
"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ5MTk4OTIsInVzZXJuYW1lIjoiU2FtIiwib3JnTmFtZSI6Ik9yZzEiLCJpYXQiOjE2MzQ4ODM4OTJ9.o85xp8erywuiujzyJoNNFYXFVumfHx6zylHTRVR_qPU",
"Content-Type":"application/json" }

app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def home():
   response = requests.get('http://141.95.53.76:4000/channels/mychannel/chaincodes/fabcar?args=[""]&peer=peer0.org1.example.com&fcn=queryAllCars', headers=headers_dict)
   data = response.json()
   json = json_normalize(data)
   df = pd.DataFrame(json)
   df.head(n=2)
   for col in df.columns:
      nameList = col.split('.')
      if len(nameList) > 1:        
         df = df.rename(columns={col: nameList[1]})
   #df = df.round(decimals=2)

   # Change type of objects
   df["kwh"] = df["kwh"].astype(str).astype(float)
   df['kwh'] = df["kwh"].round(decimals=2)

   df["pricekwh"] = df["pricekwh"].astype(str).astype(float)
   df['pricekwh'] = df["pricekwh"].round(decimals=2)

   df["totalprice"] = df["totalprice"].astype(str).astype(float)
   df['totalprice'] = df["totalprice"].round(decimals=2)

   df = df.rename(columns={'Key':'TX ID', 'consumer': 'Consumer', 'date': 'Date','kwh': 'kWh', 'pricekwh':'Price kWh', 'producer':'Producer', 'time':'Time', 'totalprice': 'Total Price'})

   df = df.sort_values(by = 'TX ID', ascending=False)

   key = df["TX ID"].astype(str)
   Consumer = df["Consumer"].astype(str)
   date = df["Date"].astype(str)
   kwh = df["kWh"].astype(str).astype(float)
   pricekwh = df["Price kWh"].astype(str).astype(float)
   producer = df["Producer"].astype(str)
   time = df["Time"].astype(str)
   totalprice = df["Total Price"].astype(str).astype(float)

   # Totale Prijs
   dashboardVar1 = sum(totalprice)

   # Geleverde energy (kwh)
   dashboardVar2 = sum(kwh)

   # Transacties
   dashboardVar3 = df

   #average price per transaction
   dashboardVar4 = sum(pricekwh) / key.count()
   dashboardVar4 = "{:.2f}".format(dashboardVar4)

   return render_template("index.html", totalCost=dashboardVar1, geleverdeEnergy=dashboardVar2, transacties=dashboardVar3, avgprice=dashboardVar4, tables=[df.to_html(classes='data', header="true", index=False)])

# def html_table():
#     return render_template('index.html',  tables=[df.to_html(classes='data', header="true")])

if __name__ == "__main__":
   app.run(debug=True)