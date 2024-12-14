import pyautogui
import time
pyautogui.PAUSE = 0.8

# Abre Chrome
with open("Abre_Chrome.py") as abre_chrome:
    exec(abre_chrome.read())
    time.sleep(1)

#Seleciona Menu
time.sleep(0.5)
pyautogui.click(x=36, y=174) #100% ZOOM
#pyautogui.click(x=40, y=181) #110% ZOOM
#pyautogui.click(x=44, y=189) #125% ZOOM
#time.sleep(0.5)

# Menu Acdemico
pyautogui.click(x=46, y=247) #100% ZOOM
#pyautogui.click(x=66, y=254) #110% ZOOM
#pyautogui.click(x=98, y=286) #125% ZOOM
#time.sleep(0.5)

#Menu ingresso de alunos
pyautogui.click(x=88, y=505) #100% ZOOM
#pyautogui.click(x=85, y=540) #110% ZOOM
#pyautogui.click(x=135, y=608) #125% ZOOM
#time.sleep(0.5)

#Menu rematricula
pyautogui.click(x=155, y=634) #100% ZOOM
#pyautogui.click(x=183, y=679) #110% ZOOM
#pyautogui.click(x=302, y=786) #125% ZOOM
#time.sleep(0.5)

#Selecao empresa
pyautogui.click(x=165, y=274) #100% ZOOM
#pyautogui.click(x=150, y=290) #110% ZOOM
#pyautogui.click(x=496, y=313) #125% ZOOM
#time.sleep(1)

#Seleciona Empresas em Branco(traz todas empresas)
for _ in range(5):
    pyautogui.press("down")
pyautogui.press("tab")

#Inclui data final 31 12 2024
for _ in range(4):
    pyautogui.press("tab")  
pyautogui.press("home")
for _ in range(4):
    pyautogui.press("delete")
pyautogui.write("3112") #ref data 31 12 2024
time.sleep(.5)

#Vai ate menu Download
for _ in range(3):
    pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(9)

with open("abrir_explorador_de_arquivos.py") as abrir_explorador_de_arquivos:
    exec(abrir_explorador_de_arquivos.read())
    time.sleep(3.5)

pyautogui.write("G:/Meu Drive/Financeiro/2024/Recebidos/Todos")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("alt", "f4")
time.sleep(1)
