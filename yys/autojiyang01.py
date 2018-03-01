import pyautogui
import time
import random
#gouliang

#pyautogui.locateOnScreen('F:\\bofang.png')

#position = pyautogui.locateCenterOnScreen('F:\\bofang.png')
#if position:
#  pyautogui.moveTo(position[0],position[1],duration=10)

def Capture(fileName):
  t = time.localtime()
  tstr = str(t.tm_year) + str(t.tm_mon) + str(t.tm_hour) + str(t.tm_min) + str(t.tm_sec) + fileName + '.png'
  pyautogui.screenshot(tstr)

def clickButton(fileName):
  leftUpPos = pyautogui.locateOnScreen(fileName)
  if leftUpPos:
    randomPos = [random.randrange(leftUpPos[0], leftUpPos[0]+leftUpPos[2]),random.randrange(leftUpPos[1],leftUpPos[1]+leftUpPos[3])]
    pyautogui.moveTo(randomPos[0],randomPos[1],duration=3)
    pyautogui.click()
    randomTime = random.randrange(1,3)
    time.sleep(randomTime)
    print('按钮：', fileName, '[', randomPos[0],randomPos[1], ']')
    Capture('clk')
  return randomPos

def DragButton(fileName,offset):
  position = pyautogui.locateCenterOnScreen(fileName)
  if position:
    pyautogui.moveTo(position[0],position[1],duration=3)
    pyautogui.dragRel(offset[0],offset[1],5,button='left')
    randomTime = random.randrange(1,3)
    time.sleep(randomTime)
  return position
  

def HasImage(fileName)
  leftUpPos = pyautogui.locateOnScreen(fileName)  
  if leftUpPos:
    return True
  else:
    return False

Capture('start')

sleepTime = 3*60;
time.sleep(sleepTime)
ScreenSize = pyautogui.size()

random.seed()
  
while True:
  if(clickRange(centerPos)): #点击屏幕中间区域，暂且需要一个类似的点击Range的函数
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
              if position:
                #寄养完毕,sleep 6小时
                time.sleep(6*60);
    else if(HasImage('jiyangjiemian.png')): #No quanbu button
      clickButton('tuichujiyang.png')
      time.sleep(10) # try clickRange again after 10 sec      
  else:#error, failed to click jiyang flag
    Capture('JiyangBtnfailure') 
    #如果打开了寄养界面(判断右下角图案，则点击tuichujiyang
    if(HasImage('jiyangjiemian.png')):
      clickButton('tuichujiyang.png')