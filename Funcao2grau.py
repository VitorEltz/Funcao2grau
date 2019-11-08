#Escreva um programa que resolva uma equação de segundo grau

input_a = input("Digite o valor de 'a' na equacao: ")
if input_a == "":
    a = 1
else:
    a = int(input_a)
input_b = input("Digite o valor de 'b' na equacao: ")
if input_b == "":
    b = 1
else:
    b = int(input_b)
input_c = input("Digite o valor de 'c' na equacao: ")
if input_c == "":
    c = 1
else:
    c = int(input_c)

delta = b**2-4*a*c
raizdelta = delta**0.5

x1 = (-b+raizdelta) / (2*a)
x2 = (-b-raizdelta) / (2*a)

print("O valor de X1 da Equacao de 2 grau eh: %d " %(x1))
print("O valor de X2 da Equacao de 2 grau eh: %d " %(x2))



