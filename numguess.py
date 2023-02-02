from random import randint

#Create answer name : i to 100 (Integer)
answer = randint(1,100)
# Print answer (for debugging)
print(answer)

# Get user's name, guess 
user_name = input('Hello, there! What is your name? ')
guess = input(f'Hi , {user_name}. Guess the number(1-100): ')

# print to check
print(user_name, guess)
