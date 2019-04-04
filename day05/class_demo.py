# class 类
# object  对象/或者所有类的父类
class  Human(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    # 第一种
    def myInfo(self):
        print('我叫%s，我今年%s岁，%s'%(self.name,self.age,self.sex))
    # 第二种
    def myInfostr(self):
        return '我叫%s，我今年%s岁，%s'%(self.name,self.age,self.sex)

#     继承
class Tester(Human):
    def zhixingceshi(self):
        print(self.name )
        print('我是大哥')
        self.myInfo()

if __name__ == '__main__':
    # 第一种
    # human=Human('Lee',21,'女')
    # print(type(human))
    # human.myInfo()
    #
    # 第二种
    # info_str = human.myInfostr()
    # print(info_str)
    # 继承
    # 对象 是  类的    实例化
    tester = Tester('Lee', 21, '女')
    tester.zhixingceshi()

