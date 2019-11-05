def 开始():
    云台灯(常量.云台所有, 红色, 常量.效果常亮)
    时间戳 = 工具.取上电时间()
    print(时间戳)

    云台.设置旋转速度(20)
    底盘.设置旋转速度(20)

    大师.设置模式(常量.自由模式)
    
    底盘.旋转指定角度(常量.顺时针, 40)
    底盘.旋转指定角度(常量.逆时针, 40)

    print(工具.取上电时间() - 时间戳)
    云台.俯仰(30)
    云台.俯仰(-10)

    print(工具.取上电时间() - 时间戳)

def 云台灯(位置, 颜色, 灯效):
    LED灯.云台(位置, 颜色['红'], 颜色['绿'], 颜色['蓝'], 灯效)

红色 = {'红': 255, '绿': 0, '蓝': 0}

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

start = 开始

工具 = tools
工具.取上电时间 = tools.get_unixtime

LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led

大师 = robot_ctrl
大师.设置模式 = 大师.set_mode

云台 = gimbal_ctrl
云台.设置旋转速度 = 云台.set_rotate_speed
云台.平转 = 云台.yaw_ctrl
云台.俯仰 = 云台.pitch_ctrl

底盘 = chassis_ctrl
底盘.设置旋转速度 = 底盘.set_rotate_speed
底盘.旋转指定角度 = 底盘.rotate_with_degree

# 常量部分
常量 = rm_define
常量.底盘跟随模式 = 常量.robot_mode_chassis_follow
常量.云台跟随模式 = 常量.robot_mode_gimbal_follow
常量.自由模式 = 常量.robot_mode_free

常量.顺时针 = 常量.clockwise
常量.逆时针 = 常量.anticlockwise

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