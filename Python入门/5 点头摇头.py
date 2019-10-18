def start():
    大师.设置模式(常量.自由模式)
    次数 = 0
    while True:
        if 次数 % 2 == 0:
            云台.俯仰(30)
            云台.俯仰(-10)
            print(str(次数) + ' nod')
        else:
            云台.平转(10)
            云台.平转(-10)
            云台.平转(0)
            print(str(次数) + ' shake')
        次数 += 1

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

云台 = gimbal_ctrl
云台.俯仰 = 云台.pitch_ctrl
云台.平转 = 云台.yaw_ctrl

常量 = rm_define
常量.自由模式 = 常量.robot_mode_free
