import logging


def log_func(handler):
    if handler.get_status() < 400:
        log_method = logging.info
    elif handler.get_status() < 500:
        log_method = logging.warning
    else:
        log_method = logging.error
    request_time = 1000.0 * handler.request.request_time()
    log_method("%d %s %s (%s) %s %s %.2fms",
               handler.get_status(), handler.request.method,
               handler.request.uri, handler.request.remote_ip,
               handler.request.arguments,
               request_time)


configs = dict(
    LOG_LEVEL=logging.INFO,  # 日志等级
    debug=True,  # Debug
    log_function=log_func,  # 日志处理方法
    template_path='views',  # html文件
    static_path='statics',  # 静态文件（css,js,img）
    static_url_prefix='/statics/',  # 静态文件前缀
    cookie_secret='suoning',  # cookie自定义字符串加盐
    xsrf_cookies=True,  # 防止跨站伪造
)
