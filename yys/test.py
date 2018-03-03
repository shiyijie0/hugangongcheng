import pyautogui
import time
while True:
  leftUpPos = pyautogui.locateOnScreen('tuichujiyang.png')
  randomPos = leftUpPos
  if leftUpPos:
    print('valid')    
  else:
    print('invalid')
  time.sleep(5) 