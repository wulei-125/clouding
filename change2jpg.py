# 批量修改文件名
# 批量修改图片文件名
import os
import re
import sys
from PIL import Image
import string

"""
PATH = "D:\\Code\\98Tang\\数字滤波器(七)--Matlab数字滤波器设计.assets\\"
def renameall():
    # 待修改文件夹
    fileList = os.listdir(PATH)
    # 输出文件夹中包含的文件
    print("修改前：" + str(fileList))
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(PATH)
    num = 1  # 名称变量
    for fileName in fileList:  # 遍历文件夹中所有文件
        pat = ".+\.(jpg|png|pgm|jpeg|JPG)"  # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹配
        os.rename(fileName, (str(num) + '.' + pattern[0]))  # 文件重新命名
        num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    print("修改后：" + str(os.listdir(PATH)))  # 输出修改后文件夹中包含的文件
"""

if __name__ == '__main__':

    dirName = ".\\"  # 最后要加双斜杠，不然会报错
    li = os.listdir(dirName)
    for filename in li:
        newname = filename
        newname = newname.split(".")
        if newname[-1] == "jpeg" or newname[-1] == "png" or newname[-1] == "pgm" or newname[-1] == "JPG" or newname[-1] == "bmp" :
            newname[-1] = "jpg"
            newname = str.join(".", newname)
            filename = dirName + filename
            newname = dirName + newname
            os.rename(filename, newname)
            print(newname, "updated successfully")