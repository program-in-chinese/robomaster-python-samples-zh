def start():
    次数 = 0
    while True:
        云台.俯仰(30)
        云台.俯仰(-10)
        次数 += 1
        if 次数 == 3:
            break

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

云台 = gimbal_ctrl
云台.俯仰 = 云台.pitch_ctrl