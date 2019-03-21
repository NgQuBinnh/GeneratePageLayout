import ctypes
import cv2
import numpy as np
from paramater import *
from draw_genarated_mask import draw_bbxs
from PIL import Image, ImageDraw, ImageFont


def GetTextDimensions(text, points, font):
    class SIZE(ctypes.Structure):
        _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]

    hdc = ctypes.windll.user32.GetDC(0)
    hfont = ctypes.windll.gdi32.CreateFontA(points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)

    size = SIZE(0, 0)
    ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))

    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
    ctypes.windll.gdi32.DeleteObject(hfont)

    return (size.cx, size.cy)

# print(GetTextDimensions("Hello worlds", 12, "Times New Roman"))
# print(GetTextDimensions("Hello world", 12, "Arial"))


data = open("new_input_en.txt", "r", encoding="utf8").readlines()

list_paragraph = []
para = ""
for sentence in data:
    flag = False
    for ch in sentence:
        if ch.isalpha() or ch.isdigit():
            flag = True
            break
    if flag:
        para += sentence
    else:
        if para != '':
            list_paragraph.append(para)
        para = ""

# print("???")
# for para in list_paragraph:
#     print(para)
#     print('-----')
#     print(GetTextDimensions(para, 15, "Times New Roman"))

image = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3), np.uint8)
# image = draw_bbxs(image, [(100, 5, 100 + int(ROW_RATIO * IMAGE_HEIGHT), 900)], "")
image = cv2.imread("sample.png")
font = cv2.FONT_HERSHEY_PLAIN
bottomLeftCornerOfText = (5, 100)
fontScale = 3
fontColor = (255, 255, 255)
lineType = 1
#
print(list_paragraph[2])
cv2.putText(image, list_paragraph[2],
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)

cv2.imwrite("sample.png", image)

image = Image.open('sample.png')
draw = ImageDraw.Draw(image)

(x, y) = (5, 100)
name = "hello sdjlskjd lj skdjslkjd lksj lksdjs lkjd"
color = 'rgb(255, 255, 255)' # white color
font = ImageFont.truetype('font-times-new-roman.ttf', size=13)

draw.text((x, y), name, fill=color, font=font)

image.save('image_on.png')

