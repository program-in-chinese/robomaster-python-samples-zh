def start():
    云台.设置旋转速度(60)

    print('no move')
    LED灯.枪亮()
    大师.设置模式(常量.跟随底盘模式)
    云台.平转(20)

    print('only gimbal move')
    LED灯.枪亮()
    大师.设置模式(常量.自由模式)
    云台.平转(20)

    print('both move')
    大师.设置模式(常量.跟随云台模式)
    云台.平转(20)

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.
LED灯 = led_ctrl
LED灯.枪亮 = LED灯.gun_led_on
LED灯.枪暗 = LED灯.gun_led_off

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl

常量 = rm_define
常量.跟随底盘模式 = 常量.robot_chassis_follow
常量.跟随云台模式 = 常量.robot_gimbal_follow
常量.自由模式 = 常量.robot_mode_free
