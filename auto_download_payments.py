import pyautogui
import time

#Seleciona Velociadade
with open("seleciona_velocidade.py") as seleciona_velocidade:
    exec(seleciona_velocidade.read())

# Abre Chrome
with open("Abre_Chrome.py") as abre_chrome:
    exec(abre_chrome.read())
    time.sleep(1)

# Clica menu baixas
with open("clica_menu_baixas.py") as clica_menu_baixas:
    exec(clica_menu_baixas.read())
    time.sleep(1)

#menu seleciona empresa
def seleciona_empresa():
    #time.sleep(0.5)
    pyautogui.click(x=193, y=275) #100% ZOOM
    #pyautogui.click(x=249, y=288) #110% ZOOM
seleciona_empresa()

pyautogui.press("down")
pyautogui.press("tab")
for _ in range(11):
    pyautogui.press("tab")
    #time.sleep(.5)

#insere a data
pyautogui.write("01012024")
pyautogui.press("tab")
pyautogui.write("31122024")
#pyautogui.press("tab")

for _ in range(3):
    pyautogui.press("tab")

#Seleciona Matricula
for _ in range(11):
    pyautogui.press("down")

for _ in range(6):
    pyautogui.press("tab")

for _ in range(3):
    pyautogui.press("up")

for _ in range(4):
    pyautogui.press("tab")  

pyautogui.press("right")
pyautogui.press("tab")
pyautogui.press("enter")

#PEga arquivo e salva na pasta correta
with open("abrir_explorador_de_arquivos.py") as abrir_explorador_de_arquivos:
    exec(abrir_explorador_de_arquivos.read())
    time.sleep(1)

pyautogui.write("G:/Meu Drive/Financeiro/2024/Recebidos/Empresa1/Matricula/Por Doc")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("alt", "f4")

### #### ##### ####### ########## ###########

#Abre Chrome
abre_chrome()

#Download Baixas Aloise Matriculas
time.sleep(1)

#menu seleciona empresa
seleciona_empresa()
    
for _ in range(3):
    pyautogui.press("down")

pyautogui.press("tab")
for _ in range(11):
    pyautogui.press("tab")
    #time.sleep(.5)

#insere a data
pyautogui.write("01012024")
pyautogui.press("tab")
pyautogui.write("31122024")
#pyautogui.press("tab")

for _ in range(3):
    pyautogui.press("tab")

#Seleciona Matricula
for _ in range(11):
    pyautogui.press("down")

for _ in range(6):
    pyautogui.press("tab")

#for _ in range(3):
#    pyautogui.press("up")

for _ in range(4):
    pyautogui.press("tab")  

pyautogui.press("right")
pyautogui.press("tab")
pyautogui.press("enter")

# Chama a função para executar as ações
abrir_explorador_de_arquivos()

pyautogui.write("G:/Meu Drive/Financeiro/2024/Recebidos/Empresa2/Matricula/Por Doc")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("alt", "f4")

### ### ### ### ### ### ### ### ### ### ### ### ###
#Abre Chrome
abre_chrome()

#Download Baixas WHALUZ Matriculas
#menu mannesoft Point(x=44, y=189
time.sleep(1)

#menu seleciona empresa
seleciona_empresa()

for _ in range(5):
    pyautogui.press("down")

pyautogui.press("tab")
for _ in range(11):
    pyautogui.press("tab")
    #time.sleep(.5)

#insere a data
pyautogui.write("01012024")
pyautogui.press("tab")
pyautogui.write("31122024")
#pyautogui.press("tab")

for _ in range(3):
    pyautogui.press("tab")

#Seleciona Matricula
for _ in range(11):
    pyautogui.press("down")

for _ in range(6):
    pyautogui.press("tab")

for _ in range(3):
    pyautogui.press("up")

for _ in range(4):
    pyautogui.press("tab")  

pyautogui.press("right")
pyautogui.press("tab")
pyautogui.press("enter")

# Chama a função para executar as ações
abrir_explorador_de_arquivos()

pyautogui.write("G:/Meu Drive/Financeiro/2024/Recebidos/Empresa3/Matricula/Por Doc")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("alt", "f4")
time.sleep(1)
