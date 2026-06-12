import requests

'''
Data
Dia da semana
Descrição do tempo
Temp min
Temp max
Vel vento
umidade Rela do ar
nasc do sol
por do sol
fase lua
'''
print("\n")
print(" Previsão do tempo dos próximos 5 dias em São Paulo - SP")
print("\n")

#Converte data no formato AAAAMMdd em dd/MM/AAAA
def converter_data_texto(data):
    ano = data[:4]
    mes = data[4:6]
    dia = data[6:]
    return f"{dia}/{mes}/{ano}"

# Função que consome o dicionario com os dados do dia X e os imprime na tela
def info_clima(clima_dia):
    print(f"===== {converter_data_texto(clima_dia["date"])} - {clima_dia["name"]} =====")
    
    print(f"Descrição do tempo: {clima_dia["symbol_description"]}")

    print(f"MAXIMA: {clima_dia["tempmax"]} {clima_dia["units"]["temp"]} | MINIMA: {clima_dia["tempmin"]} {clima_dia["units"]["temp"]}")

    print(f"Velocidade dos ventos: {clima_dia["wind"]["speed"]} {clima_dia["units"]["wind"]}")

    print(f"Humidade relativa do ar: {clima_dia["humidity"]}%")

    print(f"Nascer do sol: {clima_dia["sun"]["in"]} | Pôr do sol: {clima_dia["sun"]["out"]}")

    print(f"Fase da lua no dia: {clima_dia["moon"]["desc"]}")

# Requisição
data_request = requests.get("http://api.tempo.com/index.php?api_lang=br&localidad=12996&affiliate_id=tk99un15usak&v=3.0")

# Serialização da response
resposta_obj = data_request.json()


for c in range(len(resposta_obj["day"])):
    info_clima(resposta_obj["day"][f"{c+1}"])
    print("\n")