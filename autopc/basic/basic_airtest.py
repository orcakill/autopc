# @Time: 2024年10月01日 03:23
# @Author: orcakill
# @File: airtest.py
# @Description: airtest相关的api接口
import logging
import random

from airtest import aircv
from airtest.aircv import cv2_2_pil
from airtest.core.android import Android
from airtest.core.android.cap_methods.screen_proxy import ScreenProxy
from airtest.core.api import *
from airtest.core.helper import G
from airtest.core.settings import Settings

#  控制airtest的日志输出
log_airtest = logging.getLogger("airtest")
log_airtest.setLevel(logging.CRITICAL)
# ·图片点击识别等待时间(秒）·
WAIT_TIME = 0
# 图像识别阈值
THRESHOLD = 0.7
#  长按时间
DURATION = 0.1


class BasicAirtest:
    """
    airtest的基础api
    """

    @staticmethod
    def auto_setup(connect_name: str, device_type: str = 'Android', ip: str = '127.0.0.1:5037', hwnd: str = '',
                   title: str = ''):
        """
        设备连接，支持Android和Windows，默认使用Android连接

        :param connect_name: 连接名称
        :param device_type: 设备类型
        :param ip: IP和端口（Android连接）
        :param hwnd: 句柄（windows连接）
        :param title: 窗口标题（windows连接）
        :return: None
        """
        devices = ''
        if device_type == 'Android':
            devices = 'Android://' + ip + '/' + connect_name
        elif device_type == 'Windows':
            devices = "Windows:///"
            if hwnd is not None:
                devices = devices + hwnd
            elif title is not None:
                devices = devices + '?title_re=' + title + '.*'
        auto_setup(__file__, logdir=False, devices=[devices])

    @staticmethod
    def snapshot(img_path: str = ''):
        """
        设备截图函数，打印或不打印图片到指定路径

        :param img_path: 图片路径及名称（打印）
        :return: ndarray
        """
        if img_path:
            screen = snapshot(img_path, quality=99)
        else:
            screen = G.DEVICE.snapshot(quality=99)
        return screen

    @staticmethod
    def loop_find(template: Template, timeout=ST.FIND_TIMEOUT, threshold=None, interval=0.5, intervalfunc=None,
                  random_area=0):
        """
        判断模板图片在设备上是否存在，如果存在返回坐标

        :param template: 图片类
        :param timeout:  超时时间
        :param threshold: 相似度
        :param interval:  识别间隔
        :param intervalfunc:
        :param random_area: 随机区域，默认0，取中心点，大于零小于等于1则区域内随机
        :return:
        """
        G.LOGGING.info("Try finding: %s", template)
        start_time = time.time()
        while True:
            screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)

            if screen is None:
                G.LOGGING.warning("Screen is None, may be locked")
            else:
                if threshold:
                    template.threshold = threshold
                if 0 < random_area <= 1:
                    # 获取区域信息
                    match_rectangle = template._cv_match(screen).get("rectangle")
                    # 区域坐标
                    x1, y1 = match_rectangle[0]
                    x2, y2 = match_rectangle[1]
                    x3, y3 = match_rectangle[2]
                    x4, y4 = match_rectangle[3]
                    # 计算长方形的宽度和高度
                    width = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
                    height = max(y1, y2, y3, y4) - min(y1, y2, y3, y4)
                    # 处理随机区域
                    if random_area < 1:
                        x1, y1 = x1 + random_area * width / 2, y1 + random_area * height / 2
                        x2, y2 = x2 + random_area * width / 2, y2 - random_area * height / 2
                        x3, y3 = x3 - random_area * width / 2, y3 - random_area * height / 2
                        x4, y4 = x4 - random_area * width / 2, y4 + random_area * height / 2
                    random_x = int(random.uniform(min(x1, x2, x3, x4), max(x1, x2, x3, x4)))
                    random_y = int(random.uniform(min(y1, y2, y3, y4), max(y1, y2, y3, y4)))
                    match_pos = (random_x, random_y)
                else:
                    # 其他情况，取中心点
                    match_pos = template.match_in(screen)
                if match_pos:
                    try_log_screen(screen)
                    return match_pos

            if intervalfunc is not None:
                intervalfunc()

            # 超时则raise，未超时则进行下次循环:
            if (time.time() - start_time) > timeout:
                try_log_screen(screen)
                raise TargetNotFoundError('Picture %s not found in screen' % template)
            else:
                time.sleep(interval)

    @staticmethod
    def exists(template: Template, cvstrategy: [], timeout: float, random_area=0):
        """
        判断模板图片在设备上是否存在，如果存在返回坐标

        :param template: 图片类
        :param cvstrategy: 图像识别算法
        :param timeout: 超时时间
        :param random_area: 随机区域，默认0，取中心点，大于零小于等于1则区域内随机
        :return: bool
        """
        Settings.CVSTRATEGY = cvstrategy
        Settings.FIND_TIMEOUT_TMP = timeout
        try:
            pos = BasicAirtest.loop_find(template, timeout=ST.FIND_TIMEOUT_TMP, random_area=random_area)
        except TargetNotFoundError:
            return False
        else:
            return pos

    @staticmethod
    def touch(template: Template, cvstrategy: [], timeout: float, times: int = 1, **kwargs):
        """
        判断模板图片在设备上是否存在，如果存在点击
        :param times: 点击次数
        :param template: 图片类
        :param cvstrategy: 图像识别算法
        :param timeout: 超时时间
        :return: bool

        """
        Settings.CVSTRATEGY = cvstrategy
        Settings.FIND_TIMEOUT = timeout
        if isinstance(template, Template):
            pos = loop_find(template, timeout=ST.FIND_TIMEOUT)
        else:
            try_log_screen()
            pos = template
        for _ in range(times):
            # If pos is a relative coordinate, return the converted click coordinates.
            # iOS may all use vertical screen coordinates, so coordinates will not be returned.
            pos = G.DEVICE.touch(pos, **kwargs) or pos
            time.sleep(0.05)
        delay_after_operation()
        return pos

    @staticmethod
    def touch_coordinate(v: [], duration: float = DURATION, wait_time: float = WAIT_TIME):
        """
        点击坐标

        :param duration: 按住时间
        :param v: 坐标
        :param wait_time: 等待开始时间
        :return: bool
        """
        time.sleep(wait_time)
        if touch(v, duration=duration):
            return True
        else:
            return False

    @staticmethod
    def adb_stop_app(package: str):
        """
        停止APP

        :param package: app的包名
        :return: 无
        """
        stop_app(package=package)

    @staticmethod
    def adb_start_app(package: str):
        """
        启动APP

        :param package: app的包名
        :return: 无
        """
        start_app(package=package)

    @staticmethod
    def adb_restart_app(package: str):
        """
        重启APP

        :param package: app的包名
        :return: 无
        """
        BasicAirtest.adb_stop_app(package)
        time.sleep(2)
        BasicAirtest.adb_start_app(package)
        time.sleep(2)

    @staticmethod
    def swipe(v1: [], v2: [], duration):
        """
        滑动
        :param duration: 间隔
        :param v1: 坐标1
        :param v2: 坐标2
        :return: bool
        """
        if swipe(v1, v2, duration=duration):
            return True
        else:
            return False

    @staticmethod
    def crop_image(x1, y1, x2, y2):
        """
        局部截图

        :param x1: x1
        :param y1: y1
        :param x2: x2
        :param y2: y2
        :return: ndarray
        """
        screen = G.DEVICE.snapshot()
        # 局部截图
        local_screen = aircv.crop_image(screen, (x1, y1, x2, y2))
        return local_screen

    @staticmethod
    def resolution_ratio():
        """
        获取当前设备分辨率

        :return: Tuple
        """
        if G.DEVICE.display_info['orientation'] in [1, 3]:
            height = G.DEVICE.display_info['width']
            width = G.DEVICE.display_info['height']
        else:
            height = G.DEVICE.display_info['height']
            width = G.DEVICE.display_info['width']
        return width, height

    @staticmethod
    def cvt_color(screen):
        """
        颜色空间转换 BGR->RGB

        :param screen: 图片
        :return: ndarray
        """
        return cv2_2_pil(screen)

    @staticmethod
    def find_all(template: Template, cvstrategy: [], timeout: float):
        """
        在设备屏幕上查找所有出现的目标并返回它们的坐标

        :param template: template对象
        :param timeout: 超时时间
        :param cvstrategy:  图像识别算法
        :return: [{'result': (x, y),'rectangle': ( (left_top, left_bottom, right_bottom, right_top) ),'confidence': 0.9},...]
        """
        Settings.CVSTRATEGY = cvstrategy
        Settings.FIND_TIMEOUT = timeout
        result = find_all(template)
        return result

    @staticmethod
    def cv_match(template: Template, screen, cvstrategy: []):
        """
        图片中图片查找

        :param template: 图片1 template格式
        :param screen: 图片2 ndarray格式
        :param cvstrategy: 图像识别算法
        :return: [{'result': (x, y),'rectangle': ( (left_top, left_bottom, right_bottom, right_top) ),'confidence': 0.9},...]
        """
        Settings.CVSTRATEGY = cvstrategy
        return template._cv_match(screen)

    @staticmethod
    def match_in(template: Template, screen, cvstrategy: [], timeout: float):
        """
        判断图片是否存在并返回坐标

        :param screen:   局部截图
        :param template: 图片类
        :param cvstrategy: 图像识别算法
        :param timeout: 超时时间
        :return: (x,y)
        """
        Settings.CVSTRATEGY = cvstrategy
        Settings.FIND_TIMEOUT_TMP = timeout
        return template.match_in(screen)

    @staticmethod
    def text(word: str):
        """
        输入文字

        :param word: 文字内容
        :return: None
        """
        text1 = "input text '" + word + "'"
        shell(text1)

    @staticmethod
    def get_cap_method(serialno):
        """
        获取截图方法

        :param serialno: 安卓设备序列号
        :return: str
        """
        dev = Android(serialno=serialno)
        screen_proxy = ScreenProxy.auto_setup(dev.adb, rotation_watcher=dev.rotation_watcher)
        all_methods = screen_proxy.SCREEN_METHODS
        methods_class = screen_proxy.screen_method
        for index, (key, value) in enumerate(all_methods.items(), start=1):
            if isinstance(methods_class, value):
                return key
        return None

    @staticmethod
    def check_fast_method(serialno):
        """
        检查最快的、可用的截图方法

        :param serialno: 安卓设备序列号
        :return: str
        """
        dev = Android(serialno=serialno)
        screen_proxy = ScreenProxy.auto_setup(dev.adb, rotation_watcher=dev.rotation_watcher)
        all_methods = screen_proxy.SCREEN_METHODS
        # 从self.SCREEN_METHODS中，逆序取出可用的方法
        best_method = None
        best_time = None
        for name, screen_class in reversed(all_methods.items()):
            screen = screen_class(dev.adb, rotation_watcher=dev.rotation_watcher)
            now1 = time.time()
            result = screen_proxy.check_frame(screen)
            now2 = time.time()
            best_time1 = now2 - now1
            if result:
                if best_time1:
                    if best_time is None:
                        best_time = best_time1
                        best_method = name
                    elif best_time1 < best_time:
                        best_time = best_time1
                        best_method = name
        return best_method
