# @Time: 2024年12月30日 00:38
# @Author: orcakill
# @File: utils_logger.py
# @Description: 日志文件
import os
import sys
import warnings

from loguru import logger

logger.remove()  # 移除默认的日志记录器


class MyLogger:
    def __init__(self):
        self.logger = logger
        self.logger.remove()

    def configure_logger(self, log_file_path):
        # 添加控制台输出的格式
        self.logger.add(
            sys.stdout,
            level='DEBUG',
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                   "{process.name} | "
                   "{thread.name} | "
                   "<cyan>{module}</cyan>.<cyan>{function}</cyan>"
                   ":<cyan>{line}</cyan> | "
                   "<level>{level}</level>: "
                   "<level>{message}</level>",
        )

    def get_logger(self):
        return self.logger


def loguru_showwarning(message, category):
    logger.warning(f"{category.__name__}: {message}")


# 屏蔽第三方包日志
logger.disable("airtest")

# 创建MyLogger实例
my_logger = MyLogger().get_logger()
