# AutoPC

**基于Windows的跨平台的UI自动化框架，适用于游戏和App**（[Click here for the English version](https://github.com/orcakill/autopc/blob/master/README_en.md)）

## 快速开始

* **各种运行：** AutoPC提供了跨平台的API，包括安装应用、图像识别、模拟输入等。 基于图像识别技术定位UI元素，你无需嵌入任何代码即可进行自动化。

* **扩展性：** AutoPC提供了命令行和python接口，可以很容易地在大规模设备集群上运行。

## 安装

使用 `pip` 安装AutoPC框架

```Shell
pip install -U autopc
```

在Windows系统下操作Android，需要检查设备是否已经通过ADB连接

```Shell
# windows系统
adb devices
```

## 文档

完整的AutoPC文档请看 [readthedocs](http://autopc.readthedocs.io/zh-cn/latest/)。

## 例子

AutoPC提供与平台无关的的python API，让你的自动化代码可以运行Windows上，操作不同平台的应用。

1. 使用 [connect_device](https://autopc.readthedocs.io/zh-cn/latest/source/autopc.basic.basic_airtest.html#auto_step)
   来连接任意Android设备或者Windows窗口。
2. 使用 [模拟操作](https://autopc.readthedocs.io/zh-cn/latest/README_MORE.html#id9) 的API来自动化你的游戏或者App。

```Python
from autopc.basic.basic_airtest import *

# 通过ADB连接本地Android设备
BasicAirtest.auto_setup("Android")
# 启动APP
BasicAirtest.adb_start_app("package_name_of_your_apk")
# 点击屏幕的图片
BasicAirtest.touch(Template("image_of_a_button.png"))
# 从图片1滑动到图片2
BasicAirtest.swipe(Template("slide_start.png"), Template("slide_end.png"))
```

更详细的说明请看 [AutoPC Python API 文档](https://autopc.readthedocs.io/zh-cn/latest/source/autopc.basic.basic_airtest.html)
或者直接看 [API代码](../autopc/autopc/basic/basic_airtest.py) 。

## 贡献代码

欢迎大家fork和提pull requests。

## 致谢

感谢以下仓库让AutoPC变得更好：

- [stf](https://github.com/openstf)
- [opencv](https://github.com/opencv/opencv-python)
- [airtest](https://github.com/AirtestProject/Airtest)

## 关于我

个人开发者
