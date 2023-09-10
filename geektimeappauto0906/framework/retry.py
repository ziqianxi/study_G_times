import allure


def retry(fun):
    def wrap(*args, **kwargs):
        # 找到当前的状态
        po = args[0]
        fun_info = f"{fun.__name__}({args}, {kwargs})"

        try:
            r = fun(*args, **kwargs)
            print(f"{r} = {fun_info}")
            allure.attach(
                name=fun_info,
                body=po.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)
            return r
        except:
            # 保存现场
            allure.attach(
                name=fun_info,
                body=po.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG)

            # 异常处理
            po.exception_handle()
            # 重试
            return wrap(*args, **kwargs)

    return wrap
