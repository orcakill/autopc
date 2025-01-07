# AutoPC

**Cross-Platform UI Automation Framework for Games and Apps**（[中文版点这里](./README.md)）

## Quick start

* **Run Anywhere：** AutoPC provides cross platform APIs, including application installation, image recognition, analog input, and more. Based on image recognition technology to locate UI elements, you can automate without embedding any code.

* **Extensibility：** AutoPC provides command-line and Python interfaces, making it easy to run on large-scale device clusters.

## install

Install the AutoPC framework using `pip` 

```Shell
pip install -U autopc
```

To operate Android on Windows system, it is necessary to check whether the device has been connected through ADB

```Shell
# windows
adb devices
```

## documentation

Please refer to the complete AutoPC documentation [readthedocs](http://https://autopc.readthedocs.io/zh-cn/latest/)。

## example

AutoPC provides platform independent Python APIs, allowing your automation code to run on Windows and operate applications on different platforms.

1. Use [connect_device](https://autopc.readthedocs.io/zh-cn/latest/source/autopc.basic.basic_airtest.html#auto_step）
   To connect to any Android device or Windows window.
2. Using [Simulation Operation](https://autopc.readthedocs.io/zh-cn/latest/README_MORE.html#id9)The API for 'input' automates your game or app.

```Python
from autopc.basic.basic_airtest import *

# Connect local Android devices through ADB
BasicAirtest.auto_setup("Android")
# Launch the APP
BasicAirtest.adb_start_app("package_name_of_your_apk")
# Click on the image on the screen
BasicAirtest.touch(Template("image_of_a_button.png"))
# Slide from Image 1 to Image 2
BasicAirtest.swipe(Template("slide_start.png"), Template("slide_end.png"))
```

For a more detailed explanation, please refer to [AutoPC Python API documentation](https://autopc.readthedocs.io/zh-cn/latest/source/autopc.basic.basic_airtest.html)
Or just watch it directly [API代码](../autopc/autopc/basic/basic_airtest.py) 。

## Contribution code

Welcome everyone to fork and submit pull requests.

## acknowledgments

Thank you to the following warehouses for making AutoPC better:

- [stf](https://github.com/openstf)
- [opencv](https://github.com/opencv/opencv-python)
- [airtest](https://github.com/AirtestProject/Airtest)

## About me

Individual developer
