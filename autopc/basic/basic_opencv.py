# @Time: 2024年10月03日 03:04
# @Author: orcakill
# @File: opencv.py
# @Description: opencv相关算法api
import cv2
import imageio
import numpy as np


class BasicOpenCv:

    @staticmethod
    def draw_rectangle(screen, x1: int, y1: int, x2: int, y2: int, img_path: str):
        """
        画图，根据指定范围的坐标在原图上画框，并打印到指定地址

        :param screen: 图像ndarray
        :param x1: 图片左上角横坐标
        :param y1: 图片左上角纵坐标
        :param x2: 图片右下角横坐标
        :param y2: 图片右下角纵坐标
        :param img_path: 图片路径
        :return: None
        """

        cv2.rectangle(screen, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # 保存图片到本地磁盘
        imageio.imsave(img_path, screen)

    @staticmethod
    def draw_point(screen, pos, img_path: str):
        """
        画图，根据指定范围的坐标在原图上画框，并打印到指定地址

        :param screen: 图像 ndarray
        :param pos: (横坐标,纵坐标）
        :param img_path: 图片路径
        :return: None
        """
        rgb_image = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        print(pos)
        cv2.circle(rgb_image, pos, 5, (255, 0, 0), -1)
        # 保存图片到本地磁盘
        imageio.imsave(img_path, rgb_image)

    @staticmethod
    def get_color_format(screen):
        """
        判断数组的颜色空间格式

        :param screen: 图像数组 ndarray
        :return: str
        """

        r_mean = np.mean(screen[:, :, 0])
        g_mean = np.mean(screen[:, :, 1])
        b_mean = np.mean(screen[:, :, 2])

        if r_mean > g_mean and r_mean > b_mean:
            return 'RGB'
        elif b_mean > r_mean and b_mean > g_mean:
            return 'BGR'
        else:
            # 可能需要更复杂的判断逻辑或者无法确定
            return False
