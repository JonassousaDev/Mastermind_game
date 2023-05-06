import random
(COLORS) = ['R', 'G', 'B', ' Y', 'W', 'O']
TRIES = 10
CODE_LENGHT = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGHT):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input('Guess: ').upper().split(' ')

        if len(guess) != 4:
            print(f'you must guess {CODE_LENGHT} color.')
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f'invalid color: {color}. Try again.')
                break
        else:
            break
    return guess

