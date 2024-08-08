import pyautogui
import time
pyautogui.PAUSE = 0.75

#Abre Chrome
pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

#Abre nova aba
pyautogui.hotkey("ctrl", "t")

#Entra no Mannesoft Prime
pyautogui.write("https://5f252c.mannesoftprime.com.br/mannesoft/login.php")
pyautogui.press("enter")

#Faz Login
pyautogui.write('USER')
pyautogui.press("tab")
pyautogui.write('PASSWORD')
pyautogui.press("enter")

#Abre nova aba
pyautogui.hotkey("ctrl", "t")
time.sleep(5)
pyautogui.write("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.press("enter")

#Clica no primeiro email da caixa
#Point(x=479, y=245) primeiro email da caixa
time.sleep(10)
pyautogui.click(x=431, y=250) # 100# ZOOM
#pyautogui.click(x=492, y=253) # 110# ZOOM
#pyautogui.click(x=492, y=253) # 125# ZOOM
time.sleep(3)

#Coleata o token

pyautogui.doubleClick(x=986, y=651) # 100# ZOOM
#pyautogui.doubleClick(x=1098, y=706) # 110# ZOOM
#pyautogui.doubleClick(x=1078, y=663) # 125# ZOOM
#time.sleep(1)

#Copia Token
pyautogui.hotkey("ctrl", "c")
time.sleep(.5)

#Navega até pagina Mannesoft
pyautogui.hotkey("ctrl", "tab")
pyautogui.hotkey("ctrl", "tab")
time.sleep(.5)

#Cola Token
pyautogui.hotkey("ctrl", "v")
time.sleep(.5)
pyautogui.press("enter")
time.sleep(1)
