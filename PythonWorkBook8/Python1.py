def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            is_prime = False 
        if is_prime:
            print("its a prime number.")
        else: 
            print("Its a not a prime number.")
     
n = int(input("Check this number: "))
prime_checker(number=n)