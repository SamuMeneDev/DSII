import requests

data_request = {}

opcoes = {
    0: ["Sair (X)"],
    1: ["Dolar (USD)", "USD"],
    2: ["Peso argentino (ARS)", "ARS"],
    3: ["Etherum (ETH)", "ETH"]
}

def mostrar_opcoes():
    for indice, moeda in opcoes.items():
        print(f'[{indice}] = {moeda[0]}')

acao = -1 # Valor inicial para satisfazer a condição do loop

# Enquanto não for 0 (código de parada)
while acao != 0:
    mostrar_opcoes()
    acao = int(input("Selecione a moeda para ver a cotação atual:"))

    if acao <= 0: # Fim do programa
        break
    else: # Faz a requisição da moeda escolhida

        request = requests.get(f'https://economia.awesomeapi.com.br/all/{opcoes[acao][1]}-BRL')
        
        data_request = request.json() # Serialização da requisição
        
        # 1 (Nome da moeda escolhida) = R$ (Valor da moeda em Reais)
        print(f'1 {opcoes[acao][0]} = R${data_request[opcoes[acao][1]]["bid"]}')

print("="*10)
print("FIM")
print("="*10)