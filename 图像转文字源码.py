from PIL import Image
IMG=r"C:\Users\86136\Desktop\文件\1644290967736131627water.jpg"#图片地址
WIDTH=80#照片宽度
HEIGHT=80#照片高度
ascii_char =list("$@B%8&WM#*oahkbdpqwmZ00QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\^ '. ")
#将256灰度映射到70个字符上
def get_char(r,g,b,alpha=256):#alpha透明度
    if alpha==0:
        return ''
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)#计算灰度 unit=(256.0+1)/length
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]#不同的灰度对应着不同的字符#通过灰度来区分色块
im=Image.open(IMG)
im=im.resize((WIDTH,HEIGHT))
txt=""
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt+=get_char(*im.getpixel((j,i)))
    txt+='\n'
print(txt)
    #写入文件
with open("E:\白嫖\小黑子.txt",'w') as f:
    f.write(txt)