#list列表/集合
#def list_demo():
#这是一个全局变量
blist = [7,8,33,2,1,3,4]
    #alist是局部变量
    #alist = [4,5,6,7,8]
    #通过索引访问 元素 （从下标开始从0,1，2,3,4.....）
    #print(alist)
    #print(alist[0])
    #print(alist[2])
    #倒序访问（倒着数-1，-2，-3，-4.....）
    #print(alist[-1])
    #print(alist[-3])


#更新列表中的元素
#def list_update():
     #alist[0]=1
     #print(alist[0])
     #print(alist)

def list_update():
   alist=[9,99,999,999,9999]
   alist[0]=1
   print(alist[0])
   print(alist)
if __name__ == '__main__':
    list_update()

#切片操作
#全局变量blist(不写在方法里面 上面下面中间都OK 但是不可以写在方法里面 且必须跟方法同级！！！)
#blist=[1,2,3,4,5,6]
#def list_update1(alist):
    #从索引2的位置取到索引5
    #print(alist[2:6])
    #从索引0的位置取到索引5
    #print(alist[:6])
    #从索引3的位置取到索引末尾
    #print(alist[3:])


#耦合度
#def len_demo(alist):
    #print(len(alist))
    #print(len(blist))


#def pop_demo(alist):
    #pop()取中间值删除操作
    #alist.pop(4)
   # print(alist)
#if __name__ == '__main__':
    #alist = [11, 22, 33, 44, 55, 66, 77, 88]
    #调用这个方法
    #list_update1(blist)
    #打印blist
    #print(blist)
    #获取变量的长度 len（）：(len是length的简写就是获取长度的意思)
    #索引和下标是从0开始
    #获取长度是从1开始
    #print(len(alist))
    #print(len(blist))
    #解耦
    #len_demo(alist)
    #删除方法 list.pop()
    #pop（）这个方法有两个作用：1.取出最后一位的值2.删除从列表中取出的值
    #print(alist.pop())
    #print(alist)
    #取中间的值删除
    #pop_demo(alist)







# 讲列表排序的方法
def orderBy_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()
    pass


# 正序方法
def sort_demo():
    # 将blist 正序排
    blist.sort()
    print(blist)


# 倒序方法
def reverse_demo():
    # 将blist 倒序排
    blist.reverse()
    print(blist)


# 列表/集合
if __name__ == '__main__':
    alist = [4, 'ysl', '8', 7, 6, 2, 5]
    orderBy_demo()

