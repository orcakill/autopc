# AutoPC

**基于Windows的跨平台的UI自动化框架，适用于游戏和App**

## 快速开始

*   **各种运行：** AutoPC提供了跨平台的API，包括安装应用、模拟输入、断言等。 基于图像识别技术定位UI元素，你无需嵌入任何代码即可进行自动化。

*   **扩展性：** AutoPC提供了命令行和python接口，可以很容易地在大规模设备集群上运行。

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

完整的AutoPC文档请看 [readthedocs](http://https://autopc.readthedocs.io/zh-cn/latest/)。


## 例子

AutoPC希望提供平台无关的API，让你的自动化代码可以运行Windows上，操作不同平台的应用。

1. 使用 [connect_device](http://airtest.readthedocs.io/zh_CN/latest/README_MORE.html#connect-device) 来连接任意Android设备或者Windows窗口。
2. 使用 [模拟操作](http://airtest.readthedocs.io/zh_CN/latest/README_MORE.html#simulate-input) 的API来自动化你的游戏或者App。


```Python
from autopc.basic.basic_adb import *
from autopc.basic.basic_airtest import *

# 通过ADB连接本地Android设备
init_device("Android")
# 或者使用connect_device函数
# connect_device("Android:///")
connect_device("Android:///")
install("path/to/your/apk")
start_app("package_name_of_your_apk")
touch(Template("image_of_a_button.png"))
swipe(Template("slide_start.png"), Template("slide_end.png"))
assert_exists(Template("success.png"))
keyevent("BACK")
home()
uninstall("package_name_of_your_apk")
```

更详细的说明请看 [Airtest Python API 文档](http://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html) 或者直接看 [API代码](./airtest/core/api.py) 。



## 贡献代码

欢迎大家fork和提pull requests。[这里需要大家的帮助](./docs/wiki/platforms.md#pull-request-guide)


## 致谢

感谢以下仓库让AutoPC变得更好：

- [stf](https://github.com/openstf)


## 关于我们

个人开发者
