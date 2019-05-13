#First Python Script
#All I Can Say Is, Spam Machine Broke AF
import pyautogui
import time

#pyautogui.displayMousePosition()
#DiscordPosition = '1057, 1918'
#MessagesPosition = '1397, 1922'
#MessagengerPosition = '1264, 2013'

pyautogui.click([1057, 1918]) #Set The Mouse Position

while pyautogui.position() == (1057, 1918): #Set The Mouse Position
    pyautogui.typewrite('Text goes here') #Set Spam Text
    pyautogui.press('enter')
    time.sleep(1) #Set Sleep Time; Work Around For Message Cooldown
    if pyautogui.position() != (1057, 1918): #Set The Mouse Position
        break
print('Spamming Successful')
    
