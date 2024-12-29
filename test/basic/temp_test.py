# @Time: 2024年12月26日 03:08
# @Author: orcakill
# @File: temp_test.py
# @Description: 测试
import warnings
from loguru import logger

def loguru_showwarning(message, category):
    logger.warning(f"{category.__name__}: {message}")



if __name__ == '__main__':
    warnings.showwarning = loguru_showwarning
    warnings.warn("Currently using ADB screenshots, the efficiency may be very low.")
