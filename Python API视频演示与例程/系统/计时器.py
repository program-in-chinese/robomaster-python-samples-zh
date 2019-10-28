def 开始():
    工具.计时器(常量.开始)
    总耗时 = 0
    次数 = 0
    while 次数 < 10:
        算三角函数()
        工具.计时器(常量.暂停)
        总耗时 = 工具.累计计时()
        次数 += 1
        print(总耗时 / 次数)

def 算三角函数():
    积 = 1.0
    for 次数 in range(1, 1000):
        for 角度 in list(range(1, 360)):
            弧度 = 数学.弧度(角度)
            积 *= 数学.正弦(弧度)**2 + 数学.余弦(弧度)**2
    return 积

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

数学 = math
数学.正弦 = math.sin
数学.余弦 = math.cos
数学.弧度 = math.radians
