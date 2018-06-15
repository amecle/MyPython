# 利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程启动方法
import time
import _thread as thread

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
    thread.start_new_thread(loop1,('王大',))
    thread.start_new_thread(loop2,('王一','王二'))
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