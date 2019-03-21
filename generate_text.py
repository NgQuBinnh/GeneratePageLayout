from PIL import Image, ImageDraw, ImageFont
import cv2
import random
from paramater import *
import os

class GenrateText():
    def __init__(self):
        data = open("new_input_en.txt", "r", encoding="utf8").readlines()

        self.list_paragraph = []
        para = ""
        for sentence in data:
            flag = False
            for ch in sentence:
                if ch.isalpha() or ch.isdigit():
                    flag = True
                    break
            if flag:
                para += sentence.replace("\n", " ")
            else:
                if para != '':
                    self.list_paragraph.append(para)
                para = ""
        self.list_table = []
        self.list_figure = []

        for file in os.listdir(DIR_TABLE_FIGURE):
            img = cv2.imread(DIR_TABLE_FIGURE + file)

            if file.split('_')[0] == 'table':
                self.list_table.append(img)
            else:
                self.list_figure.append(img)

    def fill_parag(self, minx, miny, maxx, maxy, img):
        miny += MG_BLOCK_TEXT
        minx += MG_BLOCK_TEXT
        cv2.imwrite('sample.png', img)

        image = Image.open('sample.png')
        draw = ImageDraw.Draw(image)

        (x, y) = (miny, minx)
        id_para = random.randint(0, len(self.list_paragraph) - 10)
        parag = self.list_paragraph[id_para] + self.list_paragraph[id_para + 1] + self.list_paragraph[id_para + 2] + \
                self.list_paragraph[id_para + 3] +  self.list_paragraph[id_para + 4]
        parag = parag.split(' ')
        max_line = int((maxx - minx) / (FONT_NORMAL + MG_TEXT_TEXT))
        nb_line = 0
        index_word = 0
        text = ""

        while nb_line <= max_line:
            line = ""
            max_range_line = int((maxy - miny) * (random.randint(70, 93) / 100))
            while True:
                if len(parag[index_word]) > 7:
                    index_word += 1

                if index_word == len(parag) - 1:
                    index_word = 0

                line += parag[index_word] + " "
                if int(len(line) * PX_PER_CHAR > max_range_line):
                    line = line[0:max_range_line]
                    index_word += 1
                    break
                if index_word == len(parag) - 1:
                    index_word = 0
                if int(len(line + parag[index_word + 1]) * PX_PER_CHAR) > max_range_line:
                    line += parag[index_word + 1]
                    line = line[0:max_range_line]
                    break
                index_word += 1

            nb_line += 1

            text += line + "\n"
        # text = "helllo djslkdjl ksj"
        color = 'rgb(0 ,0 ,0)'  # black color
        font = ImageFont.truetype('font-times-new-roman.ttf', size=FONT_NORMAL)

        draw.text((x, y), text, fill=color, font=font)

        image.save('sample.png')

        result = cv2.imread("sample.png")
        return result

    def fill_title_parag(self, minx, miny, maxx, maxy, img):
        miny += MG_BLOCK_TEXT
        minx += MG_BLOCK_TEXT
        cv2.imwrite('sample.png', img)

        image = Image.open('sample.png')
        draw = ImageDraw.Draw(image)

        id_para = random.randint(0, len(self.list_paragraph))
        parag = self.list_paragraph[id_para] + self.list_paragraph[id_para + 1] + self.list_paragraph[id_para + 2] + \
                self.list_paragraph[id_para + 3] + self.list_paragraph[id_para + 4]
        parag = parag.split(' ')
        max_line = int((maxx - minx) / (FONT_NORMAL + MG_TEXT_TEXT))
        nb_line = 0
        index_word = 0
        text = ""

        title = parag[0] + parag[1] + parag[2] + parag[3]
        title = title[:15]
        max_line -= 1
        while nb_line <= max_line:
            line = ""
            max_range_line = int((maxy - miny) * (random.randint(70, 94) / 100))
            while True:
                if len(parag[index_word]) > 7:
                    index_word += 1
                line += parag[index_word] + " "
                if index_word == len(parag) - 1:
                    index_word = 0
                if int(len(line + parag[index_word + 1]) * PX_PER_CHAR) > max_range_line:
                    line += parag[index_word + 1]
                    line = line[0:max_range_line]
                    break
                index_word += 1

            nb_line += 1
            text += line + "\n"
        # text = "helllo djslkdjl ksj"
        color = 'rgb(0 ,0 ,0)'  # black color
        (x, y) = (miny, minx)
        font = ImageFont.truetype('font-times-new-roman.ttf', size=FONT_TITLE)
        draw.text((x, y), title, fill=color, font=font)
        (x, y) = (miny, minx + FONT_TITLE + MG_TEXT_TEXT)
        font = ImageFont.truetype('font-times-new-roman.ttf', size=FONT_NORMAL)
        draw.text((x, y), text, fill=color, font=font)

        image.save('sample.png')

        result = cv2.imread("sample.png")
        return result

    def fill_table(self, minx, miny, maxx, maxy, img):
        total_area = (maxx - minx + 1) * (maxy - miny + 1)
        indices = []
        for idx, table in enumerate(self.list_table):
            if table.shape[0] < (maxx - minx) and table.shape[1] < (maxy - miny) and (table.shape[0] * table.shape[1]) > (total_area / 3):
                indices.append(idx)
        rd_index = random.randint(0, (len(indices) - 1))
        print("Len indicie = " + str(len(indices)) + " rd_index = " + str(rd_index))
        small_img = self.list_table[indices[rd_index]]
        x_offset = int(minx + (maxx - minx + 1 - small_img.shape[0]) / 2)
        y_offset = int(miny + (maxy - miny + 1 - small_img.shape[1]) / 2)

        img[x_offset:x_offset + small_img.shape[0], y_offset:y_offset + small_img.shape[1]] = small_img

        return img

    def fill_figure(self, minx, miny, maxx, maxy, img):
        total_area = (maxx - minx + 1) * (maxy - miny + 1)
        indices = []
        for idx, figure in enumerate(self.list_figure):
            if figure.shape[0] < (maxx - minx) and figure.shape[1] < (maxy - miny) and (
                    figure.shape[0] * figure.shape[1]) > (total_area / 3):
                indices.append(idx)

        rd_index = random.randint(0, (len(indices) - 1))
        small_img = self.list_figure[indices[rd_index]]
        x_offset = int(minx + (maxx - minx + 1 - small_img.shape[0]) / 2)
        y_offset = int(miny + (maxy - miny + 1 - small_img.shape[1]) / 2)

        img[x_offset:x_offset + small_img.shape[0], y_offset:y_offset + small_img.shape[1]] = small_img

        return img

    def draw_bbxs(self, image, bbxs, lbs):
        print("len bbxs = " + str(len(bbxs)) + " len lbs = " + str(len(lbs)))
        for idx, bbx in enumerate(bbxs):
            (min_x, min_y, max_x, max_y) = bbx
            label = lbs[idx]
            if label == "parag":
                image = self.fill_parag(min_x, min_y, max_x, max_y, image)
            if label == "title-parag":
                image = self.fill_title_parag(min_x, min_y, max_x, max_y, image)

            if label == "table":
                image = self.fill_table(min_x, min_y, max_x, max_y, image)

            if label == "figure":
                image = self.fill_figure(min_x, min_y, max_x, max_y, image)

            # G = random.randint(0, 100)
            # R = random.randint(0, 150)
            # image = cv2.rectangle(image, (min_y, min_x), (max_y, max_x), (10, 52, 255), 2)
            # COLOR_BLOCK = (R, G, 120)
            # for x in range(min_x, max_x + 1, 1):
            #     for y in range(min_y, max_y + 1, 1):
            #         image[x][y] = COLOR_BLOCK
        return image


gen = GenrateText()