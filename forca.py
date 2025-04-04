palavra = "escola"
limite_tentativas = len(palavra) + 5

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("")

contador = 1 
while(contador <= limite_tentativas):
    print("Tentativas:",contador,"/",limite_tentativas)
    chute = input("Digite a letra:")

    for letra in palavra: 
    if chute == letra:
       letras_acertadas[indice] = chute
    else:
        indice + 1

    contador = contador + 1
# Para executar: python3 forca.py 



