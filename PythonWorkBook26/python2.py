new_dict ={new_key:new_value for item in list} 

new_dict = {new_key:new_value for (key, value) in dict.items() if test}


names = [ 'Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#students_scores = {new_key: new_value for item in names}
import random 

students_scores= {student: random.randint(1, 100) for student in names}

passed_students = {}