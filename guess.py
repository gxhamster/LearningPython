import random

random.seed()
secret_guess = random.randint(20, 100)
hint = 'The secret number is more than {} and less than {}'.format(secret_guess - 12, secret_guess + 12)

for tries in range(0, 6):
    guess = int(input('Enter guess: '))
    
    if (guess > secret_guess):
        print('Your guess is higher')
    elif (guess < secret_guess):
        print('Your guess is lower')
    else:
        break
    if tries % 2 == 0:
        print(hint)

print('You got it the secret number is ', guess)
print('You got it in', tries, 'tries')
