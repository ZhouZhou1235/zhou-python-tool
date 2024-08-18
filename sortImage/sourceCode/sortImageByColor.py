# 命令行批处理程序 按颜色分类存放图片

import cv2
import numpy as np
import collections
import os
import shutil
import random
import sys

def makeDir(mode=1):
    # 创建文件夹
    try: os.mkdir("./sortArea")
    except: pass
    try:
        if mode==1:
            os.mkdir("./sortArea/黑black")
            os.mkdir("./sortArea/灰gray")
            os.mkdir("./sortArea/白white")
        os.mkdir("./sortArea/红red")
        os.mkdir("./sortArea/橙orange")
        os.mkdir("./sortArea/黄yellow")
        os.mkdir("./sortArea/绿green")
        os.mkdir("./sortArea/青cyan")
        os.mkdir("./sortArea/蓝blue")
        os.mkdir("./sortArea/紫purple")
    except: pass

def getColorList(mode=1):
    # opencv 自定义颜色表 return dict字典
    # mode 是否扫描黑白 1是 2否
    dict = collections.defaultdict(list)
    if mode==1:
        # 黑色
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 46])
        color_list = []
        color_list.append(lower_black)
        color_list.append(upper_black)
        dict['black'] = color_list
        # 灰色
        lower_gray = np.array([0, 0, 46])
        upper_gray = np.array([180, 43, 220])
        color_list = []
        color_list.append(lower_gray)
        color_list.append(upper_gray)
        dict['gray']=color_list
        # 白色
        lower_white = np.array([0, 0, 221])
        upper_white = np.array([180, 30, 255])
        color_list = []
        color_list.append(lower_white)
        color_list.append(upper_white)
        dict['white'] = color_list
    # 红色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red']=color_list
    # 橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list
    # 黄色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list
    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list
    # 青色
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list
    # 蓝色
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list
    # 紫色
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list
    return dict

def getColor(frame,mode=1):
    # 获取图片的主颜色
    # frame 图帧 cv2.imread(fileName) 获取
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = getColorList(mode)
    for d in color_dict:
        mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
        # cv2.imwrite(d+'.jpg',mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary,None,iterations=2)
        cnts,x = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum+=cv2.contourArea(c)
        if sum > maxsum :
            maxsum = sum
            color = d
    return color

def judgeColorAndMove(fileName,fileUrl,mode=1):
    # 分辨颜色并移动图片
    isExist = os.path.exists(fileUrl)
    if isExist==False: return
    frame = cv2.imread(fileUrl)
    theColor = getColor(frame,mode)
    print(theColor)
    if theColor=="black":shutil.move(fileUrl,"./sortArea/黑black/"+fileName)
    if theColor=="gray":shutil.move(fileUrl,"./sortArea/灰gray/"+fileName)
    if theColor=="white":shutil.move(fileUrl,"./sortArea/白white/"+fileName)
    if theColor=="red":shutil.move(fileUrl,"./sortArea/红red/"+fileName)
    if theColor=="orange":shutil.move(fileUrl,"./sortArea/橙orange/"+fileName)
    if theColor=="yellow":shutil.move(fileUrl,"./sortArea/黄yellow/"+fileName)
    if theColor=="green":shutil.move(fileUrl,"./sortArea/绿green/"+fileName)
    if theColor=="cyan":shutil.move(fileUrl,"./sortArea/青cyan/"+fileName)
    if theColor=="blue":shutil.move(fileUrl,"./sortArea/蓝blue/"+fileName)
    if theColor=="purple":shutil.move(fileUrl,"./sortArea/紫purple/"+fileName)
    else: return 0

def renameFilesUseRandom(areaUrl):
    # 随机数重命名文件
    i = 0
    for root,dirs,files in os.walk(areaUrl):
        for theFile in files:
            (theFileName,theExt) = os.path.splitext(theFile)
            newFileName = str(i)+str(random.randint(1000000000,9999999999))+theExt
            try: os.rename(areaUrl+theFile,areaUrl+newFileName)
            except: pass

if __name__ == '__main__':
    areaUrl = "./sortArea/"
    while True:
        print("命令行批处理程序 按颜色分类存放图片")
        print("created by pinkcandyzhou")
        print("使用方法：将图片放到sortArea中 输入mode后立刻开始运行")
        print("mode 1扫描黑白灰 2不扫描黑白灰 3结束程序")
        try: mode = int(input("mode:"))
        except: continue
        if mode==3: sys.exit()
        makeDir(mode)
        renameFilesUseRandom(areaUrl)
        for root,dirs,files in os.walk(areaUrl):
            for theFile in files:
                try: judgeColorAndMove(theFile,areaUrl+theFile,mode)
                except: pass