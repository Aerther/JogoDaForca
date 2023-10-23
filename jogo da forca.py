import random
import sys

pal = []
x = 0
w = 0

print("Jogo da Forca\n")

palavras = ["abelha","cavalo","bola","mesa","caderno","lapis","borracha","estojo","chocolate","coruja"
"coberta","churrasco","palavra","sol","planeta","gato","cachorro","garrafa","controle","girafa",
"prato","colher","elefante","lua","terra"]

p = random.choice(palavras)

for i in range(len(p)):
    pal.append("_")
    
while x != 6:
    print(*pal, sep=' ')
    if "_" in pal:
        chute = input("\nDigite uma letra ou tente acertar a palavra: ").lower()
    if chute == p or "_" not in pal:
        print(f"\nMeus parabéns, conseguiu acertar a palavra em {w+1} tentativa{'' if x==1 else 's'} com {x} erro{'' if x==1 else 's'}")
        sys.exit()
    elif chute in p:
        for i, y in zip(p, range(len(p))):
            if chute == i:
                pal[y] = i.upper()
            else:
                pass  
    else:
        print("\nVocê não acertou nenhuma letra")
        x += 1
    w += 1
print(f"\nVocê perdeu, a palavra era {p}")
