#try: SOmething that might cause an ecxeption
#except: Do this ifthere was an Exceptione
#else: Do this if there were no exceptions
#finally: DO this no matter what happens

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileExistsError:
        file = open("a_file.txt", "w")
        file.write("something")
except KeyError as error_message: 
    print(f"The key {error_message} does not exist")
else:
    content= file.read()
    print(content)
finally:
    raise TypeError("This is an error that 2 made up.") 

height = float(input("height"))
weight = int(input(input ("Weight:")))

if height > 3: 
    raise ValueError("iNVALID HEIGHT")

bmi = weight / height **2
print(bmi)