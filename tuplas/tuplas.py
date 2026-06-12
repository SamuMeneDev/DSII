''' 1 '''

tupla1 = (200, 1100, 41, 28, 99, 100)

print(sum(tupla1))

''' 2 '''

tupla2 = (2023, 2200, 5000, 99, 300, 14, 9, 11, 21, 54, 1)
print(f'O maior valor é: {max(tupla2)}. O menor valor é: {min(tupla2)}')

''' 3 '''
tupla3 = ('Elisangela','Ricardo','Rafael','Thamires','Fernanda','Camila','Beatriz','Wanderson','Anderson')

def ordenar_nomes(tupla):
    return sorted(tupla)
print(ordenar_nomes(tupla3))

''' 4 '''

tupla4 = (200,400,60000,90000,13,27,93,100,205)
tupla5 = (1900,2026,1041,290,97,88,23,22,1)
lista_aux = []
for c in range(len(tupla4)):
    lista_aux.append(tupla4[c] + tupla5[c])
print(tuple(lista_aux))

''' 5 '''
tupla6 = (2,300,90,120,200,2,45,89,2,8000,900,999,56,2,77)

print(tupla6.count(2))

''' 6 '''


lista_registro = [
    ('Clodoaldo', '11944758895'),
    ('Junior', '11955548998'),
    ('Aline', '11999999998'),
    ('Rosangela', '11947791539'),
    ('Vanessa', '11957798462'),
    ('Allan', '11987799999'),
    ('Regiane', '11944788923'),
    ('Elaine', '11993564879')
]
''' 7 '''

tupla8 = (2000,300,True,'312N','555',89,1990,300,'São Paulo-Capital',2023,257,999,654,712,
'Estação Itaquera',False,400,221,'Estação Guaianazes')

print(tupla8[5:8])
print(tupla8[3:15])

''' 8 '''

numFixos= (45, 23, 67, 12, 89, 34, 56, 78, 90, 10, 20, 30, 70, 5, 15)

print(sorted(numFixos, reverse=True))

''' 9 '''

palavras= ("python", "programação", "tupla", "lista", "dicionário",
"string", "algoritmo", "computador", "aplicação", "desenvolvimento",
"aprender", "ensinar", "conhecimento", "inteligência", "artificial")

print(sorted(palavras, reverse=True))

''' 10 '''
times_futebol = ("Real Madrid", "Barcelona", "Manchester City",
"Liverpool", "Bayern de Munique", "Paris Saint-Germain", "Chelsea",
"Juventus", "Borussia Dortmund", "Atlético de Madrid")

time1, time2, time3, time4, time5, time6, time7, time8, time9, time10 = times_futebol

''' 11 '''
numeros = (1981,2222,2014,1970,1982,233,567,2000,99,89)
novos_numeros = numeros[:-2]

''' 12 '''

times_futebol = ("Real Madrid", "Barcelona", "Manchester City",
"Liverpool", "Bayern de Munique", "Paris Saint-Germain", "Chelsea",
"Juventus", "Borussia Dortmund", "Atlético de Madrid")

novos_times = times_futebol[:5] + times_futebol[6:]

''' 13 '''

lista_times = []
for c in range(len(times_futebol)):
    if times_futebol[c] != "Real Madrid" or times_futebol[c] != "Juventus":
        lista_times.append(times_futebol[c])

novos_times = tuple(lista_times)

