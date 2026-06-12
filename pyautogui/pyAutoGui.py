import pyautogui
from time import sleep

# 1. Tamanho da tela
print(pyautogui.size())

# 2. Nome das teclas

print(pyautogui.KEY_NAMES)

# 3. Calendário
pyautogui.moveTo(1820, 1062) # 1820, 1062 (Na minha máquina)
sleep(2) # Espera por preucaução
pyautogui.click()


# 4. Pesquisar 'PyAutoGui' no Bing

pyautogui.press('winleft') # Menu iniciar
pyautogui.write("chrome")
pyautogui.press('enter')
sleep(5) # Tempo para abrir o programa
pyautogui.write('https://www.bing.com/')
pyautogui.press('enter')
sleep(5) # Tempo para carregar a página
pyautogui.write('PyAutoGui')


# 5. 
print(pyautogui.size())

# 6. Print da tela
img = pyautogui.screenshot()

# 7.
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
sleep(3)
pyautogui.write("terra.com.br ")
pyautogui.press("enter")
sleep(3)
pyautogui.moveTo(1595, 25)

pyautogui.screenshot("imagemEncontrada.png")
pyautogui.alert(title="Imagem", text=f"Imagem na posição X={1595}|Y={25}")

# 8.
pyautogui.alert(title="Aviso", text="Conexão bem-sucedida")

# 9. 
opt = pyautogui.confirm(title="Aviso", text="Escolha um", buttons=["Sim", "Não", "Talvez"])
pyautogui.alert(title="Aviso", text=f"Sua resposta: {opt}")


# 10. 
mes = pyautogui.confirm(title="Meses", text="Escolha um mes", buttons=["Janeiro", "Fevereiro", "Março"])
resultado = "Correta" if mes=="Março" else "Incorreta"

pyautogui.alert(title="Mês", text=f"Opção {resultado}")

# *
im1 = pyautogui.screenshot("captura062024")

# Utilitário para achar as cordenadas
def achar_cord():
    while True:
        x, y = pyautogui.position()
        print(f"X = {x} | Y = {y} ")
