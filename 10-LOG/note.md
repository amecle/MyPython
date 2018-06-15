# LOG
 - [Python之日志处理（logging模块）](https://www.cnblogs.com/yyds/p/6901864.html)
 - logging模块
 - logging模块提供模块级别的函数记录日志
 - 包括四大组件
 
## 1. 日志相关概念
 - 日志：程序运行的时候，定期、自动的记录一些关于运行的信息。
    - 通常有一个文件专门记录，这个文件写在磁盘上。
    - 日志记录属于I/O操作，I/O操作非常慢
    - 轻易不应有大量的I/O操作，但是日志必须要有
    - 所以，写日志不要太频繁，只记录关键信息
 - 日志的级别（level）
    - 不同的用户关注不同的程序信息
    - DEBUG 调试
    - INFO 信息
    - NOTICE 通知
    - WARNING 警告
    - ERROR 错误
    - CRITICAL 紧急
    - ALERT 报警
    - EMERGENCY 紧急事件
 - I/O操作 --> 不要频繁操作
 - LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
 - 日志信息
    - time
    - 地点
    - level
    - 内容
 - 成熟的第三方日志
    - log4j
    - log4php
    - logging
    
# 2 Logging模块
 - 日志级别
    - 级别可以自定义
    - DEBUG 调试
    - INFO 信息
    - WARNING 警告
    - ERROR 错误
    - CRITICAL 紧急
 - 初始化/写日志实例需要指定级别，只有当级别>=指定级别才被记录
 - 使用方式：单例模式
    - 直接使用logging(封装了其他组件)
    - loging四大组件直接定制
    
# 2.1 logging模块级别的日志
 - 使用以下几个函数
    - logging.debug(msg,*args,**kwargs)  创建一条严重级别为DEBUG的日志记录
    - logging.info(msg,*args,**kwargs)  创建一条严重级别为INFO的日志记录
    - logging.warning(msg,*args,**kwargs)  创建一条严重级别为WARNING的日志记录
    - logging.error(msg,*args,**kwargs)  创建一条严重级别为ERROR的日志记录
    - logging.critical(msg,*args,**kwargs)  创建一条严重级别为CRITICAL的日志记录
    - logging.log(level,*args,**kwargs)  创建一条严重级别为level的日志记录
    - logging.basicConfig(**kwargs)  对root logger进行一次性配置
 - logging.basicConfig(**kwargs)  对root logger进行一次性配置
    - 只在第一次调用的时候起作用
    - 不配置 logger 则使用默认值
        - 输出：sys.stderr (控制台)
        - 级别：WARNING
        - 格式：level:log_name:content  （log_name:专门写日志的实例,叫root）
 - 案例 01.py
 - format参数
 
        asctime      %(asctime)s     日志事件发生的时间
        created
        relativeCreated
        msecs
        levelname
        levelno
        name      %(name)s    所使用的日志器名称，默认是'root'，因为默认使用的是rootLogger
        message
        pathname
        filename
        module
        lineno
        funcName
        process
        processName
        thread
        threadName
        
# 2.1 logging 模块的处理流程
 - 四大组件
    - 日志器（Logger）：产生日志的一个接口
        - 负责产生一条日志
    - 处理器（Handler）：把产生的日志发送到相应的目的地(有时一个日志要发送到多个目的地)
        - 日志产生后有不同的去向，一个处理器负责一个去向
    - 过滤器（Filter）：更精细的控制那些日志输出（级别就可以看作一个简单的Filter）
        - 对符合条件的日志让其输出，不符合条件的给过滤掉
    - 格式器（Formatter）：对输出信息进行格式化
        - 格式器按相应的格式给他输出
 - Logger
    - 产生一个日志
    - 操作
    
            Logger.setLevel()  设置日志器将会处理的日志消息的最低级别
            Logger.addHandler()  为该logger对象添加一个handler
            Logger.removeHandler()  移除一个handler
            Logger.addFilter()  为该logger对象添加一个filter
            Logger.removeFilter()  移除一个filter
            Logger.debug()  产生一条debug级别的日志，同理，info，error 等
            Logger.exception()  创建类似于Logger.error的日志消息
            Logger.log()  获取一个明确的日志level参数类创建一个日志记录
    - 如何得到一个logger对象
        - 实例化(不推荐)
        - logging.getLogger()
           - 推荐用法
 - Handler 
    - 把 log 发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter, removeFilter
    - 不需要直接使用，Handler 是基类，给继承用的，他的子类如下：
    
            logging.StreamHandler  将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象
            logging.FileHandler  将日志消息发送到磁盘文件，默认情况下文件大学会无限增长
            logging.handlers.RotatingFileHandler  将日志消息发送到磁盘文件，并支持日志文件按大小切割（可以每10M写一个文件）
               - （重要）（文件旋转）
            logging.handlers.TimedRotatingFileHandler  将日志消息发送到磁盘文件，并支持日志文件按时间切割（可以每天写一个文件）
               - （时间旋转）
            logging.handlers.HTTPHandler  将日志消息以GET或POST的方式发送给一个HTTP服务器
            logging.handlers.SMTPHandler  将日志消息发送给一个指定的email地址
            logging.NullHandler  该Handler实例会忽略error message。通常被想使用logging的library……
            
 - Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        - datefmt：指定日期格式字符串，如果不指定该参数则默认使用'%Y-%m-%d %H:%M:%S'
        - style：python 3.2新增的参数，可取值为'%', '{', '$',如果不指定该参数则默认使用'%' 
 - Filter 类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容
  