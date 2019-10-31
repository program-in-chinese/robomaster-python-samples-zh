def start():
    云台.设置旋转速度(20)
    大师.设置模式(常量.底盘跟随模式)
    云台.平转(90)

    运行时间 = 工具.程序运行时间()
    print("90 degree with 20 speed 1: " + str(运行时间))

    云台.平转(-90)
    print("90 degree with 20 speed 2: " + str(工具.程序运行时间() - 运行时间))
    
    运行时间 = 工具.程序运行时间()
    云台.平转(180)
    print("180 degree with 20 speed: " + str(工具.程序运行时间() - 运行时间))
    
    云台.设置旋转速度(40)
    运行时间 = 工具.程序运行时间()
    云台.平转(-180)
    print("180 degree with 40 speed: " + str(工具.程序运行时间() - 运行时间))

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

工具 = tools
工具.程序运行时间 = 工具.run_time_of_program

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl

# 常量部分
常量 = rm_define
常量.底盘跟随模式 = 常量.robot_mode_chassis_follow
常量.云台跟随模式 = 常量.robot_mode_gimbal_follow
常量.自由模式 = 常量.robot_mode_free

常量.云台所有 = 常量.armor_top_all
常量.云台左 = 常量.armor_top_left
常量.云台右 = 常量.armor_top_right

常量.效果常亮 = 常量.effect_always_on
常量.效果熄灭 = 常量.effect_always_off
常量.效果呼吸 = 常量.effect_breath
常量.效果闪烁 = 常量.effect_flash
常量.效果走马灯 = 常量.effect_marquee

时间 = time
时间.睡眠 = 时间.sleep