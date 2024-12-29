# @Time: 2024年12月26日 01:54
# @Author: orcakill
# @File: test_basic_airtest.py
# @Description: BasicAirtest测试用例
import sys
import warnings
from unittest import TestCase

from airtest.core.cv import Template

from autopc.basic.basic_airtest import BasicAirtest
from autopc.basic.basic_opencv import BasicOpenCv
from autopc.utils.utils_logger import my_logger as logger, loguru_showwarning

connect_name = "A2CDUN4312H00817"


# connect_name = '127.0.0.1:62001'


class TestBasicAirtest(TestCase):
    def test_snapshot(self):
        """
        测试截图
        :return:
        """
        BasicAirtest.auto_setup(connect_name)
        BasicAirtest.snapshot("../resources/print/snapshot.png")

    def test_loop_find(self):
        """
        测试循环查找
        :return:
        """
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        screen = BasicAirtest.snapshot()
        pos = BasicAirtest.loop_find(template=template, random_area=0.5)
        BasicOpenCv.draw_point(screen, pos, "../resources/print/loop_find_result.png")

    def test_exists(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        pos = BasicAirtest.exists(template=template)
        logger.info("坐标：{}", pos)

    def test_touch(self):
        self.fail()

    def test_touch_coordinate(self):
        self.fail()

    def test_adb_stop_app(self):
        self.fail()

    def test_adb_start_app(self):
        self.fail()

    def test_adb_restart_app(self):
        self.fail()

    def test_swipe(self):
        self.fail()

    def test_crop_image(self):
        self.fail()

    def test_resolution_ratio(self):
        self.fail()

    def test_cvt_color(self):
        self.fail()

    def test_find_all(self):
        self.fail()

    def test_cv_match(self):
        self.fail()

    def test_match_in(self):
        self.fail()

    def test_text(self):
        self.fail()

    def test_get_cap_method(self):
        self.fail()

    def test_check_fast_method(self):
        self.fail()
