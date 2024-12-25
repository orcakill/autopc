# @Time: 2024年12月26日 00:13
# @Author: orcakill
# @File: test_basic_adb.py
# @Description: BasicADB测试用例
from unittest import TestCase

from autopc.basic.basic_adb import BasicADB


class TestBasicADB(TestCase):
    def test_get_adb_resolution(self):
        """
        测试获取adb分辨率

        :return:
        """
        return  BasicADB.get_adb_resolution("A2CDUN4312H00817")
