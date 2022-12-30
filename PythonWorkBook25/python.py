
import csv 

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data: 
        #disinclude the first item in the list with the row 2 temp is row0
        if row[1] != "temp":
            temperatures.append(row[1])     
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"])) 

data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns 
print(data["Condition"])
print(data.Condition)

#Get Data in Row
print(data[data.dat == "Monday"])
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
monday_temp =  int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F) 

#Create a dataframe fromscreatch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

import pandas 

data = pandas.DataFrame(data_dict)
print(data)

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

