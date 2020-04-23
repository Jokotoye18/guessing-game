import random
level = input("Enter the level you wish to play from 'easy, medium, hard':: ")
level = level.lower()
if level == 'easy':
    print("You have the chance to guess a number from 1-10 and you have '6' guesses")
    answer = random.randint(1,10)
    guesses = 6
    active = True
    while active:
        prompt = input('Enter your guess :: ')
        prompt = prompt.strip()
        if answer == int(prompt):
            print(f'You got it right! The answer is {answer}, cheers!')
            break
        else:
            guesses -= 1
            print(f"That was wrong, try again. You have {guesses} guesses left.")
            if guesses == 0:
                print("You are out of guesses. Game over!")
                break

if level == 'medium':
    print("You have the chance to guess a number from 1-20 and you have '4' guesses")
    answer = random.randint(1,20)
    guesses = 4
    active = True
    while active:
        prompt = input('Enter your guess :: ')
        prompt = prompt.strip()
        if answer == int(prompt):
            print(f'You got it right! The answer is {answer}, cheers!')
            break
        else:
            guesses -= 1
            print(f"That was wrong, try again. You have {guesses} guesses left.")
            if guesses == 0:
                print("You are out of guesses. Game over!")
                break

if level == 'hard':
    print("You have the chance to guess a number from 1-50 and you have '3' guesses")
    answer = random.randint(1,50)
    guesses = 3
    active = True
    while active:
        prompt = input('Enter your guess :: ')
        prompt = prompt.strip()
        if answer == int(prompt):
            print(f'You got it right! The answer is {answer}, cheers!')
            break
        else:
            guesses -= 1
            print(f"That was wrong, try again. You have {guesses} guesses left.")
            if guesses == 0:
                print("You are out of guesses. Game over!")
                break