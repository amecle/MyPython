# 环境
 - xubuntu 16.04
 - anaconda
 - pycharm
 - python3.6
 - [python开发线程:线程&守护线程&全局解释器锁]
    - (https://www.cnblogs.com/jokerbj/p/7460260.html)
 - [GIL全局解释锁（英）]
    - (http://www.dabeaz.com/python/UnderstandingGIL.pdf)

# 多线程 vs 多进程
 - 程序：一堆代码以文本形式存入一个文档。（文件，死的，可以修改）
 - 进程：程序运行的一个状态。（程序跑起来就是进程，在内存中，活的）
    - 包含地址空间，内存，数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
 - 线程：
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程之间共享数据和上下文运行环境
    - 共享互斥问题
 - 全局解释器锁（GIL）
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只允许有一个控制线程在执行（伪多线程）
    
 - Python包
    - thread：有问题，不好用，python3 改成了 _thread
    - threading：通行的包
    - 案例01.py：顺序执行，耗时比较长
    - 案例02.py：改用多线程，缩短总时间，使用 _thread
    - 案例03.py：多线程，传参数，使用 _thread
 - threading 的使用
    - 直接利用threading.Thread生成Thread实例
       1. t = threading.Thread(target=函数命,args=(参数,))
       2. t.start()  启动多线程
       3. t.join()  等待多线程执行完成
       4. 案例 04.py
       5. 案例 05.py : 加入join后比较和案例04.py结果的异同
       - 守护线程  - daemon
          - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
          - 一般认为，守护线程不重要，或者不允许离开主线程独立运行
          - 守护线程案例能否有效果跟环境相关
          - 案例06.py 非守护线程
          - 案例07.py 守护线程