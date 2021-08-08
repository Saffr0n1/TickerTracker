from urllib.request import Request, urlopen
import json
import pandas as pd

req = Request("https://api.stocktwits.com/api/2/trending/symbols/equities.json", headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
data = json.loads(webpage)

temp = []
for item in data['symbols']:
    temp.append(item['symbol'])
    if len(temp) > 10:
        break

d = {'ticker': temp}
output = pd.DataFrame(d)
output.to_csv("stockTwitsTest3.csv")