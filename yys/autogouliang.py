import pyautogui
import time
import random
#gouliang

#pyautogui.locateOnScreen('F:\\bofang.png')

#position = pyautogui.locateCenterOnScreen('F:\\bofang.png')
#if position:
#  pyautogui.moveTo(position[0],position[1],duration=10)

def clickButton(fileName):
  position = pyautogui.locateCenterOnScreen(fileName)
  leftUpPos = pyautogui.locateOnScreen(fileName)
  if position:
    randomPos = [random.randrange(leftUpPos[0], leftUpPos[0]+leftUpPos[2]),random.randrange(leftUpPos[1],leftUpPos[1]+leftUpPos[3])]
    pyautogui.moveTo(randomPos[0],randomPos[1],duration=3)
    pyautogui.click()
    randomTime = random.randrange(0,5)
    time.sleep(randomTime)
  return position

def DragButton(fileName,offset):
  position = pyautogui.locateCenterOnScreen(fileName)
  if position:
    pyautogui.moveTo(position[0],position[1],duration=3)
    pyautogui.dragRel(offset[0],offset[1],5,button='left')
    randomTime = random.randrange(0,3)
    time.sleep(randomTime)
  return position


random.seed()
  
while True:
  position = clickButton("jiyang.png")
  if position:
    position = clickButton("quanbu.png")
    if position:
      position = clickButton("Nsmall.png")
      if position:
        offset = [486, 3]
        position = DragButton('huakuai.png',offset)
        if position:
          position = clickButton('gouliang.png')
          if position:
            position = clickButton('queding.png')
            if position:
              position = clickButton('tuichujiyang.png')
  else:
    time.sleep(200) 