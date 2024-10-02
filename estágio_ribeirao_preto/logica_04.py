"""4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
"""
a = [1,3,5,7]    #Números impares
resultado_1 = a.append(9)
print(a)

b = [2,4,8,16,32,64]  #multiplos de 2
resultado_2 = b.append(128)
print(b)

c = [0, 1, 4, 9, 16, 25, 36] #numeros elevados ao quadrado 0², 1², 2², 3²......
resultado_3 = c.append(49) # 7² = 49
print(c)

d = [4, 16, 36, 64]  # 2², 4², 6², 8² esta pulando de 2 em 2 e elevando ao quadrado
resultado_4 = d.append(100) #10²
print(d)
e = [1, 1, 2, 3, 5, 8] # sequencia de fibonacci, soma o numero atual com o anterior.
resultado_5 = e.append(13) # 8 + 5 = 13
print(e)

f = [2,10, 12, 16, 17, 18, 19] # não parece uma sequencia muito correta, então chutei no 20
resultado_6 = f.append(20)
print(f)


