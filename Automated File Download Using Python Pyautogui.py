import pyautogui
import time
import os

pyautogui.PAUSE = 1.2

#Open Browser Function
def abrir_chrome():
    try:            
        os.chdir(r'G:\Meu Drive\Python\AutomatiMannesoft\Auxiliares')
        with open("Open_Chrome.py") as abre_chrome:
            exec(abre_chrome.read())
        time.sleep(1)
        pyautogui.press("F5")
        time.sleep(1)
        pyautogui.press("HOME")
        time.sleep(1)
    except Exception as e:
        print(f"Error in abrir_chrome: {e}")

#Go to Receivables Menu Function
def clicar_menu_baixas():
    pyautogui.PAUSE = 1.81
    time.sleep(1)
    try:
        with open("clica_menu_baixas.py") as clica_menu_baixas:
            exec(clica_menu_baixas.read())
        time.sleep(1)
    except Exception as e:
        print(f"Error in clicar_menu_baixas: {e}")

# Variable to count executions
execucoes = 0

def selecionar_empresa():
    global execucoes
    try:
        pyautogui.click(x=222, y=243)  # Select Company
        if execucoes == 1:
            for _ in range(5):
                pyautogui.press("down")
        else:
            pyautogui.press("down")
        pyautogui.press("tab")
        for _ in range(11):
            pyautogui.press("tab")
        execucoes += 1
    except Exception as e:
        print(f"Error in selecionar_empresa: {e}")

#Inset data Function
def inserir_data():
    try:
        pyautogui.write("01012026")
        pyautogui.press("tab")
        pyautogui.write("31122026")
        for _ in range(3):
            pyautogui.press("tab")
    except Exception as e:
        print(f"Error in inserir_data: {e}")

#Select expecific payments Function
def selecionar_matricula():
    try:
        for _ in range(11):
            pyautogui.press("down")
        for _ in range(6):
            pyautogui.press("tab")
        #select with contracts
        for _ in range(3):
            pyautogui.press("up")
        for _ in range(4):
            pyautogui.press("tab")
        pyautogui.press("right")
        pyautogui.press("tab")
        pyautogui.press("enter")
    except Exception as e:
        print(f"Error in selecionar_matricula: {e}")

#Inset data Function
def abrir_explorador(caminho):
    try:
        with open("abrir_explorador_de_arquivos.py") as abrir_explorador_de_arquivos:
            exec(abrir_explorador_de_arquivos.read())
        time.sleep(1)
        pyautogui.write(caminho)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.hotkey("alt", "f4")
        time.sleep(1)
    except Exception as e:
        print(f"Error in abrir_explorador: {e}")

#Global functions
def main():
    global execucoes
    try:
        Open_chrome()
        clicar_menu_baixas()
        selecionar_empresa()
        inserir_data()
        selecionar_matricula()
        abrir_explorador("G:/Meu Drive/Financeiro/2026/Company1")
        time.sleep(1)

        # secound company
        execucoes = 1
        Open_chrome()
        selecionar_empresa()
        inserir_data()
        selecionar_matricula()
        abrir_explorador("G:/Meu Drive/Financeiro/2026/Company2")

    except Exception as e:
        print(f"Ocorreu um erro no main: {e}")

if __name__ == "__main__":
    main()

print('END Receivables 2026')


