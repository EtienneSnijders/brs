# brs
Correction of the online Borromean ring signature Algorithm 

import requests
import pandas as pd
import io
from pandas import json_normalize

headers_dict = {
"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ3Njg3NTUsInVzZXJuYW1lIjoiRXRpZW5uZVMiLCJvcmdOYW1lIjoiT3JnMSIsImlhdCI6MTYzNDczMjc1NX0.PC14IEti6LOzKakBTlODu1ay5I7hAgIQhdaiu1PHqKI",
"Content-Type":"application/json" }

response = requests.get('http://localhost:4000/channels/mychannel/chaincodes/fabcar?args=[""]&peer=peer0.org1.example.com&fcn=queryAllCars', headers=headers_dict)
data = response.json()
df = json_normalize(data)
print(df)

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ4Mjk3NTYsInVzZXJuYW1lIjoiRXRpZW5uZVMiLCJvcmdOYW1lIjoiT3JnMSIsImlhdCI6MTYzNDc5Mzc1Nn0.ZMtE9MAJnSNPlWLnR749OJ2YNx3cEbEHzT7VVUlND9w
