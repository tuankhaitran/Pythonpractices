# Open CSV file without csv module
# path = "C:\Study\Pythonpractices\CVSmodulepractices\google_stock_data.csv"
# lines = [line for line in open(path)]
# print(lines[0])
# print(lines[1])

# print(lines[0].strip().split(','))

# USING csv module
import csv
from datetime import datetime

path = "C:\Study\Pythonpractices\CVSmodulepractices\google_stock_data.csv"
file = open(path, newline='')
reader=csv.reader(file)

# Extract the first line, which is just headers
header= next(reader)
data = []
for row in reader:
    #row = [Data, Open, High, Low, Close,Volume,Adj Close]
    date = datetime.strptime(row[0],'%m/%d/%Y')
    open_price= float(row[1])
    high=float(row[2])
    low= float(row[3])
    close= float(row[4])
    volume =int(row[5])
    adj_close=float(row[6])

    data.append([date,open_price,high,low,close,volume,adj_close])

# Compute and store daily stock returns
# Stock Return = % change in price; Can be daily, monthly, weekly, yearly..

return_path = "C:\Study\Pythonpractices\CVSmodulepractices\google_return.csv"
file=open(return_path,'w')
writer= csv.writer(file)
writer.writerow(["Date", "Return"])


for i in range(len(data)-1):
    todays_row=data[i]
    todays_date=todays_row[0]
    todays_price=todays_row[-1]
    yesterday_row=data[i+1]
    yesterday_price=yesterday_row[-1]
    
    daily_return = (todays_price-yesterday_price)/yesterday_price
    formatted_date=todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])




 