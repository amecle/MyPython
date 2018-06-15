# 利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    # 把参数打印出来
    print('我是参数',in1)
    time.sleep(4)
    print('End loop 1 at :', time.ctime())

def loop2(in1,in2):
    # ctime 得到当前时间
    print('Start loop 2 at :',time.ctime())
    # 把参数打印出来
    print('我是参数',in1,'和参数',in2)
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('Starting at:',time.ctime())
    t1 = threading.Thread(target=loop1,args=('王大',))
    t1.start()

    t2 = threading.Thread(target=loop2,args=('王一','王二'))
    t2.start()

    # 将t1，t2子线程join
    # 主线程必须等待t1，t2子线程执行完毕才会往下执行
    t1.join()
    t2.join()
    # 下面的print 一定是最后执行的语句
    print('All done at :',time.ctime())

if __name__ == '__main__':
    # 启动多线程后本程序就作为主线程存在
    # 创建的多线程为子线程，这时程序有3个线程在运行
    main()
    # 主线程执行完毕，进程结束，则子线程可能也要终止
    # 所以看到的结果是：子线程的print语句也许不会被执行

    # 一定要有while语句（死循环），来等待子线程执行完毕
while True:
        time.sleep(10)