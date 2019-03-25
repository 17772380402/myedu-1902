def zuihou():
    a='123456'
    # try作为异常处理，如果异常，则执行except内的代码
    try:
        # 判断a是否包含5
        assert '4' in a
    #     except报错后执行
    except:
         print('a里面没有7')
    # print('------')
   # 不管是否有异常，finally里面的代码 都会被执行
    finally:
        print('最后----')
if __name__ == '__main__':
    zuihou()


