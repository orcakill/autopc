# _*_ coding:UTF-8 _*_
# @Time: 2024年10月02日 22:49
# @Author: orcakill
# @File: version.py.py
# @Description: 版本号
__version__ = "1.0.1.6"

import os
import sys


def get_autopc_version():
    """
    当前版本设置

    :return:
    """
    pip_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    pip_pkg_dir = os.path.abspath(pip_pkg_dir)

    return (
        'autopc {} from {} (python {})'.format(
            __version__, pip_pkg_dir, sys.version[:3],
        )
    )


def show_version():
    sys.stdout.write(get_autopc_version())
    sys.stdout.write(os.linesep)
    sys.exit()
