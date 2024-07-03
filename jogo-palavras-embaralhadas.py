import random

attempt = 7
words = 'TESTE', 'PROGRAMA', 'SHOW', 'OVO', 'LINUX', 'PYTHON', 'JAVASCRIPT', 'CARRO', 'FERRARI', 'CAMARO', 'BRANCO', 'PESQUISAR', 'COMPUTAÇÃO'
drawn = random.choice(words)
while attempt != 0:
    shuffles = random.sample(drawn, len(drawn))
    join_scrambled_word = ''.join(shuffles)
    print(join_scrambled_word)
    print("="*20)
    tent = input("Digite a palavra: ").upper()
    if tent == drawn:
        print("Parabéns, você venceu!")
        break
    else:
        attempt -= 1
        print(f"Você errou! Tentativas restantes: {attempt}")
        print("="*20)
