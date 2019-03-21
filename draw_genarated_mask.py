import numpy as np
from paramater import *
from generate_text import *
from generate_block import *
import cv2
import argparse
import random
from PIL import Image, ImageDraw, ImageFont

def add_arguments(parser):
    parser.add_argument("-image_width", type=int, default=IMAGE_WIDTH)
    parser.add_argument("-image_height", type=int, default=IMAGE_HEIGHT)
    parser.add_argument("-data_dir", type=str, default=DATA_DIR)
    parser.add_argument("-out_dir", type=str, default=OUT_DIR)
    return parser

def main(arg):
    img_w = arg.image_width
    img_h = arg.image_height
    # Initilize generate blocks
    generate_block = GenerateBlock(img_w, img_h)
    generate_component = GenerateComponent()
    generate_text = GenrateText()
    blocks = generate_block.random_bbxs()
    index = 0
    for sub_block in blocks:
        index += 1

        cpn_blocks = []
        lb_blocks = []
        for block in sub_block:
            (min_x, min_y, max_x, max_y) = block
            components, labels = generate_component.layout_block(min_x, min_y, max_x, max_y)
            print("len pcn = " + str(len(components)) + " len lbs = " + str(len(labels)))

            cpn_blocks.append(components)
            lb_blocks.append(labels)

        idx = 0

        for i1, cpn1 in enumerate(cpn_blocks[idx]):
            for i2, cpn2 in enumerate(cpn_blocks[idx + 1]):
                for i3, cpn3 in enumerate(cpn_blocks[idx + 2]):
                    if len(cpn_blocks) - 1 == idx + 2:
                        bbxs = []
                        img = np.full((img_h, img_w, 3), 255, dtype=np.uint8)
                        bbxs.extend(cpn1)
                        bbxs.extend(cpn2)
                        bbxs.extend(cpn3)
                        lbs = []
                        lbs.extend(lb_blocks[idx + 0][i1])
                        lbs.extend(lb_blocks[idx + 1][i2])
                        lbs.extend(lb_blocks[idx + 2][i3])
                        img = generate_text.draw_bbxs(img, bbxs, lbs)
                        index += 1
                        cv2.imwrite(OUT_DIR + "mask" + str(index) + ".png", img)
                    else:
                        for i4, cpn4 in enumerate(cpn_blocks[idx + 3]):
                            if len(cpn_blocks) - 1 == idx + 3:
                                bbxs = []
                                # img = np.zeros((img_h, img_w, 3), np.uint8)
                                img = np.full((img_h, img_w, 3), 255, dtype=np.uint8)
                                bbxs.extend(cpn1)
                                bbxs.extend(cpn2)
                                bbxs.extend(cpn3)
                                bbxs.extend(cpn4)
                                lbs = []
                                lbs.extend(lb_blocks[idx + 0][i1])
                                lbs.extend(lb_blocks[idx + 1][i2])
                                lbs.extend(lb_blocks[idx + 2][i3])
                                lbs.extend(lb_blocks[idx + 3][i4])
                                img = generate_text.draw_bbxs(img, bbxs, lbs)
                                index += 1
                                cv2.imwrite(OUT_DIR + "mask" + str(index) + ".png", img)
                            else:
                                for i5, cpn5 in enumerate(cpn_blocks[idx + 4]):
                                    if len(cpn_blocks) - 1 == idx + 4:
                                        bbxs = []
                                        img = np.full((img_h, img_w, 3), 255, dtype=np.uint8)
                                        bbxs.extend(cpn1)
                                        bbxs.extend(cpn2)
                                        bbxs.extend(cpn3)
                                        bbxs.extend(cpn4)
                                        bbxs.extend(cpn5)
                                        lbs = []
                                        lbs.extend(lb_blocks[idx + 0][i1])
                                        lbs.extend(lb_blocks[idx + 1][i2])
                                        lbs.extend(lb_blocks[idx + 2][i3])
                                        lbs.extend(lb_blocks[idx + 3][i4])
                                        lbs.extend(lb_blocks[idx + 4][i5])
                                        img = generate_text.draw_bbxs(img, bbxs, lbs)
                                        index += 1

                                        cv2.imwrite(OUT_DIR + "mask" + str(index) + ".png", img)
                                    else:
                                        for i6, cpn6 in enumerate(cpn_blocks[idx + 5]):
                                            if len(cpn_blocks) - 1 == idx + 5:
                                                bbxs = []
                                                img = np.full((img_h, img_w, 3), 255, dtype=np.uint8)
                                                bbxs.extend(cpn1)
                                                bbxs.extend(cpn2)
                                                bbxs.extend(cpn3)
                                                bbxs.extend(cpn4)
                                                bbxs.extend(cpn5)
                                                bbxs.extend(cpn6)
                                                lbs = []
                                                lbs.extend(lb_blocks[idx + 0][i1])
                                                lbs.extend(lb_blocks[idx + 1][i2])
                                                lbs.extend(lb_blocks[idx + 2][i3])
                                                lbs.extend(lb_blocks[idx + 3][i4])
                                                lbs.extend(lb_blocks[idx + 4][i5])
                                                lbs.extend(lb_blocks[idx + 5][i6])
                                                img = generate_text.draw_bbxs(img, bbxs, lbs)
                                                index += 1

                                                cv2.imwrite(OUT_DIR + "mask" + str(index) + ".png", img)
                                            else:
                                                for i7, cpn7 in enumerate(cpn_blocks[idx + 6]):
                                                    if len(cpn_blocks) - 1 == idx + 6:
                                                        bbxs = []
                                                        img = np.full((img_h, img_w, 3), 255, dtype=np.uint8)
                                                        bbxs.extend(cpn1)
                                                        bbxs.extend(cpn2)
                                                        bbxs.extend(cpn3)
                                                        bbxs.extend(cpn4)
                                                        bbxs.extend(cpn5)
                                                        bbxs.extend(cpn6)
                                                        bbxs.extend(cpn7)
                                                        lbs = []
                                                        lbs.extend(lb_blocks[idx + 0][i1])
                                                        lbs.extend(lb_blocks[idx + 1][i2])
                                                        lbs.extend(lb_blocks[idx + 2][i3])
                                                        lbs.extend(lb_blocks[idx + 3][i4])
                                                        lbs.extend(lb_blocks[idx + 4][i5])
                                                        lbs.extend(lb_blocks[idx + 5][i6])
                                                        lbs.extend(lb_blocks[idx + 6][i7])
                                                        img = generate_text.draw_bbxs(img, bbxs, lbs)
                                                        index += 1

                                                        cv2.imwrite(OUT_DIR + "mask" + str(index) + ".png", img)
                                                    else:
                                                        for i8, cpn8 in enumerate(cpn_blocks[idx + 7]):
                                                            if len(cpn_blocks) - 1 == idx + 7:
                                                                bbxs = []
                                                                img = np.full((img_h, img_w, 3), 255, dtype=np.uint8)
                                                                bbxs.extend(cpn1)
                                                                bbxs.extend(cpn2)
                                                                bbxs.extend(cpn3)
                                                                bbxs.extend(cpn4)
                                                                bbxs.extend(cpn5)
                                                                bbxs.extend(cpn6)
                                                                bbxs.extend(cpn7)
                                                                bbxs.extend(cpn8)
                                                                lbs = []
                                                                lbs.extend(lb_blocks[idx + 0][i1])
                                                                lbs.extend(lb_blocks[idx + 1][i2])
                                                                lbs.extend(lb_blocks[idx + 2][i3])
                                                                lbs.extend(lb_blocks[idx + 3][i4])
                                                                lbs.extend(lb_blocks[idx + 4][i5])
                                                                lbs.extend(lb_blocks[idx + 5][i6])
                                                                lbs.extend(lb_blocks[idx + 6][i7])
                                                                lbs.extend(lb_blocks[idx + 7][i8])
                                                                img = generate_text.draw_bbxs(img, bbxs, lbs)
                                                                index += 1

                                                                cv2.imwrite(OUT_DIR + "mask" + str(index) + ".png",
                                                                            img)
                                                            else:
                                                                for i9, cpn9 in enumerate(cpn_blocks[idx + 8]):
                                                                    if len(cpn_blocks) - 1 == idx + 8:
                                                                        bbxs = []
                                                                        img = np.full((img_h, img_w, 3), 255,
                                                                                      dtype=np.uint8)
                                                                        bbxs.extend(cpn1)
                                                                        bbxs.extend(cpn2)
                                                                        bbxs.extend(cpn3)
                                                                        bbxs.extend(cpn4)
                                                                        bbxs.extend(cpn5)
                                                                        bbxs.extend(cpn6)
                                                                        bbxs.extend(cpn7)
                                                                        bbxs.extend(cpn8)
                                                                        bbxs.extend(cpn9)
                                                                        lbs = []
                                                                        lbs.extend(lb_blocks[idx + 0][i1])
                                                                        lbs.extend(lb_blocks[idx + 1][i2])
                                                                        lbs.extend(lb_blocks[idx + 2][i3])
                                                                        lbs.extend(lb_blocks[idx + 3][i4])
                                                                        lbs.extend(lb_blocks[idx + 4][i5])
                                                                        lbs.extend(lb_blocks[idx + 5][i6])
                                                                        lbs.extend(lb_blocks[idx + 6][i7])
                                                                        lbs.extend(lb_blocks[idx + 7][i8])
                                                                        lbs.extend(lb_blocks[idx + 8][i9])
                                                                        img = generate_text.draw_bbxs(img, bbxs, lbs)
                                                                        index += 1

                                                                        cv2.imwrite(
                                                                            OUT_DIR + "mask" + str(index) + ".png",
                                                                            img)

    # cv2.imwrite(OUT_DIR + "mask" + ".png", img)
    print(img_w, img_h)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = add_arguments(parser)

    args = parser.parse_args()
    print(args)

    main(args)

# font = cv2.FONT_HERSHEY_PLAIN
# bottomLeftCornerOfText = (500, 100)
# fontScale = 2
# fontColor = (255, 255, 255)
# lineType = 1
#
# cv2.putText(img, 'Hello World!',
#             bottomLeftCornerOfText,
#             font,
#             fontScale,
#             fontColor,
#             lineType)





