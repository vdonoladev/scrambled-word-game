import random

attempt = 7
words = 'TEST', 'PROGRAM', 'SHOW', 'EGG', 'LINUX', 'PYTHON', 'JAVASCRIPT', 'CAR', 'FERRARI', 'CAMARO', 'WHITE', 'SEARCH ', 'COMPUTING'
drawn = random.choice(words)
while attempt != 0:
    shuffles = random.sample(drawn, len(drawn))
    join_scrambled_word = ''.join(shuffles)
    print(join_scrambled_word)
    print("="*20)
    tent = input("Type the word: ").upper()
    if tent == drawn:
        print("Congratulations you won!")
        break
    else:
        attempt -= 1
        print(f"You missed! Remaining attempts: {attempt}")
        print("="*20)
