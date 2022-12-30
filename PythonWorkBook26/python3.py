passed_students = {
    "Beth": 72, 
    "Caroline":62
}

passed_students = {new_key:new_value for (key, value) in dicti,items()} 

sentence = "What is the Airspeed Valeocity of an Unladen Swallow>"

result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {
    "Monday":12, 
    "Tuesday":14, 
    "Wedneshay":15, 
    "Thrsday": 14, 
    "Friday":21, 
    "Saturday":22, 
    "Sunday":24, 
}

weather_f = {day:temp_c*9/5 + 32 for(day, temp_c) in weather_c.items()}
print(weather_f)

student_dict = {
    "studnet": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas 


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame 
for(key, value) in student_data_frame.items():
    print(key)

#Loop through rows of a data frame 
for (index, row) in student_data_frame.iterrows():
    print(index)