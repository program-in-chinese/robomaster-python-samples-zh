def 开始():
    工具.计时器(常量.开始)
    for 次数 in range(1, 501):
        pass
    print(str(次数) +": " + str(工具.累计计时()) + " seconds")
    工具.计时器(常量.重置)

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

start = 开始

工具 = tools
工具.累计计时 = 工具.timer_current
工具.计时器 = 工具.timer_ctrl

# 常量部分
常量 = rm_define
常量.开始 = 常量.timer_start
常量.暂停 = 常量.timer_stop
常量.重置 = 常量.timer_reset
