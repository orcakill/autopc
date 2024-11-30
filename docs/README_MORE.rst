AutoPC
=======

**游戏和应用程序的跨平台 UI 自动化框架**

开始
---------------

*   **跨平台:** AutoPC 几乎可以通过PC自动化多个平台上游戏和应用程序。

*   **一次编写，随处运行:** AutoPC 提供了跨平台的 API，包括 App 安装、模拟输入、断言等。AutoPC使用图像识别技术定位UI元素，无需注入任何代码即可实现游戏和应用的自动化。

*   **完全可扩展:** AutoPC提供诸多API函数，通过编写python调用函数实现更多可扩展的功能。

支持的平台
...................

-  Android
-  Windows

安装
------------

系统要求
...................

-  操作系统:

   -  Windows

-  Python3.9


安装 python 软件包
..............................

AutoPC 包可以直接从 Pypi 安装。
使用pip管理所有 python 依赖项和包的安装
itself.

.. code:: shell

    pip install -U autopc


您也可以从 Git 存储库安装它。

.. code:: shell

    git clone https://github.com/orcakill/autopc.git
    pip install -e autopc


在这里使用 ''-e'' 以 develop 模式安装 airtest，因为这个仓库在
快速发展。然后你可以用 ''git pull'' 升级仓库。


文档
-------------

你可以在 `readthedocs`_ 上找到完整的 AutoPC 文档。


例子
------------

AutoPC提供了独立于平台的简单API。本节
描述如何创建执行以下操作的自动化案例：

1. 连接到本地 Android 设备 ``adb``
2. 安装 ''APK'' 应用程序
3. 运行应用程序并截取屏幕截图
4. 执行多个用户操作（触摸、滑动、KeyEvent）
5. 卸载应用程序

.. code:: python

    from autopc.basic.airtest import *

    # connect an android phone with adb
    init_device("Android")
    # or use connect_device api
    # connect_device("Android:///")

    install("path/to/your/apk")
    start_app("package_name_of_your_apk")
    touch(Template("image_of_a_button.png"))
    swipe(Template("slide_start.png"), Template("slide_end.png"))
    assert_exists(Template("success.png"))
    keyevent("BACK")
    home()
    uninstall("package_name_of_your_apk")


更详细的信息请参考 `AutoPC Python API参考`_ 。

基本用法
------------

AutoPC旨在提供独立于平台的API，这样你就可以一次编写自动化案例，并在多个设备和平台上运行。

1. 使用 `connect_device`_ API，您可以连接到任何 android 设备或 Windows 应用程序。

2. 然后执行 `simulated input`_  以自动化您的游戏或应用程序。


连接设备
...............

使用 ''connect_device'' API，您可以连接到任何 android/ 设备或 Windows 应用程序。

.. code:: python

    connect_device("platform://host:port/uuid?param=value&param2=value2")

- 平台: Android/Windows...

- host: 适用于 Android 的 adb 主机，对于其他平台为空

- port: Android 的 adb 端口，其他平台为空

- uuid: 目标设备的 uuid，例如 serialno 用于 Android，handle 用于 Windows

- param: 设备初始化配置字段。例如 cap_method/ori_method/...

- value: 设备初始化配置字段值。


另请参阅 `connect_device`_.

连接 Android 设备
***********************

1. 使用 USB 将您的 Android 手机连接到您的 PC
2. 使用 ''adb devices'' 确保状态为 ''device''
3. 在AutoPC中连接设备
4. 如果您有多个设备甚至远程设备，请使用更多的参数来指定设备

.. code:: python

    # connect an android phone with adb
    init_device("Android")

    # or use connect_device api with default params
    connect_device("android:///")

    # connect a remote device using custom params
    connect_device("android://adbhost:adbport/1234566?cap_method=javacap&touch_method=adb")

连接 Windows 应用程序
****************************

.. code:: python

    # connect local windows desktop
    connect_device("Windows:///")

    # connect local windows application
    connect_device("Windows:///?title_re=unity.*")


AutoPC 使用 pywinauto 作为 Windows 后端。更多窗口搜索参数请参见 `pywinauto documentation`_ 文档。


模拟输入
...............

完全支持以下 API：

- touch(点击)
- swipe(滑动)
- text(文本输入)
- keyevent(关键事件检查)、
- snapshot(屏幕截图)
- wait(等待)

还有更多 API 可用，其中一些可能是特定于平台的，有关更多信息，请参阅 `API reference`_ 。



.. _readthedocs: http://https://autopc.readthedocs.io/zh-cn/latest/
.. _simulated input: https://autopc.readthedocs.io/zh-cn/latest//README_MORE.html#simulate-input
.. _AutoPC Python API参考:  https://autopc.readthedocs.io/zh-cn/latest/all_module/airtest.core.api.html
.. _API reference: https://autopc.readthedocs.io/zh-cn/latest//index.html#main-api
.. _connect_device: https://autopc.readthedocs.io/zh-cn/latest/source/autopc.basic.basic_airtest.html#autopc.basic.basic_airtest.auto_setup
.. _pywinauto documentation: https://autopc.readthedocs.io/zh-cn/latest//code/pywinauto.findwindows.html#pywinauto.findwindows.find_elements