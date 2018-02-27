import pyautogui
import time
#gouliang

#pyautogui.locateOnScreen('F:\\bofang.png')

#position = pyautogui.locateCenterOnScreen('F:\\bofang.png')
#if position:
#  pyautogui.moveTo(position[0],position[1],duration=10)
while True:
  position = pyautogui.locateCenterOnScreen("jiyang.png")
  if position:
    pyautogui.moveTo(position[0],position[1],duration=3)
    pyautogui.click()
    time.sleep(3)
    position = pyautogui.locateCenterOnScreen("quanbu.png")
    if position:
      pyautogui.moveTo(position[0],position[1],duration=3)
      pyautogui.click()
      time.sleep(2)
      position = pyautogui.locateCenterOnScreen("Nsmall.png")
      if position:
        pyautogui.moveTo(position[0],position[1],duration=2)
        pyautogui.click()
        time.sleep(2)
        position = pyautogui.locateCenterOnScreen('huakuai.png')
        if position:
          pyautogui.moveTo(position[0],position[1],duration=5)
          pyautogui.dragRel(480,5,button='left')
          time.sleep(2)
          position = pyautogui.locateCenterOnScreen('gouliang.png')
          if position:
            pyautogui.moveTo(position[0],position[1],duration=1)
            pyautogui.click()
            time.sleep(5)
            position = pyautogui.locateCenterOnScreen('queding.png')
            if position:
              pyautogui.moveTo(position[0],position[1],duration=3)
              pyautogui.click()
              time.sleep(5)
              position = pyautogui.locateCenterOnScreen('tuichujiyang.png')
              if position:
                pyautogui.moveTo(position[0],position[1],duration=2)
                pyautogui.click()
                time.sleep(5)
  else:
    time.sleep(200) 