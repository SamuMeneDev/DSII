# 1
PI = 3.1415

raio = float(input("Digite o raio da lata de óleo (cm): "))
altura = float(input("Digite a altura da lata de óleo (cm): "))

# V = PI * r² * h
volume = PI * raio**2 * altura

print(f"O volume da lata é de: {volume:.2f} cm³")

# 2

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nasc

if idade < 10:
    print(f"Idade: {idade} | Criança")
elif idade < 18:
    print(f"Idade: {idade} | Adolescente")
elif idade < 60:
    print(f"Idade: {idade} | Adulto")
else:
    print(f"Idade: {idade} | Idoso")

# 3

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))
c = int(input("Digite o valor C: "))

valores = [a, b, c]

maior_ab = (a + b + abs(a-b)) / 2

def saida_maior(maior, valores):
    for num in valores:
        if maior == num:
            print(f"O numero {num} eh o maior")
if maior_ab > c:
    saida_maior(maior_ab, valores)
else:
    saida_maior(c, valores)

# 4

idade_dias = int(input("Digite sua idade em dias: "))

print("Sua idade em...")

print(f"DIAS: {idade_dias}")

idade_mes = idade_dias / 30
print(f"MESES: {idade_mes:.0f}")

idade_ano = idade_dias / 365
print(f"ANOS: {idade_ano:.0f}")

# 5

# Função de fatorial usando recursão
# (Multiplica todos os valores subsequentes chamando a mesma função, se for 0 retorna 1, isso vale tambem
#  para o ultimo valor na recursão)
def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)
    
num = int(input("Digite um valor para calcular seu fatorial: "))

print(f"O fatorial de {num} ({num}!) é igual a {fatorial(num)}")
