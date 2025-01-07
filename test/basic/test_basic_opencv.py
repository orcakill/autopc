# @Time: 2025年01月07日 14:32
# @Author: orcakill
# @File: test_basic_opencv.py
# @Description: opencv的测试函数
from unittest import TestCase

from airtest.core.cv import Template

from autopc.basic.basic_airtest import BasicAirtest
from autopc.basic.basic_opencv import BasicOpenCv
from autopc.utils.utils_logger import my_logger as logger

# connect_name = "A2CDUN4312H00817"
connect_name = '127.0.0.1:62001'

class TestBasicOpenCv(TestCase):
    def test_draw_rectangle(self):
        BasicAirtest.auto_setup(connect_name)
        screen = BasicAirtest.snapshot()
        BasicOpenCv.draw_rectangle(screen, 100, 100, 200, 200, "../resources/print/draw_rectangle_result.png")

    def test_draw_point(self):
        BasicAirtest.auto_setup(connect_name)
        template = Template("../resources/sources/loop_nox.png")
        screen = BasicAirtest.snapshot()
        pos = BasicAirtest.loop_find(template=template, random_area=0.5)
        BasicOpenCv.draw_point(screen, pos, "../resources/print/loop_find_result.png")

    def test_get_color_format(self):
        BasicAirtest.auto_setup(connect_name)
        screen = BasicAirtest.snapshot()
        result = BasicOpenCv.get_color_format(screen)
        logger.info("识别结果：{}", result)
