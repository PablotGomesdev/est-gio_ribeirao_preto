"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula,
além de informar a quantidade de vezes em que ela ocorre.
"""
palavra = str(input("Digite uma palavra qualquer: "))
palavra = palavra.lower()
quantidade_a = palavra.count("a")
print("A letra a aparece {} vezes na frase.".format(quantidade_a))

