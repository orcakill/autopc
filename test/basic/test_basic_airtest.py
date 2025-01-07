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
from autopc.utils.utils_logger import my_logger as logger

# connect_name = "A2CDUN4312H00817"
connect_name = '127.0.0.1:62001'


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
        screen = BasicAirtest.snapshot()
        pos = BasicAirtest.exists(template=template)
        BasicOpenCv.draw_point(screen, pos, "../resources/print/exists_result.png")
        logger.info("坐标：{}", pos)

    def test_touch(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        BasicAirtest.touch(template=template)

    def test_touch_coordinate(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        pos = BasicAirtest.exists(template=template)
        logger.info("坐标：{}", pos)
        BasicAirtest.touch_coordinate(pos)

    def test_adb_stop_app(self):
        BasicAirtest.adb_stop_app("com.netease.onmyoji")

    def test_adb_start_app(self):
        BasicAirtest.adb_start_app("com.netease.onmyoji")

    def test_adb_restart_app(self):
        BasicAirtest.adb_restart_app("com.netease.onmyoji")

    def test_swipe(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        pos = BasicAirtest.exists(template=template)
        pos1 = (pos[0] + 200, pos[1])
        logger.info("坐标：{}", pos)
        logger.info("坐标：{}", pos1)
        BasicAirtest.touch_coordinate(pos)

    def test_crop_image(self):
        BasicAirtest.auto_setup(connect_name)
        BasicAirtest.crop_image(100, 100, 200, 200)

    def test_resolution_ratio(self):
        BasicAirtest.auto_setup(connect_name)
        resolution_ratio = BasicAirtest.resolution_ratio()
        logger.debug("设备分辨率：{}", resolution_ratio)

    def test_cvt_color(self):
        BasicAirtest.auto_setup(connect_name)
        screen = BasicAirtest.snapshot()
        BasicAirtest.cvt_color(screen)

    def test_find_all(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        pos = BasicAirtest.find_all(template=template)
        logger.info("坐标：{}", pos)

    def test_cv_match(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox_all.png")
        screen = BasicAirtest.snapshot()
        result = BasicAirtest.cv_match(template=template, screen=screen)
        logger.info("识别结果：{}", result)

    def test_match_in(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox_all.png")
        screen = BasicAirtest.snapshot()
        pos = BasicAirtest.match_in(template=template, screen=screen)
        logger.info("识别结果：{}", pos)

    def test_text(self):
        BasicAirtest.auto_setup(connect_name)
        BasicAirtest.text("123")

    def test_get_cap_method(self):
        BasicAirtest.auto_setup(connect_name)
        result = BasicAirtest.get_cap_method(connect_name)
        logger.info("识别结果：{}", result)

    def test_check_fast_method(self):
        BasicAirtest.auto_setup(connect_name)
        result = BasicAirtest.check_fast_method(connect_name)
        logger.info("识别结果：{}", result)
