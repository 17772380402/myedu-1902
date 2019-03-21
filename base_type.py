# if __name__ == '__main__':
# print('hello world')


# 声明一个 int_demo方法
# def int_demo():
# 声明aint变量，并赋值1
# aint = 1
# 打印aint的值
# print(aint)

# 声明一个add的方法
# def add(aint, bint):
# 打印aint的值
# print(aint)
# 打印bint的值
# print(bint)
# 返回aint+bint
# return aint + bint


# if __name__ == '__main__':
# 提取变量ctrl+alt+v
# 调用add方法，传入1,2，得到返回值，赋值给result变量
# result = add(1, 2)
# print(result)



# 声明一个 float_demo方法
#def float_demo():
    # 声明变量，并赋值
    #afloat = 1.99
    #打印float的值
   # print(afloat)
#if __name__ == '__main__':
   # float_demo()


#def str_demo():
    #a='hello'
    #b='  world'
    #return a+b
#if __name__ == '__main__':
    #print(str_demo())






def str_demo():
    a='hello'
    b=666
    #下面这一步可省略
    print('%s%s'%(a,b))
    s=str(b)
    print(s)
    print(type(s))
    print(a+s)
if __name__ == '__main__':
    str_demo()