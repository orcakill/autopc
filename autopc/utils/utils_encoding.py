# _*_ coding:UTF-8 _*_
# @Time: 2024年10月02日 20:25
# @Author: orcakill
# @File: utils_encoding.py
# @Description: 文件格式工具类

import chardet


class UtilsEncoding:

    @staticmethod
    def check_file_encoding(file_path: str):
        """
        检查文件的编码格式并输出

        :param file_path: 文件路径
        :return: None
        """
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
            print("Detected encoding:", encoding)

    @staticmethod
    def check_file_content(file_path: str):
        """
        检查文档的格式

        :param file_path:
        :return:
        """
        install_requires=[]
        with open(file_path, encoding="UTF-16") as file:
            for line in file:
                install_requires.append(line.strip())
        print(install_requires)


if __name__ == '__main__':
    UtilsEncoding.check_file_encoding("utils_version.py")
