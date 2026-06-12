from math import sqrt
from random import randint
''' 1
Faça um programa que leia um número digitado pelo usuário e apresente o seu
sucessor e seu antecessor.
'''
numero = int(input("Digite um número: "))
print(f'Sucessor de {numero}= {numero+1}')
print(f'Antecessor de {numero}= {numero-1}')

''' 2
Crie um programa que leia uma entrada em Reais e retorne à quantidade de
Dólares que poderá ser comprado com o valor inicial.
'''
reais = float(input("Digite uma quantia em reais: R$"))
cotacao = 5.28
qnde = reais / cotacao
print(f"Com R${reais}, o dolar valendo U${cotacao} (06/03/2026), é possivel comprar U${qnde:.2f}")


''' 3 
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com
5% de desconto.
'''
preco = float(input("Preço do produto: R$"))
novo_valor = preco - (preco * 0.5)
print(f"Novo preço com 5% de desconto: R${novo_valor:.2f}")


''' 4
Criar um algoritmo que leia um número e mostre o seu dobro, triplo e a sua raiz
quadrada
'''
numero = int(input("Digite um número: "))
raiz = sqrt(numero)
print(f"Dobro: {numero*2}; Triplo: {numero*3}; Raiz: {raiz}")

''' 5
Faça um programa que leia a largura e a altura de uma parede em Metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
lata de tinta pinta uma área de 2m².
'''
largura = float(input("Largura: "))
altura = float(input("Altura: "))
area =largura*altura
qnde = area / 2
print(f"Para pintar a pareda com área: {qnde}m², é preciso {qnde} baldes de tinta")



''' 6
Desenvolva um programa que leia 4 notas de um aluno e calcule a sua média
aritmética.
'''

notas = list()
for c in range(4):
    notas.append(float(input(f"Digite a {c + 1}ª Nota: ")))
somatoria = 0
for nota in notas:
    somatoria += nota
print(f"A média do aluno foi: {somatoria / 4:.2f}")

''' 7
Escreva um programa que leia um valor em metros e exiba o valor convertido em 
centímetros e milímetros.
'''
metro = float(input("Digite um valor em metros: "))
print(f"{metro}m: {metro*100} cm; {metro*1000}mm")

''' 8
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário 
com 15% de aumento
'''
salario = float(input("Digite o salário do funcionário: R$"))
print(f"Novo salário com reajuste de 15%: R${salario+(salario*0.15)}")

''' 9
Faça um programa que leia um número qualquer e exiba sua tabuada na tela. 
'''

numero = int(input("Digite um número qualquer"))

print(f"1 x {numero} = {1*numero}")
print(f"2 x {numero} = {2*numero}")
print(f"3 x {numero} = {3*numero}")
print(f"4 x {numero} = {4*numero}")
print(f"5 x {numero} = {5*numero}")
print(f"6 x {numero} = {6*numero}")
print(f"7 x {numero} = {7*numero}")
print(f"8 x {numero} = {8*numero}")
print(f"9 x {numero} = {9*numero}")
print(f"10 x {numero} = {10*numero}")

'''
10. Faça um programa que leia três números e mostre qual é o maior e qual é o 
menor entre eles.
'''
numero = []

for c in range(3):
    numero.append(int(input(f"Digite o {c+1} número: ")))
numero.sort(reverse=True)
print(f"O maior número é {numero[0]}")
numero.sort(reverse=False)
print(f"O menor número é {numero[0]}")

''' 11
 Escreva um programa que faça o computador "Pensar" em um número inteiro 
entre 0 e 5 e solicite ao usuário que tente adivinhar qual foi o número escolhido 
pelo computador.
'''
numero = randint(1, 5)
chute = int(input("Pensei em um numero entre 1 e 5, tente advinhar qual é: "))
if chute == numero:
    print("Parabéns, acertou!")
else:
    print("Infelizmente não acertou")
''' 12

'''

