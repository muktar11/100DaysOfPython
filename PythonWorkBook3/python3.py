print("Welcomt to the rollercoster! ")
height = int(input("What is your height in cm ? ")) 
bill = 0

if height >= 120:
    print("YOu can ride the rollercoster")
    age = int(input("What is your age? "))
    if age > 12:
        bill = 5
        print("Child taickets are $5")
    elif age <= 18: 
        bill = 7
        print("yout tickets are $7")
    else: 
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do  you eant a photo taken ? Y or N") 
    if wants_photo == "Y":
        bill = bill + 3
    print(f"your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")