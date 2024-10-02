"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e
retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""
numero = int(input("digite um numero inteiro: "))
anterior1 = 1
anterior2 = 0
for n_elemento in range(1, numero + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero == atual:
        print(f"O número {numero} faz parte da sequência de fibonacci.")
        break
    elif numero < atual:
        print(f"O número {numero} não faz parte da sequência de fibonacci.")
        break
