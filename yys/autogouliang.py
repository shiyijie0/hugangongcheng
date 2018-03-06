# -*- coding: cp936 -*-
import pyautogui
import time
import random
import threading
#gouliang

#pyautogui.locateOnScreen('F:\\bofang.png')

#position = pyautogui.locateCenterOnScreen('F:\\bofang.png')
#if position:
#  pyautogui.moveTo(position[0],position[1],duration=10)

def Capture(fileName):
  t = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
  tstr = 'Captures/' + t + fileName + '.png'
  pyautogui.screenshot(tstr)

def clickButton(fileName):
  leftUpPos = pyautogui.locateOnScreen(fileName)
  randomPos = leftUpPos
  if leftUpPos:
    randomPos = [random.randrange(leftUpPos[0], leftUpPos[0]+leftUpPos[2]),random.randrange(leftUpPos[1],leftUpPos[1]+leftUpPos[3])]
    pyautogui.moveTo(randomPos[0],randomPos[1], 2, pyautogui.easeInQuad)
    pyautogui.click()
    randomTime = random.randrange(3,7)
    time.sleep(randomTime)
    Capture('clk')
    print('按钮：', fileName, '[', randomPos[0],randomPos[1], ']')
  else:
    print('没有找到按钮：' + fileName)
  return randomPos

def DragButton(fileName,offset):
  position = pyautogui.locateCenterOnScreen(fileName)
  if position:
    pyautogui.moveTo(position[0],position[1],duration=3)
    pyautogui.dragRel(offset[0],offset[1],5,button='left')
    randomTime = random.randrange(2,3)
    time.sleep(randomTime)
  return position
  
def DragButtonToFind(fileName,toFind,pixelLimit):
  position = pyautogui.locateCenterOnScreen(fileName)
  if position:
    pyautogui.moveTo(position[0],position[1],duration=3)
    offset = 0
    while offset < pixelLimit:
      randomDrag = random.randrange(0,1)
      pyautogui.dragRel(10,0,randomDrag,button='left')
      founded = pyautogui.locateOnScreen(toFind)
      if founded:
        return True
      else:
        offset = offset + randomDrag
    randomTime = random.randrange(1,2)
    time.sleep(randomTime)
  return False


def HasImage(fileName):
  leftUpPos = pyautogui.locateOnScreen(fileName)  
  if leftUpPos:
    return True
  else:
    return False

Capture('start')
random.seed()

#
def Autojiyang():
  Capture('TimeToStart')
  while True:
    position = clickButton("jiyang.png")
    if position:
      position = clickButton("quanbu.png")
      if position:
        position = clickButton("Nsmall.png")
        if position:
          #offset = [486, 3]
          #position = DragButton('huakuai.png',offset)
          founded = DragButtonToFind('huakuai.png','gouliang.png',486)
          if founded:
            position = clickButton('gouliang.png')
            if position:
              position = clickButton('queding.png')
              if position:
                position = clickButton('tuichujiyang.png')
                if position:
                  #寄养完毕，六小时之后继续
                  timer=threading.Timer(6*60*60,Autojiyang)
                  timer.start()
                  #该循环终止
                  return
      else: #没有找到quanbu按钮
        randomTime = random.randrange(1,3)
        time.sleep(randomTime) # try clickButton again after 10 sec  
    else:#error, failed to click jiyang flag
      Capture('JiyangBtnfailure')
      #如果被打开了悬赏封印窗口，则点取消
      if(HasImage('xuanshangfengyin.png')):
        clickButton('quxiaoxuanshang.png')
      #如果已经打开了寄养界面(判断右下角图案，则点击tuichujiyang
      if(HasImage('jiyangjiemian.png')):
        clickButton('tuichujiyang.png')
        time.sleep(1)


timer=threading.Timer((6*60*60)-(6*60),Autojiyang)
timer.start()        