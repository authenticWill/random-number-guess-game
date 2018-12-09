import random
while True:
    x = float(random.randint(1,10))

    y = float(input('Guess a number 1-10:'))

    print('You guessed {0}. The number was {1}'.format(y,x))
    if (x==y):
        print('You guessed correctly!')
    else:
        print('Wrong!')
