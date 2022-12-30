from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 
#Functon to check users guess againes actual answer
def check_answer(guess, answer):
    if guess > answer: 
        print("Too high") 
        global turns 
        turns -= 1 
    elif guess < answer:
        print("Too Low.")
    else: 
        print(f"YOu  gor it! The answer was {answer}.")


#Make  function to set diffuculty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        global turns 
        turns = EASY_LEVEL_TURNS 
    else: 
        turns = HARD_LEVEL_TURNS

#choosing a random numbeer between 1 and 100 
print("welcomt to the nuberGuessing Game")
print("Tam thinkking of a number between 1 and 100")
answer = randint(1, 100)
print(f"Pssst, the correct answer is {answer}")

#Let the user guess a  number 
guess = int(input("Make the guess"))
turns = set_difficulty()
print(f"YOu have {turns}attempts remaining to guess the number") 


#Tracj the number of turns and reduce by 1 if they getit wrong

#Repeat the guessing functionaly if thet get it  wrong.