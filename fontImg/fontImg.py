import msvcrt
from PIL import Image
import sys
def imgToFontImg(src,output="img-text.txt"):
    try:
        IMG = src
        WIDTH = 300
        HEIGHT = 160
        OUTPUT = output
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        def get_char(r,g,b,alpha = 256):
            if alpha == 0:
                return ' '
            length = len(ascii_char)
            gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            unit = (255.0 + 1)/length
            return ascii_char[int(gray/unit)]
        if __name__ == '__main__':
            im = Image.open(IMG)
            im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
            txt = ""
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    txt += get_char(*im.getpixel((j,i)))
                txt += '\n'
            with open(OUTPUT,'w') as f:
                f.write(txt)
        msvcrt.getch()
        return 1
    except:
        print("pinkcandy run error")
        return 0

while True:
    print("pinkcandy 字符画生成程序")
    print("图片文件放入当前位置输入名称开始转换,可以空格指定输出txt文件名称。\n例：test1.jpg test1_out.txt\n输入q退出程序")
    userInput = list(map(str,input().split(" ")))
    src = userInput[0]
    try:output = userInput[1]
    except:output=""
    if userInput[0]=="q":
        sys.exit()
    else:
        print("就绪 按回车开始转换")
        OUTPUT = imgToFontImg(src,output)
        if OUTPUT==1:
            f = open(output,"r",encoding="UTF-8")
            outStr = f.read()
            print(outStr)
            for i in range(10):print()
            print("pinkcandy done")