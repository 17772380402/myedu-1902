import os

# if __name__ == '__main__':
#       # 获取当前目录的路径
#       getcwd=os.getcwd()
#       print(getcwd)
#       # 获取上级目录的路径
#       abspath = os.path.abspath('..')
#       print(abspath )
#       # 获取上上级目录的路径
#       abspath1= os.path.abspath('../..')
#       print(abspath1)

def open_demo():
    # 绝对路径../test.text
    # 相对路径C:\Users\Administrator\PycharmProjects\myedu.\test.text
    text_io=open('../test.text','w+')
    text_io.write("我呵呵呵呵呵")
if __name__ == '__main__':
    open_demo()

def open_demo1():
    # 绝对路径../test.text
    # 相对路径C:\Users\Administrator\PycharmProjects\myedu.\test.text
    text_io=open('../test.text','a+')
    text_io.write("我呵呵呵呵呵")
if __name__ == '__main__':
    open_demo1()

def open_demo():
    # 绝对路径../test.text
    # 相对路径C:\Users\Administrator\PycharmProjects\myedu.\test.text
    # r代表只读模式，不可以写入
    text_io=open('../test.text','r')

def open_demo3():
    open_demo()
    readline =text_io.readline()
    print(readline)
    readlines=text_io.readlines()
    print(readlines)