import pyautogui
pyautogui.PAUSE = 0.8
import time

def abrir_explorador_de_arquivos():
    # Pressiona a tecla "Win" para abrir o menu Iniciar
    pyautogui.press("win")
    time.sleep(1)

    # Digita "Explorador de arquivos" e pressiona "Enter"
    pyautogui.write("Explorador de arquivos")
    pyautogui.press("enter")
    time.sleep(0.5)

    # Navega pelas opções no explorador de arquivos (5 vezes)
    for _ in range(5):
        pyautogui.press("tab")
        time.sleep(0.3)

    # Digita o caminho da pasta "Downloads"
    pyautogui.write("downloads")
    time.sleep(0.4)
    pyautogui.press("enter")
    time.sleep(0.8)

    # Seleciona o último arquivo baixado (coordenadas: x=759, y=351)
    pyautogui.click(x=254, y=208)
    pyautogui.hotkey("ctrl", "x")
    time.sleep(0.4)

    # Navega para outra parte da janela (8 tabs)
    for _ in range(8):
        pyautogui.press("tab")
        #time.sleep(0.3)

# Chama a função para executar as ações
abrir_explorador_de_arquivos()
