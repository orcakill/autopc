# @Time: 2024年10月21日 14:21
# @Author: orcakill
# @File: basic_adb.py
# @Description: adb相关API,执行adb命令
import subprocess


class BasicADB:

    @staticmethod
    def get_adb_resolution(device_address):
        """
        根据设备信息获取Android设备分辨率

        :param device_address:
        :return:
        """
        command = 'adb -s ' + device_address + ' shell wm size'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        resolution_tuple = output.decode().strip().split(' ')[-1]
        resolution_tuple = tuple(map(int, resolution_tuple.split('x')))
        if resolution_tuple:
            print(resolution_tuple)
            return resolution_tuple
