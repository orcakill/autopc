# @Time: 2024年10月01日 03:23
# @Author: orcakill
# @File: airtest.py
# @Description: airtest相关的api接口
import logging

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
    def exists(template: Template, cvstrategy: [], timeout: float):
        """
        判断模板图片在设备上是否存在，如果存在返回坐标

        :param template: 图片类
        :param cvstrategy: 图像识别算法
        :param timeout: 超时时间
        :return: bool
        """
        Settings.CVSTRATEGY = cvstrategy
        Settings.FIND_TIMEOUT_TMP = timeout
        return exists(template)

    @staticmethod
    def touch(template: Template, cvstrategy: [], timeout: float, times: int, duration: float):
        """
        判断模板图片在设备上是否存在，如果存在点击
        :param times: 点击次数
        :param duration: 按住时间
        :param template: 图片类
        :param cvstrategy: 图像识别算法
        :param timeout: 超时时间
        :return: bool

        """
        Settings.CVSTRATEGY = cvstrategy
        Settings.FIND_TIMEOUT = timeout
        if touch(template, times=times, duration=duration):
            return True
        else:
            return False

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
