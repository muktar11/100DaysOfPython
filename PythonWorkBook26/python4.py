student_dict = {
    "student":{"Angela", "James", "Lily"}, 
    "score": [56, 76, 98 ]
}

#Looping through dictionaries:
for(key, value) in student_dict.items():
    #Access key and value 
    pass 

import pandas 
student_data_frame = pandas.DataFrame(student_dict) 

#Loop through rows of a data frame 
for(index, row) in student_data_frame.iterrows():
    #Access index and row
    #  Access row.student or row.scroe
    pass 
# keywordd Method with iterrows()
#  {new_key:new_value  for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B":"Bravo"}

#TODO 2 Createa list of the phonetic code words from a worcd that the 