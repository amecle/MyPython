'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread

def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    # 睡眠4秒，单位：秒
    time.sleep(4)
    print('End loop 1 at :', time.ctime())

def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :',time.ctime())
    # 睡眠4秒，单位：秒
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('Starting at:',time.ctime())

    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_tread
    # 参数：1.需要运行的函数名，2.函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())

    print('All done at:',time.ctime())

if __name__ == '__main__':
    # 启动多线程后本程序就作为主线程存在
    # 创建的多线程为子线程，这时程序有3个线程在运行
    main()
    # 主线程执行完毕，进程结束，则子线程可能也要终止
    # 所以看到的结果是：子线程的print语句也许不会被执行

    # 一定要有while语句（死循环），来等待子线程执行完毕
    #while True:
    #    time.sleep(1)