with open('weather_data - Sheet1.csv') as file:
    data = file.readlines()

print(data)

columns = data.pop(0)
temprature = []
for index in range(len(data)):
    data[index] = data[index][:len(data[index])-1].split(',')
    temprature.append(int(data[index][1]))

print(data)
print(temprature)

import pandas as pd

df = pd.read_csv('weather_data - Sheet1.csv')

print(df[df['temp'] == df['temp'].max()])