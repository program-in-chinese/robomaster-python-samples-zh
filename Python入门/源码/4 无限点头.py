# 可见控制台中打出当前点头的次数, print可用于实时监控某变量的值
def start():
    次数 = 0
    while True:
        云台.俯仰(30)
        云台.俯仰(-10)
        次数 += 1
        print(次数)

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

云台 = gimbal_ctrl
云台.俯仰 = 云台.pitch_ctrl
