import os,time,sys

# 文件类型列表
imgextList = [".jpg",".png",".gif",".jpeg",".svg",".webp",".tiff"]
videoextList = [".avi",".mp4",".mov",".wmv",".flv",".mkv",".webm"]
musicextList = [".mp3",".wma",".wav",".ogg"]

def doRename(modeNum=1,setSize=5000000):
    # 重命名函数
    # 遍历目录下所有文件夹
    for theDir in dirNames:
        doNum = 1
        filePath = ""
        fileList = []
        renamedFileList = []
        # 文件夹中不允许有子文件夹
        for i,j,k in os.walk("./"+theDir):
            fileList=k
            if j:
                print("pinkcandy error 文件夹中不允许有子文件夹")
                return
        # 遍历文件
        for theFile in fileList:
            # 获取文件信息
            filePath = "./"+theDir+"/"+theFile
            (theFileName,theExt) = os.path.splitext(filePath)
            theFileName = theFileName.replace("./"+theDir+"/","")
            info = os.stat(filePath)
            size = info.st_size
            size = size/1000000
            size = "%.4f"%size
            size = str(size)+"MB"
            createdTime = info.st_mtime
            arr1 = time.localtime(int(createdTime))
            createdTime = time.strftime("%Y-%m-%d",arr1)
            # 根据模式重命名
            if modeNum==1:
                theNewFileName = str(doNum)+",{"+theFileName+"},"+size+","+createdTime+theExt
            elif modeNum==2:
                if len(theFileName)>20: theFileName=theFileName[0:20]
                theNewFileName = str(doNum)+",{"+theFileName+"},"+size+","+createdTime+theExt
            elif modeNum==3:
                if theExt in imgextList: theNewFileName = str(doNum)+",{"+"imageFile图片文件"+"}"+theExt
                elif theExt in videoextList: theNewFileName = str(doNum)+",{"+"videoFile视频文件"+"}"+theExt
                elif theExt in musicextList: theNewFileName = str(doNum)+",{"+"musicFile音频文件"+"}"+theExt
                else: theNewFileName = str(doNum)+",{"+"file文件"+"}"+theExt
            else:
                print("pinkcandy error modeNum只能为1 2 3")
                return
            os.rename(filePath,"./"+theDir+"/"+theNewFileName)
            renamedFileList.append(theNewFileName)
            doNum += 1
        # 创建新文件夹
        newDirName = "bigFiles大文件"
        os.makedirs("./"+theDir+"/"+newDirName)
        # 遍历命名完毕的文件
        for theFile in renamedFileList:
            filePath = "./"+theDir+"/"+theFile
            info = os.stat(filePath)
            size = info.st_size
            # 超过设定值则移到新文件夹
            if size>setSize:
                os.rename(filePath,"./"+theDir+"/"+newDirName+"/"+theFile)
    print("pinkcandy done 完毕")
    x = input("本次循环终止 输入q退出 回车继续")
    if x=="q":
        sys.exit()

def main():
    # 主函数
    print("批量重命名和大小整理程序")
    print("modeNum 输入数字1/2/3 1保留原文件名称 2文件名称过长会截断 3重命名为统一的名字")
    print("setSize 输入大小整理数字 1MB=1000000")
    global path,dirNames,fileNames
    path,dirNames,fileNames = None,None,None
    for i,j,k in os.walk("./"):
        if j:
            path,dirNames,fileNames=i,j,k
            break
    if dirNames:
        try:
            modeNum = int(input("modeNum:"))
            setSize = int(input("setSize:"))
            doRename(modeNum,setSize)
        except:
            x = input("本次循环终止 输入q退出 回车继续")
            if x=="q":
                sys.exit()

if __name__=="__main__":
    # 执行入口
    while True:
        main()