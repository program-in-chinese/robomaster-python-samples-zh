def start():
    云台灯(常量.云台左, 红色, 常量.效果常亮)
    时间.睡眠(2)
    LED灯.熄灭(常量.云台左)
    # 云台灯(常量.云台左, 绿色, 常量.效果熄灭)
    时间.睡眠(1)
    云台单灯(常量.云台左, 1, 常量.效果常亮)
    时间.睡眠(2)

def 云台单灯(位置, 序号, 灯效):
    LED灯.云台单灯(位置, 序号, 灯效)

def 云台灯(位置, 颜色, 灯效):
    LED灯.云台(位置, 颜色['红'], 颜色['绿'], 颜色['蓝'], 灯效)

红色 = {'红': 255, '绿': 0, '蓝': 0}
绿色 = {'红': 0, '绿': 255, '蓝': 0}

# 以下为API中文化部分, 与程序逻辑无关. 请勿作修改.

LED灯 = led_ctrl
LED灯.云台 = LED灯.set_top_led
LED灯.熄灭 = LED灯.turn_off

# 常量部分
常量 = rm_define
常量.装甲所有 = 常量.armor_all
常量.底盘前 = 常量.armor_bottom_front
常量.底盘后 = 常量.armor_bottom_back
常量.底盘左 = 常量.armor_bottom_left
常量.底盘右 = 常量.armor_bottom_right
常量.云台左 = 常量.armor_top_left
常量.云台右 = 常量.armor_top_right

常量.效果常亮 = 常量.effect_always_on
常量.效果熄灭 = 常量.effect_always_off
常量.效果呼吸 = 常量.effect_breath
常量.效果闪烁 = 常量.effect_flash
常量.效果走马灯 = 常量.effect_marquee

时间 = time
时间.睡眠 = 时间.sleep