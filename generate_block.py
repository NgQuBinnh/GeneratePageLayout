from paramater import *


class GenerateBlock():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.std_row = ROW_RATIO * self.height
        self.std_col = COL_RATIO * self.width
        self.max_row = int(self.height / self.std_row)
        self.min_x_rows = []

        min_x = MG_BLOCK_EDGE
        for i in range(self.max_row):
            self.min_x_rows.append(min_x)
            min_x += self.std_row + MG_BLOCK_BLOCK

        # print(len(self.min_x_rows))

    def left_column(self):
        result_blocks = []
        size_columns = 3
        min_y = int(self.width - size_columns * self.std_col - MG_BLOCK_EDGE)
        max_y = int(self.width - MG_BLOCK_EDGE)

        col_current = int(self.width - 3 * self.std_col)
        fixed_col = (MG_BLOCK_EDGE, col_current, self.height - 1 - MG_BLOCK_EDGE, self.width - 1 - MG_BLOCK_EDGE)
        sub_block_area = self.just_row_subarea(MG_BLOCK_EDGE, MG_BLOCK_EDGE, self.height - 1, col_current)
        for idx, subblock in enumerate(sub_block_area):
            sub_block_area[idx].append(fixed_col)
        result_blocks.extend(sub_block_area)

        # One column moving on left side

        for up_row in range(self.max_row - 1):
            for down_row in range(up_row + 3, self.max_row, 1):
                min_x = int(self.min_x_rows[up_row])
                max_x = int(self.min_x_rows[down_row] + self.std_row)
                # print("minx = " + str(min_x) + "   " + "maxx = " + str(max_x))
                fixed_col = (min_x, min_y, max_x, max_y)

                sub_row_block_area = self.just_row_subarea(min_x - MG_BLOCK_BLOCK, 0,
                                                           max_x, min_y - 1)

                sub_row_block_area_1 = self.just_row_subarea(0, 0,
                                                             min_x - 1, self.width - 1)
                sub_row_block_area_2 = self.just_row_subarea(max_x, 0,
                                                             self.height - 1, self.width - 1)

                for idx, sub_block in enumerate(sub_row_block_area):
                    sub_row_block_area[idx].append(fixed_col)

                for area_1 in sub_row_block_area:
                    for area_2 in sub_row_block_area_1:
                        for area_3 in sub_row_block_area_2:
                            page = []
                            page.extend(area_1)
                            page.extend(area_2)
                            page.extend(area_3)
                            result_blocks.append(page)
                # result_blocks.extend(sub_row_block_area)

        return result_blocks

    def right_column(self):
        result_blocks = []
        size_columns = 3
        max_y = int(size_columns * self.std_col)
        min_y = int(MG_BLOCK_EDGE)

        col_current = int(size_columns * self.std_col)
        fixed_col = (MG_BLOCK_EDGE, MG_BLOCK_EDGE, self.height - 1 - MG_BLOCK_EDGE, col_current)
        sub_block_area = self.just_row_subarea(MG_BLOCK_EDGE, col_current, self.height - 1, self.width - 1)
        for idx, subblock in enumerate(sub_block_area):
            sub_block_area[idx].append(fixed_col)
        result_blocks.extend(sub_block_area)

        # One column moving on left side

        for up_row in range(self.max_row - 1):
            for down_row in range(up_row + 3, self.max_row, 1):
                min_x = int(self.min_x_rows[up_row])
                max_x = int(self.min_x_rows[down_row] + self.std_row)
                # print("minx = " + str(min_x) + "   " + "maxx = " + str(max_x))
                fixed_col = (min_x, min_y, max_x, max_y)

                sub_row_block_area = self.just_row_subarea(min_x - MG_BLOCK_BLOCK, max_y,
                                                           max_x, self.width - 1)

                sub_row_block_area_1 = self.just_row_subarea(0, 0,
                                                             min_x - 1, self.width - 1)
                sub_row_block_area_2 = self.just_row_subarea(max_x, 0,
                                                             self.height - 1, self.width - 1)

                for idx, sub_block in enumerate(sub_row_block_area):
                    sub_row_block_area[idx].append(fixed_col)

                for area_1 in sub_row_block_area:
                    for area_2 in sub_row_block_area_1:
                        for area_3 in sub_row_block_area_2:
                            page = []
                            page.extend(area_1)
                            page.extend(area_2)
                            page.extend(area_3)
                            result_blocks.append(page)
                # result_blocks.extend(sub_row_block_area)

        return result_blocks

    def just_row_subarea(self, minx, miny, maxx, maxy):
        if maxx - minx < self.std_row or maxy - miny < self.std_col:
            return []
        sub_blocks = []
        height_area = maxx - minx + 1
        mg_block = MG_BLOCK_BLOCK

        max_row = int((height_area - mg_block * int(height_area / self.std_row)) / self.std_row)
        # print(max_row)
        for r2 in range(0, int(max_row / 2) + 1, 1):
            for r3 in range(0, int(max_row / 3) + 1, 1):
                for r4 in range(0, int(max_row / 4) + 1, 1):
                    if max_row - 1 <= r2 * 2 + r3 * 3 + r4 * 4 <= max_row:

                        max_col_current = maxy - mg_block
                        min_col_current = int(miny + mg_block)
                        # mg_block = int((height_area - (r2 * 2 * self.std_row + r3 * 3 * self.std_row +
                        #                                self.std_row * r4 * 4)) / (r2 + r3 + r4 + 1))
                        # print("mg = " + str(mg_block))
                        min_row_current = int(minx + mg_block)

                        tmp_block = []
                        for i in range(r2):
                            max_row_current = min_row_current + int(2 * self.std_row - 1)
                            tmp_block.append((min_row_current, min_col_current, max_row_current, max_col_current))
                            min_row_current = max_row_current + mg_block

                        for i in range(r4):
                            max_row_current = min_row_current + int(4 * self.std_row - 1)
                            tmp_block.append((min_row_current, min_col_current, max_row_current, max_col_current))
                            min_row_current = max_row_current + mg_block

                        for i in range(r3):
                            max_row_current = min_row_current + int(3 * self.std_row - 1)
                            tmp_block.append((min_row_current, min_col_current, max_row_current, max_col_current))
                            min_row_current = max_row_current + mg_block

                        sub_blocks.append(tmp_block)

                        mg_block = MG_BLOCK_BLOCK
        return sub_blocks

    def rows_midle_rows(self, minx, miny, maxx, maxy):
        result_blocks = []
        mid_width = int((miny + maxy) / 2)
        lef_area = self.just_row_subarea(minx, miny, maxx, mid_width - 1)
        rig_area = self.just_row_subarea(minx, mid_width + 1, maxx, maxy)
        for area_1 in lef_area:
            for area_2 in rig_area:
                page = []
                page.extend(area_1)
                page.extend(area_2)
                result_blocks.append(page)
        return result_blocks

    def random_bbxs(self):
        blocks = []
        # for cor in range(0, self.height - 200, int(self.height * ROW_RATIO) + 1 ):
        #     block.append((cor + 7, 100, cor + int(self.height * ROW_RATIO), 200))

        # for r2 in range(0, 6, 1):
        #     for r3 in range(0, 4, 1):
        #         for r4 in range(0, 3, 1):
        #             if 7 <= r2 * 2 + r3 * 3 + r4 * 4 <= 10:
        #                 print(str(r2) + " " + str(r3) + " " + str(r4))
        #                 blocks.append(self.one_left_column(r2, r3, r4))

        left_cols_area = self.left_column()
        just_rows_area = self.just_row_subarea(0, 0, self.height - 1, self.width - 1)
        row_mid_row = self.rows_midle_rows(0, 0, self.height - 1, self.width - 1)
        right_cols_area = self.right_column()
        blocks.extend(just_rows_area)
        blocks.extend(left_cols_area)
        blocks.extend(row_mid_row)
        blocks.extend(right_cols_area)
        return blocks

import random


class GenerateComponent:

    def __init__(self):
        self.std_row = ROW_RATIO_CPN * IMAGE_HEIGHT
        pass

    def row_subarea(self, minx, miny, maxx, maxy, is_col_area=False):
        # if maxx - minx < self.std_row or maxy - miny < self.std_col:
        #     return []
        sub_blocks = []
        lb_blocks = []
        height_area = maxx - minx + 1
        mg_block = MG_BLOCK_BLOCK

        max_row = int((height_area - mg_block * int(height_area / self.std_row)) / self.std_row)
        # max_row = int(height_area / self.std_row)
        # print(max_row)
        for r2 in range(0, int(max_row / 2) + 1, 1):
            for r3 in range(0, int(max_row / 3) + 1, 1):
                for r4 in range(0, int(max_row / 4) + 1, 1):
                    if max_row - 1 <= r2 * 2 + r3 * 3 + r4 * 4 <= max_row:

                        max_col_current = maxy - mg_block
                        min_col_current = int(miny + mg_block)
                        # mg_block = int((height_area - (r2 * 2 * self.std_row + r3 * 3 * self.std_row +
                        #                                self.std_row * r4 * 4)) / (r2 + r3 + r4 + 1))
                        # print("mg = " + str(mg_block))
                        min_row_current = int(minx + mg_block)

                        tmp_block = []
                        lb_block = []
                        for i in range(r2):
                            max_row_current = min_row_current + int(2 * self.std_row - 1)
                            tmp_block.append((min_row_current, min_col_current, max_row_current, max_col_current))
                            rd = random.randint(0, 3)
                            if rd % 2 == 0:
                                lb_block.append("title-parag")
                            else:
                                lb_block.append("parag")

                            min_row_current = max_row_current + mg_block

                        for i in range(r4):
                            max_row_current = min_row_current + int(4 * self.std_row - 1)
                            tmp_block.append((min_row_current, min_col_current, max_row_current, max_col_current))

                            rd = random.randint(0, 50)
                            if rd % 3 == 0:
                                if not is_col_area:
                                    lb_block.append("table")
                                else:
                                    lb_block.append("title-parag")
                            else:
                                if rd % 3 == 1:
                                    lb_block.append("parag")
                                else:
                                    lb_block.append("figure")

                            min_row_current = max_row_current + mg_block

                        for i in range(r3):
                            max_row_current = min_row_current + int(3 * self.std_row - 1)
                            tmp_block.append((min_row_current, min_col_current, max_row_current, max_col_current))

                            rd = random.randint(0, 55)
                            if rd % 3 == 0:
                                if not is_col_area:
                                    lb_block.append("table")
                                else:
                                    lb_block.append("title-parag")
                            else:
                                if rd % 3 == 1:
                                    lb_block.append("parag")
                                else:
                                    lb_block.append("figure")

                            min_row_current = max_row_current + mg_block

                        sub_blocks.append(tmp_block)
                        lb_blocks.append(lb_block)

                        mg_block = MG_BLOCK_BLOCK
        return sub_blocks, lb_blocks

    def title_paragraph(self, minx, miny, maxx, maxy):
        cpns = []
        lbs = []

        minx += MG_BLOCK_TEXT
        miny += MG_BLOCK_TEXT
        maxx -= MG_BLOCK_TEXT
        maxy -= MG_BLOCK_TEXT

        pro = random.randint(40, 70)
        up_t, le_t, dow_t, ri_t = minx, miny, minx + FONT_TITLE, miny + int((maxy - miny) * (pro / 100))
        up_p, left_p, down_p, right_p = dow_t + MG_TEXT_TEXT, le_t, maxx, maxy

        cpn = [(up_t, le_t, dow_t, ri_t), (up_p, left_p, down_p, right_p)]
        cpns.append(cpn)

        lb = ["title", "parag"]
        lbs.append(lb)

        cpn = [(minx, miny, maxx, maxy)]
        cpns.append(cpn)

        lb = ["parag"]
        lbs.append(lb)

        return cpn, lbs

    def layout_block(self, minx, miny, maxx, maxy):
        cpns = []
        lbs = []
        if maxy - miny < IMAGE_WIDTH * COL_RATIO * 3.5:
            print("this is column")
            cpn, lb = self.row_subarea(minx, miny, maxx, maxy, is_col_area=True)
            cpns.extend(cpn)
            lbs.extend(lb)
        else:
            type_row = int((maxx - minx) / (ROW_RATIO * IMAGE_HEIGHT))
            if type_row >= 2:
                cpn, lb = self.row_subarea(minx, miny, maxx, maxy)
                cpns.extend(cpn)
                lbs.extend(lb)

            if type_row == 3:
                print("R3")
                if maxy - miny > IMAGE_WIDTH / 2:
                    cpn1, lb1 = self.row_subarea(minx, miny, maxx, miny + int((maxy - miny) / 2))
                    cpn2, lb2 = self.row_subarea(minx, miny + int((maxy - miny) / 2) + MG_BLOCK_TEXT, maxx, maxy)
                    for i in range(len(cpn1)):
                        for j in range(len(cpn2)):
                            sum_cpn = []
                            sum_cpn.extend(cpn1[i])
                            sum_cpn.extend(cpn2[j])

                            sum_lb = []
                            sum_lb.extend(lb1[i])
                            sum_lb.extend(lb2[j])

                            cpns.append(sum_cpn)
                            lbs.append(sum_lb)
                else:
                    cpn = [(minx, miny, maxx, maxy)]
                    ro = random.randint(0, 59)
                    if ro % 4 == 2 or ro % 4 == 3:
                        lb = ["table"]
                        cpns.append(cpn)
                        lbs.append(lb)
                    if ro % 4 == 1:
                        lb = ["figure"]
                        cpns.append(cpn)
                        lbs.append(lb)
                    if ro % 4 == 0:
                        lb = ["title-parag"]
                        cpns.append(cpn)
                        lbs.append(lb)
            else:
                if type_row == 4:
                    print("R4")
                    # Split column
                    if maxy - miny > IMAGE_WIDTH / 2:
                        cpn1, lb1 = self.row_subarea(minx, miny, maxx, miny + int((maxy - miny) / 2))
                        cpn2, lb2 = self.row_subarea(minx, miny + int((maxy - miny) / 2) + MG_BLOCK_TEXT, maxx, maxy)
                        for i in range(len(cpn1)):
                            for j in range(len(cpn2)):
                                sum_cpn = []
                                sum_cpn.extend(cpn1[i])
                                sum_cpn.extend(cpn2[j])

                                sum_lb = []
                                sum_lb.extend(lb1[i])
                                sum_lb.extend(lb2[j])

                                cpns.append(sum_cpn)
                                lbs.append(sum_lb)
                    else:
                        cpn = [(minx, miny, maxx, maxy)]
                        ro = random.randint(0,59)
                        if ro % 3 == 0:
                            lb = ["table"]
                            cpns.append(cpn)
                            lbs.append(lb)
                        if ro % 3 == 1:
                            lb = ["figure"]
                            cpns.append(cpn)
                            lbs.append(lb)
                        if ro % 3 == 0:
                            lb = ["title-parag"]
                            cpns.append(cpn)
                            lbs.append(lb)
                else:
                    if type_row == 2:
                        cpn = [(minx, miny, maxx, maxy)]
                        lb = ["title-parag"]
                        cpns.append(cpn)
                        lbs.append(lb)

        return cpns, lbs











