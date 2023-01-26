from PIL import Image,ImageDraw,ImageFilter,ImageFont
import random
def randomChar():
    if random.randint(0,2) == 0:
        return(chr(random.randint(65,90)))
    elif random.randint(0,2)== 1:
        return(chr(random.randint(97,122)))
    else:
        return(chr(random.randint(48,57)))
def BGcolor(): # 随机生成背景色
     return(random.randint(135,255),random.randint(135,255), random.randint(135,255))
def Wordcolor(): # 随机生成字体颜色
    return(random.randint(32,127), random.randint(32,127), random.randint(32,127))
def CAPTCHA(): # 生成随机验证码
    global im
    im = Image.new("RGB" ,(400,100),(255,255,255))  #定义长宽为400和100的图片。
    global font
    font = ImageFont.truetype('C:/Windows/Fonts/ANTQUAI.TTF',60)
    global draw
    draw = ImageDraw.Draw(im)
    for x in range(400):
        for y in range(100):
            draw.point((x, y), BGcolor())
        words = ""
    for i in range(3):
        fillcolor = "RGB(%d,%d,%d)"%(random.randint(32,127),random.randint(32,127),random.randint(32,127))
        draw.line((35, random.randint(0, 130), random.randint(130, 150), random.randint(20, 130)), fill=fillcolor,width=random.randint(1, 5))
        draw.line((random.randint(20, 130), random.randint(255, 275), random.randint(130, 300), 10), fill=fillcolor,width=random.randint(1, 5))




if __name__ == "__main__":

    CAPTCHA()
    words = ''
    for i in range(4):
        word = randomChar()
        draw.text((100 * i + random.randint(10, 40), random.randint(0, 20)), word, font=font, fill=Wordcolor())
        words += word

    img = im.filter(ImageFilter.BLUR)
    # im.save("CAPTCHA.png")
    im.show()
    print(words)



