def break_demo():
    for i in range (5):
        print('第%s次循环'%i)
#         如果i等于2
        if i ==2:
            print('')
            # 终止所有循环
            break
            print('第%s次循环,if判断之后'%i)
        print('')
if __name__ == '__main__':
    break_demo()


    def continue_demo():
        for i in range(5):
            print('第%s次循环' % i)
            #         如果i等于2
            if i == 2:
                print('')
                # 终止本次循环
                continue
                print('第%s次循环,if判断之后' % i)
            print('')


if __name__ == '__main__':
        continue_demo()

        
