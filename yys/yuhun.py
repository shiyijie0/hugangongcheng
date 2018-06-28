import pyautogui
import time
import random
#gouliang

def Capture(fileName):
  t = time.localtime()
  tstr = str(t.tm_year) + str(t.tm_mon) + str(t.tm_hour) + str(t.tm_min) + str(t.tm_sec) + fileName + '.png'
  pyautogui.screenshot(tstr)

def clickButton(fileName):
  leftUpPos = pyautogui.locateOnScreen(fileName)
  if leftUpPos:
    randomPos = [random.randrange(leftUpPos[0], leftUpPos[0]+leftUpPos[2]),random.randrange(leftUpPos[1],leftUpPos[1]+leftUpPos[3])]
    #pyautogui.moveTo(randomPos[0],randomPos[1],duration=1)
    pyautogui.click(randomPos[0],randomPos[1])
    randomTime = random.randrange(1,3)
    time.sleep(randomTime)
    print('按钮：', fileName, '[', randomPos[0],randomPos[1], ']')
    ##Capture('clk')
    return True
  return False

while True:
  if( True ): #点击屏幕中间区域，暂且需要一个类似的点击Range的函数
    position = clickButton("kaishizhandou.png") #找到开始战斗按钮
    if position:
      time.sleep(25) #sleep 20秒等战斗结束
      success = False
      finished = False
      while finished != True: #寻找标志战斗结束的按钮
        if clickButton("victory0.png"):
          #time.sleep(2)
          finished = False
          while finished != True:
            if clickButton("victory1.png"):
              finished = True
              #time.sleep(2)       
        elif clickButton("victory1.png"):
          #finished = True
          time.sleep(3)
          clickButton("victory1.png")
        elif clickButton("failure.png"):
          #time.sleep(2)
          finished = True
      clickButton("morenyaoqing.png")   
      clickButton("failurequeding.png")   
    else:
      time.sleep(3) # try clickRange again after 10 sec      
  